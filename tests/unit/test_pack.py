from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tarfile
from pathlib import Path

import pytest

from deploy.checks import required_checks_pass, run_component_checks
from deploy.install import (
    InstallError,
    _write_units,
    ensure_secrets,
    install_root_needs_adoption,
    mark_install_root,
    render_service_unit,
)
from scripts.pack import (
    PackError,
    PackSpec,
    ServiceSpec,
    build_bundle,
    load_spec,
    source_files,
)

ROOT = Path(__file__).resolve().parents[2]


def _git(repo: Path, *args: str) -> None:
    subprocess.run(["git", *args], cwd=repo, check=True, capture_output=True)


def _repo(tmp_path: Path) -> Path:
    repo = tmp_path / "tool"
    repo.mkdir()
    (repo / "deploy").mkdir()
    (repo / "pyproject.toml").write_text(
        '[project]\nname = "sample-tool"\nversion = "1.2.3"\n', encoding="utf-8"
    )
    (repo / "README.md").write_text("committed\n", encoding="utf-8")
    (repo / ".gitignore").write_text("ignored.txt\ndist/\n", encoding="utf-8")
    (repo / "deploy/install.py").write_text("#!/usr/bin/env python3\n", encoding="utf-8")
    (repo / "deploy/docs.py").write_text("#!/usr/bin/env python3\n", encoding="utf-8")
    (repo / "deploy/checks.py").write_text(
        (ROOT / "deploy/checks.py").read_text(encoding="utf-8"), encoding="utf-8"
    )
    _git(repo, "init")
    _git(repo, "config", "user.email", "pack@example.test")
    _git(repo, "config", "user.name", "Pack Test")
    _git(repo, "add", ".")
    _git(repo, "commit", "-m", "fixture")
    return repo


def _spec() -> PackSpec:
    return PackSpec(
        format_version=1,
        name="sample-tool",
        display_name="Sample Tool",
        default_install_root="~/.local/opt/sample-tool",
        repo_environment="SAMPLE_REPO",
        secrets_file="~/.config/sample-tool/secrets.env",
        required_secrets=["SAMPLE_API_KEY"],
        exclude=[],
        services=[
            ServiceSpec(
                unit="sample-tool.service",
                description="Sample Tool",
                entrypoint="sample-tool",
                args=["serve"],
                health_url="http://127.0.0.1:9000/health",
            )
        ],
        capability=None,
    )


def test_alexandria_pack_config_is_valid() -> None:
    spec = load_spec(ROOT / "deploy/pack.toml")

    assert spec.name == "alexandria"
    assert spec.default_install_root == "~/src/alexandria"
    assert spec.required_secrets == ["OPENROUTER_API_KEY"]
    assert spec.services[0].unit == "alexandria-mcp.service"


def test_source_set_includes_worktree_files_but_not_ignored_or_secret_files(
    tmp_path: Path,
) -> None:
    repo = _repo(tmp_path)
    (repo / "README.md").write_text("working tree\n", encoding="utf-8")
    (repo / "notes.txt").write_text("include me\n", encoding="utf-8")
    (repo / "ignored.txt").write_text("ignore me\n", encoding="utf-8")
    (repo / "secrets.env").write_text("SAMPLE_API_KEY=secret\n", encoding="utf-8")

    files = source_files(repo, [])

    assert Path("README.md") in files
    assert Path("notes.txt") in files
    assert Path("ignored.txt") not in files
    assert Path("secrets.env") not in files


