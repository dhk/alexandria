"""Standard-library component checks shared by a tool-pack installer and front panel."""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.request
from collections.abc import Mapping, Sequence
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Literal

CheckState = Literal["pass", "fail", "skip"]


@dataclass(frozen=True)
class CheckResult:
    key: str
    label: str
    state: CheckState
    detail: str
    required: bool = True

    def as_dict(self) -> dict[str, object]:
        return asdict(self)


def _expanded(path: str) -> Path:
    return Path(os.path.expandvars(path)).expanduser().resolve()


def _read_env_names(path: Path) -> set[str]:
    if not path.is_file():
        return set()
    names: set[str] = set()
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if line and not line.startswith("#") and "=" in line:
            name, value = line.split("=", 1)
            if name.strip() and value.strip():
                names.add(name.strip())
    return names


def _command_check(entrypoint: str, timeout_seconds: float) -> CheckResult:
    executable = Path.home() / ".local" / "bin" / entrypoint
    if not executable.exists():
        found = shutil.which(entrypoint)
        executable = Path(found) if found else executable
    if not executable.exists():
        return CheckResult("command", "Installed command", "fail", f"missing {entrypoint}")
    try:
        completed = subprocess.run(
            [str(executable), "--help"],
            check=False,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=timeout_seconds,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        return CheckResult("command", "Installed command", "fail", str(exc))
    if completed.returncode != 0:
        return CheckResult(
            "command",
            "Installed command",
            "fail",
            f"{entrypoint} --help exited {completed.returncode}",
        )
    return CheckResult("command", "Installed command", "pass", f"{entrypoint} --help")


def _service_check(unit: str, timeout_seconds: float) -> CheckResult:
    if sys.platform != "linux" or shutil.which("systemctl") is None:
        return CheckResult(
            "service",
            "User service",
            "skip",
            "systemd user services are unavailable on this host",
        )
    deadline = time.monotonic() + timeout_seconds
    while True:
        try:
            completed = subprocess.run(
                ["systemctl", "--user", "is-active", unit],
                check=False,
                capture_output=True,
                text=True,
                timeout=timeout_seconds,
            )
        except (OSError, subprocess.TimeoutExpired) as exc:
            return CheckResult("service", "User service", "fail", str(exc))
        state = completed.stdout.strip() or completed.stderr.strip() or "unknown"
        if completed.returncode == 0 and state == "active":
            return CheckResult("service", "User service", "pass", f"{unit}: {state}")
        if state not in {"activating", "reloading"} or time.monotonic() >= deadline:
            return CheckResult("service", "User service", "fail", f"{unit}: {state}")
        time.sleep(0.2)


def _http_check(url: str, expected_service: str, timeout_seconds: float) -> CheckResult:
    try:
        with urllib.request.urlopen(url, timeout=timeout_seconds) as response:
            body = response.read(64 * 1024)
            if not 200 <= response.status < 300:
                raise OSError(f"HTTP {response.status}")
            payload = json.loads(body)
    except (OSError, ValueError, urllib.error.URLError) as exc:
        return CheckResult("health", "HTTP health", "fail", f"{url}: {exc}")
    if not isinstance(payload, dict) or payload.get("service") != expected_service:
        actual = payload.get("service") if isinstance(payload, dict) else None
        return CheckResult(
            "health",
            "HTTP health",
            "fail",
            f"{url}: expected {expected_service!r}, received {actual!r}",
        )
    version = payload.get("version") if isinstance(payload, dict) else None
    detail = f"{url} · version {version}" if version else url
    return CheckResult("health", "HTTP health", "pass", detail)


def run_component_checks(
    manifest: Mapping[str, Any],
    bundle_root: Path,
    *,
    install_root: Path | None = None,
    include_services: bool = True,
    timeout_seconds: float = 3.0,
) -> list[CheckResult]:
    """Run local, no-spend checks without returning secret values."""
    install = manifest.get("install")
    tool = manifest.get("tool")
    services = manifest.get("services")
    if (
        not isinstance(install, dict)
        or not isinstance(tool, dict)
        or not isinstance(services, list)
    ):
        return [CheckResult("manifest", "Pack manifest", "fail", "invalid manifest shape")]

    install_root = install_root or _expanded(str(install.get("default_root", "")))
    current = install_root / "current"
    release_ok = current.is_symlink() and current.resolve().is_dir()
    checks = [
        CheckResult(
            "release",
            "Current release",
            "pass" if release_ok else "fail",
            str(current.resolve()) if release_ok else f"missing managed link at {current}",
        )
    ]

    entrypoints = [
        str(service.get("entrypoint", ""))
        for service in services
        if isinstance(service, dict) and service.get("entrypoint")
    ]
    if entrypoints:
        checks.append(_command_check(entrypoints[0], timeout_seconds))

    secrets_file = _expanded(str(install.get("secrets_file", "")))
    required = install.get("required_secrets", [])
    required_names = [str(name) for name in required] if isinstance(required, list) else []
    configured = _read_env_names(secrets_file)
    missing = [name for name in required_names if name not in configured]
    checks.append(
        CheckResult(
            "configuration",
            "Research configuration",
            "pass" if not missing else "fail",
            str(secrets_file) if not missing else "missing " + ", ".join(missing),
            required=False,
        )
    )

    if include_services:
        for service in services:
            if not isinstance(service, dict):
                continue
            checks.append(_service_check(str(service.get("unit", "")), timeout_seconds))
            checks.append(
                _http_check(
                    str(service.get("health_url", "")),
                    str(service.get("health_service", "")),
                    timeout_seconds,
                )
            )
    else:
        checks.extend(
            [
                CheckResult("service", "User service", "skip", "service installation skipped"),
                CheckResult("health", "HTTP health", "skip", "service installation skipped"),
            ]
        )

    capability = manifest.get("capability")
    if isinstance(capability, dict):
        token_file = _expanded(str(capability.get("token_file", "")))
        token_ready = token_file.is_file() and bool(token_file.read_text(encoding="utf-8").strip())
        checks.append(
            CheckResult(
                "capability",
                "MCP capability",
                "pass" if token_ready else ("fail" if include_services else "skip"),
                str(token_file) if token_ready else "capability token has not been created",
            )
        )

    docs_ready = (bundle_root / "docs-index.html").is_file() and (bundle_root / "source").is_dir()
    checks.append(
        CheckResult(
            "documentation",
            "Documentation",
            "pass" if docs_ready else "fail",
            str(bundle_root / "docs-index.html")
            if docs_ready
            else "documentation payload incomplete",
        )
    )
    return checks


def required_checks_pass(checks: Sequence[CheckResult]) -> bool:
    return all(check.state != "fail" for check in checks if check.required)


def print_component_panel(checks: Sequence[CheckResult]) -> None:
    use_color = sys.stdout.isatty() and os.environ.get("NO_COLOR") is None
    colors = {"pass": "\033[32m", "fail": "\033[31m", "skip": "\033[33m"}
    reset = "\033[0m" if use_color else ""
    print("\nComponent check")
    for check in checks:
        marker = {"pass": "PASS", "fail": "FAIL", "skip": "SKIP"}[check.state]
        color = colors[check.state] if use_color else ""
        print(f"  {color}{marker:4}{reset}  {check.label}: {check.detail}")
