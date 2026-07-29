#!/usr/bin/env python3
"""Install a pack bundle on Ubuntu without overwriting the prior release.

This file is copied to the root of every archive.  It deliberately uses only
the Python standard library available on a stock Ubuntu host; uv installs the
tool's requested Python and dependencies afterward.
"""

from __future__ import annotations

import argparse
import getpass
import json
import os
import shlex
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request
import uuid
from collections.abc import Callable, Mapping, Sequence
from pathlib import Path
from typing import Any

from deploy.checks import print_component_panel, required_checks_pass, run_component_checks


class InstallError(RuntimeError):
    """The bundle cannot be installed without risking the current release."""


Runner = Callable[[Sequence[str]], None]
_PACK_ROOT_MARKER = ".tool-pack-root.json"


def load_manifest(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise InstallError(f"cannot read {path}: {exc}") from exc
    if not isinstance(value, dict) or value.get("format_version") != 1:
        raise InstallError("unsupported or missing pack manifest")
    for key in ("bundle_id", "tool", "source", "install", "services"):
        if key not in value:
            raise InstallError(f"pack manifest is missing {key!r}")
    return value


def _expanded(path: str) -> Path:
    return Path(os.path.expandvars(path)).expanduser().resolve()


def _prompt_path(prompt: str, default: Path, input_fn: Callable[[str], str]) -> Path:
    answer = input_fn(f"{prompt} [{default}]: ").strip()
    return _expanded(answer) if answer else default


def _confirm(prompt: str, *, default: bool, input_fn: Callable[[str], str] = input) -> bool:
    suffix = "[Y/n]" if default else "[y/N]"
    answer = input_fn(f"{prompt} {suffix} ").strip().lower()
    if not answer:
        return default
    return answer in {"y", "yes"}


def _default_runner(command: Sequence[str]) -> None:
    print(f"→ {shlex.join(command)}", flush=True)
    subprocess.run(list(command), check=True)


def _read_env_names(path: Path) -> set[str]:
    if not path.is_file():
        return set()
    names: set[str] = set()
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if line and not line.startswith("#") and "=" in line:
            names.add(line.split("=", 1)[0].strip())
    return names


def ensure_secrets(
    path: Path,
    required: Sequence[str],
    *,
    environ: Mapping[str, str] | None = None,
    interactive: bool,
    secret_fn: Callable[[str], str] = getpass.getpass,
) -> list[str]:
    """Write missing secrets from env or hidden prompts; return unresolved names."""
    environment = os.environ if environ is None else environ
    existing = _read_env_names(path)
    additions: list[tuple[str, str]] = []
    unresolved: list[str] = []
    for name in required:
        if name in existing:
            continue
        value = environment.get(name, "").strip()
        if not value and interactive:
            value = secret_fn(f"{name} (leave blank to configure later): ").strip()
        if not value:
            unresolved.append(name)
            continue
        if "\n" in value or "\r" in value:
            raise InstallError(f"{name} contains a newline and cannot be written safely")
        additions.append((name, value))

    if additions or path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        previous = path.read_text(encoding="utf-8") if path.exists() else ""
        separator = "" if not previous or previous.endswith("\n") else "\n"
        payload = previous + separator + "".join(f"{name}={value}\n" for name, value in additions)
        path.write_text(payload, encoding="utf-8")
        path.chmod(0o600)
    return unresolved


def _systemd_quote(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def render_service_unit(
    service: Mapping[str, Any],
    *,
    home: Path,
    current: Path,
    repo_environment: str,
    secrets_file: Path,
) -> str:
    entrypoint = str(service["entrypoint"])
    arguments = [str(value) for value in service.get("args", [])]
    executable = home / ".local" / "bin" / entrypoint
    command = " ".join(_systemd_quote(value) for value in [str(executable), *arguments])
    return (
        "[Unit]\n"
        f"Description={service['description']}\n"
        "After=network-online.target\n"
        "Wants=network-online.target\n\n"
        "[Service]\n"
        "Type=simple\n"
        f"Environment={_systemd_quote(f'{repo_environment}={current}')}\n"
        f"EnvironmentFile={_systemd_quote('-' + str(secrets_file))}\n"
        f"WorkingDirectory={_systemd_quote(str(current))}\n"
        f"ExecStart={command}\n"
        "Restart=on-failure\n"
        "RestartSec=2\n\n"
        "[Install]\n"
        "WantedBy=default.target\n"
    )


def install_root_needs_adoption(root: Path, tool_name: str) -> bool:
    """Return whether an existing non-empty directory is not pack-managed."""
    if not root.exists():
        return False
    if not root.is_dir():
        raise InstallError(f"install root exists but is not a directory: {root}")
    marker = root / _PACK_ROOT_MARKER
    if marker.is_file():
        try:
            payload = json.loads(marker.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            raise InstallError(f"install-root marker is unreadable: {marker}") from exc
        if not isinstance(payload, dict) or payload.get("tool") != tool_name:
            raise InstallError(f"install root belongs to another tool: {root}")
        return False
    return any(root.iterdir())


def mark_install_root(root: Path, tool_name: str) -> None:
    root.mkdir(parents=True, exist_ok=True)
    marker = root / _PACK_ROOT_MARKER
    if marker.exists():
        return
    marker.write_text(
        json.dumps({"format_version": 1, "tool": tool_name}, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def install_release(source: Path, releases: Path, bundle_id: str, manifest: dict[str, Any]) -> Path:
    release = releases / bundle_id
    if release.exists():
        installed_manifest = release / ".pack-manifest.json"
        if not installed_manifest.is_file():
            raise InstallError(f"existing release has no manifest: {release}")
        existing = load_manifest(installed_manifest)
        if existing.get("bundle_id") != bundle_id:
            raise InstallError(f"existing release identity does not match: {release}")
        return release

    releases.mkdir(parents=True, exist_ok=True)
    staging = releases / f".{bundle_id}.staging-{uuid.uuid4().hex[:8]}"
    try:
        shutil.copytree(source, staging, symlinks=True)
        (staging / ".pack-manifest.json").write_text(
            json.dumps(manifest, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        staging.rename(release)
    except BaseException:
        shutil.rmtree(staging, ignore_errors=True)
        raise
    return release


def current_release(current: Path) -> Path | None:
    if not current.is_symlink():
        if current.exists():
            raise InstallError(f"{current} exists but is not a managed symlink")
        return None
    target = Path(os.readlink(current))
    return (current.parent / target).resolve() if not target.is_absolute() else target.resolve()


def switch_current(current: Path, release: Path) -> None:
    current.parent.mkdir(parents=True, exist_ok=True)
    temporary = current.with_name(f".{current.name}-{uuid.uuid4().hex[:8]}")
    temporary.symlink_to(release)
    os.replace(temporary, current)


def _find_uv() -> str | None:
    found = shutil.which("uv")
    if found:
        return found
    local = Path.home() / ".local" / "bin" / "uv"
    return str(local) if local.is_file() else None


def _install_uv(runner: Runner) -> str:
    print("Downloading uv's official installer from astral.sh…")
    with tempfile.TemporaryDirectory(prefix="tool-pack-uv-") as temporary:
        installer = Path(temporary) / "install.sh"
        try:
            with urllib.request.urlopen("https://astral.sh/uv/install.sh", timeout=30) as response:
                installer.write_bytes(response.read())
        except (OSError, urllib.error.URLError) as exc:
            raise InstallError(f"could not download uv: {exc}") from exc
        runner(["sh", str(installer)])
    uv = _find_uv()
    if uv is None:
        raise InstallError("uv installation finished but ~/.local/bin/uv was not found")
    return uv


def ensure_uv(*, interactive: bool, input_fn: Callable[[str], str], runner: Runner) -> str:
    uv = _find_uv()
    if uv:
        return uv
    if not interactive or not _confirm(
        "uv is required but not installed. Install it from astral.sh now?",
        default=True,
        input_fn=input_fn,
    ):
        raise InstallError("uv is required; install it from https://docs.astral.sh/uv/")
    return _install_uv(runner)


def _healthy(url: str, timeout_seconds: float = 15.0) -> bool:
    deadline = time.monotonic() + timeout_seconds
    while time.monotonic() < deadline:
        try:
            with urllib.request.urlopen(url, timeout=2) as response:
                if 200 <= response.status < 300:
                    return True
        except (OSError, urllib.error.URLError):
            time.sleep(0.25)
    return False


def _write_units(
    services: Sequence[Mapping[str, Any]],
    *,
    home: Path,
    current: Path,
    repo_environment: str,
    secrets_file: Path,
) -> list[str]:
    unit_dir = home / ".config" / "systemd" / "user"
    unit_dir.mkdir(parents=True, exist_ok=True)
    units: list[str] = []
    for service in services:
        unit = str(service["unit"])
        path = unit_dir / unit
        desired = render_service_unit(
            service,
            home=home,
            current=current,
            repo_environment=repo_environment,
            secrets_file=secrets_file,
        )
        existing = path.read_text(encoding="utf-8") if path.is_file() else None
        if existing == desired:
            units.append(unit)
            continue
        if existing is not None:
            timestamp = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())
            backup = path.with_name(f"{path.name}.bak-{timestamp}-{uuid.uuid4().hex[:6]}")
            shutil.copy2(path, backup)
            print(f"  preserved previous unit: {backup}")
        path.write_text(desired, encoding="utf-8")
        units.append(unit)
    return units


def _confirm_replacement(
    description: str,
    *,
    interactive: bool,
    input_fn: Callable[[str], str],
) -> None:
    if interactive and not _confirm(description, default=False, input_fn=input_fn):
        raise InstallError("aborted before replacing existing installation state")


def _restart_units(units: Sequence[str], runner: Runner) -> None:
    runner(["systemctl", "--user", "daemon-reload"])
    for unit in units:
        runner(["systemctl", "--user", "enable", unit])
        runner(["systemctl", "--user", "restart", unit])


def _offer_linger(*, interactive: bool, input_fn: Callable[[str], str], runner: Runner) -> None:
    if shutil.which("loginctl") is None:
        return
    username = getpass.getuser()
    result = subprocess.run(
        ["loginctl", "show-user", username, "-p", "Linger", "--value"],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.stdout.strip().lower() == "yes":
        return
    command = ["sudo", "loginctl", "enable-linger", username]
    if interactive and _confirm(
        "Enable systemd user-service linger so the tool survives logout/reboot?",
        default=True,
        input_fn=input_fn,
    ):
        runner(command)
    else:
        print(f"Linger is not enabled. Run later: {shlex.join(command)}")


def _print_capability(manifest: Mapping[str, Any]) -> None:
    raw = manifest.get("capability")
    if not isinstance(raw, dict):
        return
    token_file = _expanded(str(raw.get("token_file", "")))
    if not token_file.is_file():
        print(f"Capability token not found yet at {token_file}")
        return
    token = token_file.read_text(encoding="utf-8").strip()
    if not token:
        return
    print("\nCapability URLs (treat these like passwords):")
    for template in raw.get("urls", []):
        print(f"  {str(template).replace('{token}', token)}")


def _rollback(
    previous: Path | None,
    *,
    current: Path,
    uv: str,
    units: Sequence[str],
    runner: Runner,
) -> None:
    if previous is None or not previous.is_dir():
        print("No earlier release was available for automatic rollback.", file=sys.stderr)
        return
    print(f"Rolling back to {previous.name}…", file=sys.stderr)
    switch_current(current, previous)
    runner([uv, "tool", "install", "--reinstall", str(previous)])
    _restart_units(units, runner)


def main(argv: list[str] | None = None) -> int:
    bundle_root = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(
        prog="install.py",
        description="Install or upgrade this tool bundle with recoverable releases.",
    )
    parser.add_argument("--install-root", type=Path)
    parser.add_argument("--yes", action="store_true", help="accept defaults; never prompt")
    parser.add_argument("--skip-service", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument(
        "--check",
        action="store_true",
        help="run the installed component checks without changing anything",
    )
    args = parser.parse_args(argv)

    try:
        manifest = load_manifest(bundle_root / "pack-manifest.json")
        install = manifest["install"]
        tool = manifest["tool"]
        if not isinstance(install, dict) or not isinstance(tool, dict):
            raise InstallError("pack manifest install/tool sections must be objects")
        default_root = _expanded(str(install["default_root"]))
        if args.install_root:
            install_root = args.install_root.expanduser().resolve()
        elif args.yes or args.dry_run:
            install_root = default_root
        else:
            install_root = _prompt_path("Install root", default_root, input)
        releases = install_root / "releases"
        current = install_root / "current"
        source = bundle_root / "source"
        secrets_file = _expanded(str(install["secrets_file"]))
        services = manifest["services"]
        if not isinstance(services, list) or not all(isinstance(item, dict) for item in services):
            raise InstallError("pack manifest services must be an array of objects")
        if args.check:
            checks = run_component_checks(
                manifest,
                bundle_root,
                install_root=install_root,
                include_services=not args.skip_service,
            )
            print_component_panel(checks)
            return 0 if required_checks_pass(checks) else 1
        tool_name = str(tool["name"])
        adoption_needed = install_root_needs_adoption(install_root, tool_name)
        previous = current_release(current)
        release_path = releases / str(manifest["bundle_id"])
        command_paths = sorted(
            {Path.home() / ".local" / "bin" / str(service["entrypoint"]) for service in services},
            key=str,
        )
        existing_commands = [path for path in command_paths if path.exists() or path.is_symlink()]
        unit_dir = Path.home() / ".config" / "systemd" / "user"
        differing_units: list[Path] = []
        for service in services:
            unit_path = unit_dir / str(service["unit"])
            if unit_path.exists() and not unit_path.is_file():
                raise InstallError(f"systemd unit path is not a regular file: {unit_path}")
            desired = render_service_unit(
                service,
                home=Path.home(),
                current=current,
                repo_environment=str(install["repo_environment"]),
                secrets_file=secrets_file,
            )
            if unit_path.is_file() and unit_path.read_text(encoding="utf-8") != desired:
                differing_units.append(unit_path)

        if args.dry_run:
            print(f"Bundle: {manifest['bundle_id']}")
            print(f"Source: {source}")
            print(f"New release: {release_path}")
            print(
                f"Install root: {install_root} ({'needs adoption' if adoption_needed else 'available'})"
            )
            print(f"Current link: {current} -> {previous or 'not installed'}")
            print(f"Secrets: {secrets_file}")
            print("Services: " + ", ".join(str(item["unit"]) for item in services))
            print(
                "Existing commands: "
                + (", ".join(str(path) for path in existing_commands) or "none")
            )
            print(
                "Systemd units requiring backup/replacement: "
                + (", ".join(str(path) for path in differing_units) or "none")
            )
            return 0

        if sys.platform != "linux" and not args.skip_service:
            raise InstallError("service installation requires Linux; use --skip-service elsewhere")
        if not source.is_dir():
            raise InstallError(f"bundle source directory is missing: {source}")

        interactive = not args.yes
        if adoption_needed:
            if not interactive:
                raise InstallError(
                    f"{install_root} contains files from outside the pack installer; "
                    "rerun interactively to inspect and adopt it, or choose another --install-root"
                )
            _confirm_replacement(
                f"{install_root} already contains files. Adopt it without deleting anything?",
                interactive=True,
                input_fn=input,
            )
        if previous is not None and previous != release_path:
            _confirm_replacement(
                f"Switch {current} from {previous} to {release_path}? The old release is retained.",
                interactive=interactive,
                input_fn=input,
            )
        if existing_commands:
            _confirm_replacement(
                "uv will reinstall and replace these existing command links: "
                + ", ".join(str(path) for path in existing_commands)
                + ". Continue?",
                interactive=interactive,
                input_fn=input,
            )
        for unit_path in differing_units:
            _confirm_replacement(
                f"Back up and replace the differing systemd unit {unit_path}?",
                interactive=interactive,
                input_fn=input,
            )

        mark_install_root(install_root, tool_name)
        release = install_release(source, releases, str(manifest["bundle_id"]), manifest)
        if manifest.get("source", {}).get("dirty"):
            print("WARNING: this bundle contains uncommitted source changes.")
        uv = ensure_uv(interactive=interactive, input_fn=input, runner=_default_runner)
        _default_runner([uv, "tool", "install", "--reinstall", str(release)])

        required = install.get("required_secrets", [])
        if not isinstance(required, list) or not all(isinstance(item, str) for item in required):
            raise InstallError("required_secrets must be an array of names")
        unresolved = ensure_secrets(
            secrets_file,
            required,
            interactive=interactive,
        )
        if unresolved:
            print("Secrets still required before research can run: " + ", ".join(unresolved))

        switch_current(current, release)
        units: list[str] = []
        if not args.skip_service:
            if shutil.which("systemctl") is None:
                raise InstallError(
                    "systemctl is unavailable; use --skip-service for a tool-only install"
                )
            units = _write_units(
                services,
                home=Path.home(),
                current=current,
                repo_environment=str(install["repo_environment"]),
                secrets_file=secrets_file,
            )
            try:
                _restart_units(units, _default_runner)
                failed = [
                    str(service["health_url"])
                    for service in services
                    if not _healthy(str(service["health_url"]))
                ]
                if failed:
                    raise InstallError("health checks failed: " + ", ".join(failed))
            except (OSError, InstallError, subprocess.CalledProcessError):
                _rollback(
                    previous,
                    current=current,
                    uv=uv,
                    units=units,
                    runner=_default_runner,
                )
                raise
        checks = run_component_checks(
            manifest,
            bundle_root,
            install_root=install_root,
            include_services=not args.skip_service,
        )
        print_component_panel(checks)
        if not required_checks_pass(checks):
            if units:
                _rollback(
                    previous,
                    current=current,
                    uv=uv,
                    units=units,
                    runner=_default_runner,
                )
            raise InstallError("one or more required component checks failed")
        if units:
            _offer_linger(interactive=interactive, input_fn=input, runner=_default_runner)

        print(f"\nInstalled {tool['display_name']} {tool['version']}")
        print(f"Current release: {current} -> {release}")
        print("Older releases remain under " + str(releases))
        print(f"Bundle documentation: {bundle_root / 'launch-docs.py'}")
        _print_capability(manifest)
        return 0
    except (KeyError, OSError, InstallError, subprocess.CalledProcessError) as exc:
        print(f"install: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