def test_build_bundle_contains_manifest_installer_and_current_worktree(tmp_path: Path) -> None:
    repo = _repo(tmp_path)
    (repo / "README.md").write_text("working tree\n", encoding="utf-8")
    (repo / "notes.txt").write_text("untracked\n", encoding="utf-8")

    result = build_bundle(repo, _spec(), tmp_path / "output")

    assert result.archive.is_file()
    assert result.checksum.is_file()
    with tarfile.open(result.archive, "r:gz") as bundle:
        names = set(bundle.getnames())
        readme_name = f"{result.bundle_root}/source/README.md"
        assert f"{result.bundle_root}/install.py" in names
        assert f"{result.bundle_root}/launch-docs.py" in names
        assert f"{result.bundle_root}/deploy/__init__.py" in names
        assert f"{result.bundle_root}/deploy/checks.py" in names
        assert f"{result.bundle_root}/docs-index.html" in names
        assert f"{result.bundle_root}/pack-manifest.json" in names
        assert f"{result.bundle_root}/source/notes.txt" in names
        extracted = bundle.extractfile(readme_name)
        assert extracted is not None
        assert extracted.read() == b"working tree\n"


def test_build_bundle_requires_opt_in_for_large_files(tmp_path: Path) -> None:
    repo = _repo(tmp_path)
    (repo / "large.bin").write_bytes(b"x" * 32)

    with pytest.raises(PackError, match="exceed the size limit"):
        build_bundle(repo, _spec(), tmp_path / "output", max_file_bytes=16)


def test_ensure_secrets_uses_environment_without_echoing_value(tmp_path: Path) -> None:
    path = tmp_path / ".config" / "sample" / "secrets.env"

    unresolved = ensure_secrets(
        path,
        ["SAMPLE_API_KEY"],
        environ={"SAMPLE_API_KEY": "secret-value"},
        interactive=False,
    )

    assert unresolved == []
    assert path.read_text(encoding="utf-8") == "SAMPLE_API_KEY=secret-value\n"
    assert os.stat(path).st_mode & 0o777 == 0o600


def test_ensure_secrets_never_replaces_an_existing_value(tmp_path: Path) -> None:
    path = tmp_path / "secrets.env"
    path.write_text("SAMPLE_API_KEY=original\n", encoding="utf-8")

    unresolved = ensure_secrets(
        path,
        ["SAMPLE_API_KEY"],
        environ={"SAMPLE_API_KEY": "replacement"},
        interactive=False,
    )

    assert unresolved == []
    assert path.read_text(encoding="utf-8") == "SAMPLE_API_KEY=original\n"


def test_existing_install_root_must_be_adopted_and_is_never_cleared(tmp_path: Path) -> None:
    root = tmp_path / "existing"
    root.mkdir()
    existing = root / "keep.txt"
    existing.write_text("keep me\n", encoding="utf-8")

    assert install_root_needs_adoption(root, "sample-tool") is True
    mark_install_root(root, "sample-tool")

    assert install_root_needs_adoption(root, "sample-tool") is False
    assert existing.read_text(encoding="utf-8") == "keep me\n"


def test_install_root_owned_by_another_tool_is_refused(tmp_path: Path) -> None:
    root = tmp_path / "existing"
    mark_install_root(root, "another-tool")

    with pytest.raises(InstallError, match="belongs to another tool"):
        install_root_needs_adoption(root, "sample-tool")


def test_render_service_unit_pins_repo_and_secret_file(tmp_path: Path) -> None:
    service = {
        "description": "Sample Tool",
        "entrypoint": "sample-tool",
        "args": ["serve"],
    }
    unit = render_service_unit(
        service,
        home=tmp_path,
        current=tmp_path / ".local/opt/sample/current",
        repo_environment="SAMPLE_REPO",
        secrets_file=tmp_path / ".config/sample/secrets.env",
    )

    assert "SAMPLE_REPO=" in unit
    assert f"EnvironmentFile=-{tmp_path}/.config/sample/secrets.env" in unit
    assert f"WorkingDirectory={tmp_path}/.local/opt/sample/current" in unit
    assert 'ExecStart="' in unit
    assert 'sample-tool" "serve' in unit


def test_rendered_service_unit_passes_systemd_parser_when_available(tmp_path: Path) -> None:
    systemd_analyze = shutil.which("systemd-analyze")
    if systemd_analyze is None:
        pytest.skip("systemd-analyze is not installed")
    executable = tmp_path / ".local" / "bin" / "sample-tool"
    executable.parent.mkdir(parents=True)
    executable.write_text("#!/bin/sh\nexit 0\n", encoding="utf-8")
    executable.chmod(0o755)
    current = tmp_path / "src" / "sample" / "current"
    current.mkdir(parents=True)
    secrets = tmp_path / ".config" / "sample" / "secrets.env"
    secrets.parent.mkdir(parents=True)
    secrets.write_text("SAMPLE_API_KEY=test\n", encoding="utf-8")
    unit = render_service_unit(
        {
            "description": "Sample Tool",
            "entrypoint": "sample-tool",
            "args": ["serve"],
        },
        home=tmp_path,
        current=current,
        repo_environment="SAMPLE_REPO",
        secrets_file=secrets,
    )
    unit_path = tmp_path / "sample-tool.service"
    unit_path.write_text(unit, encoding="utf-8")

    completed = subprocess.run(
        [systemd_analyze, "--user", "verify", str(unit_path)],
        check=False,
        capture_output=True,
        text=True,
    )

    assert completed.returncode == 0, completed.stderr


def test_differing_systemd_unit_is_backed_up_before_replacement(tmp_path: Path) -> None:
    unit_dir = tmp_path / ".config" / "systemd" / "user"
    unit_dir.mkdir(parents=True)
    unit = unit_dir / "sample-tool.service"
    unit.write_text("old unit\n", encoding="utf-8")
    service = {
        "unit": "sample-tool.service",
        "description": "Sample Tool",
        "entrypoint": "sample-tool",
        "args": ["serve"],
    }

    units = _write_units(
        [service],
        home=tmp_path,
        current=tmp_path / "src/sample/current",
        repo_environment="SAMPLE_REPO",
        secrets_file=tmp_path / ".config/sample/secrets.env",
    )

    backups = list(unit_dir.glob("sample-tool.service.bak-*"))
    assert units == ["sample-tool.service"]
    assert len(backups) == 1
    assert backups[0].read_text(encoding="utf-8") == "old unit\n"
    assert unit.read_text(encoding="utf-8") != "old unit\n"


def test_checksum_uses_sha256sum_format(tmp_path: Path) -> None:
    repo = _repo(tmp_path)
    result = build_bundle(repo, _spec(), tmp_path / "output")
    digest, filename = result.checksum.read_text(encoding="utf-8").strip().split(maxsplit=1)

    assert len(digest) == 64
    assert filename == result.archive.name
    int(digest, 16)


def test_extracted_installer_dry_run_never_prompts(tmp_path: Path) -> None:
    repo = _repo(tmp_path)
    (repo / "deploy/install.py").write_text(
        (ROOT / "deploy/install.py").read_text(encoding="utf-8"), encoding="utf-8"
    )
    result = build_bundle(repo, _spec(), tmp_path / "output")
    extracted = tmp_path / "extracted"
    with tarfile.open(result.archive, "r:gz") as bundle:
        bundle.extractall(extracted, filter="data")

    completed = subprocess.run(
        [sys.executable, str(extracted / result.bundle_root / "install.py"), "--dry-run"],
        check=True,
        capture_output=True,
        text=True,
        stdin=subprocess.DEVNULL,
    )

    assert "New release:" in completed.stdout


def test_noninteractive_installer_refuses_an_unmanaged_directory(tmp_path: Path) -> None:
    repo = _repo(tmp_path)
    (repo / "deploy/install.py").write_text(
        (ROOT / "deploy/install.py").read_text(encoding="utf-8"), encoding="utf-8"
    )
    result = build_bundle(repo, _spec(), tmp_path / "output")
    extracted = tmp_path / "extracted"
    with tarfile.open(result.archive, "r:gz") as bundle:
        bundle.extractall(extracted, filter="data")
    install_root = tmp_path / "existing"
    install_root.mkdir()
    existing = install_root / "keep.txt"
    existing.write_text("keep me\n", encoding="utf-8")

    completed = subprocess.run(
        [
            sys.executable,
            str(extracted / result.bundle_root / "install.py"),
            "--yes",
            "--skip-service",
            "--install-root",
            str(install_root),
        ],
        check=False,
        capture_output=True,
        text=True,
        stdin=subprocess.DEVNULL,
    )

    assert completed.returncode == 1
    assert "contains files from outside the pack installer" in completed.stderr
    assert existing.read_text(encoding="utf-8") == "keep me\n"
    assert not (install_root / ".tool-pack-root.json").exists()


def test_extracted_docs_launcher_validates_payload(tmp_path: Path) -> None:
    repo = _repo(tmp_path)
    (repo / "deploy/docs.py").write_text(
        (ROOT / "deploy/docs.py").read_text(encoding="utf-8"), encoding="utf-8"
    )
    result = build_bundle(repo, _spec(), tmp_path / "output")
    extracted = tmp_path / "extracted"
    with tarfile.open(result.archive, "r:gz") as bundle:
        bundle.extractall(extracted, filter="data")

    completed = subprocess.run(
        [sys.executable, str(extracted / result.bundle_root / "launch-docs.py"), "--check"],
        check=True,
        capture_output=True,
        text=True,
        stdin=subprocess.DEVNULL,
    )

    assert "Documentation ready:" in completed.stdout


def test_component_panel_proves_release_command_config_and_docs(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    home = tmp_path / "home"
    install_root = home / "src" / "sample-tool"
    release = install_root / "releases" / "release-1"
    release.mkdir(parents=True)
    install_root.mkdir(parents=True, exist_ok=True)
    (install_root / "current").symlink_to(release)
    executable = home / ".local" / "bin" / "sample-tool"
    executable.parent.mkdir(parents=True)
    executable.write_text("#!/bin/sh\nexit 0\n", encoding="utf-8")
    executable.chmod(0o755)
    secrets = home / ".config" / "sample-tool" / "secrets.env"
    secrets.parent.mkdir(parents=True)
    secrets.write_text("SAMPLE_API_KEY=configured\n", encoding="utf-8")
    bundle = tmp_path / "bundle"
    (bundle / "source").mkdir(parents=True)
    (bundle / "docs-index.html").write_text("docs\n", encoding="utf-8")
    monkeypatch.setenv("HOME", str(home))
    manifest = {
        "tool": {"name": "sample-tool"},
        "install": {
            "default_root": "~/src/sample-tool",
            "secrets_file": "~/.config/sample-tool/secrets.env",
            "required_secrets": ["SAMPLE_API_KEY"],
        },
        "services": [
            {
                "unit": "sample-tool.service",
                "entrypoint": "sample-tool",
                "health_url": "http://127.0.0.1:9000/health",
            }
        ],
        "capability": {"token_file": "~/.local/share/sample-tool/token"},
    }

    checks = run_component_checks(manifest, bundle, include_services=False)

    by_key = {check.key: check for check in checks}
    assert by_key["release"].state == "pass"
    assert by_key["command"].state == "pass"
    assert by_key["configuration"].state == "pass"
    assert by_key["service"].state == "skip"
    assert by_key["health"].state == "skip"
    assert by_key["capability"].state == "skip"
    assert by_key["documentation"].state == "pass"
    assert required_checks_pass(checks)


def test_docs_index_contains_toggle_driven_component_front_panel(tmp_path: Path) -> None:
    repo = _repo(tmp_path)

    result = build_bundle(repo, _spec(), tmp_path / "output")

    with tarfile.open(result.archive, "r:gz") as bundle:
        extracted = bundle.extractfile(f"{result.bundle_root}/docs-index.html")
        assert extracted is not None
        index = extracted.read().decode()
    assert "Installation front panel" in index
    assert "Opening this panel runs local" in index
    assert "fetch('/__pack/checks'" in index
    assert "panel.addEventListener('toggle'" in index
