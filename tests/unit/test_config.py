from pathlib import Path

import pytest

from alexandria.infrastructure.config import (
    ENV_DATA_DIR,
    ENV_REPO_ROOT,
    RepoNotFoundError,
    load_config,
)


def _make_repo(tmp_path: Path) -> Path:
    repo = tmp_path / "repo"
    (repo / "docs").mkdir(parents=True)
    (repo / "docs" / "DESIGN.md").write_text("design", encoding="utf-8")
    (repo / "AGENTS.md").write_text("agents", encoding="utf-8")
    return repo


def test_repo_root_env_override_wins(tmp_path: Path) -> None:
    repo = _make_repo(tmp_path)
    config = load_config({ENV_REPO_ROOT: str(repo)}, cwd=tmp_path)
    assert config.repo_root == repo
    assert config.repo_root_source == f"{ENV_REPO_ROOT} environment variable"


def test_repo_root_detected_from_cwd(tmp_path: Path) -> None:
    repo = _make_repo(tmp_path)
    nested = repo / "research" / "some-slug"
    nested.mkdir(parents=True)
    config = load_config({}, cwd=nested)
    assert config.repo_root == repo


def test_repo_root_not_found_raises(tmp_path: Path) -> None:
    with pytest.raises(RepoNotFoundError):
        load_config({}, cwd=tmp_path)


def test_data_dir_env_override_wins(tmp_path: Path) -> None:
    repo = _make_repo(tmp_path)
    config = load_config(
        {ENV_DATA_DIR: str(tmp_path / "state"), ENV_REPO_ROOT: str(repo)}, cwd=tmp_path
    )
    assert config.data_dir == tmp_path / "state"
    assert config.data_dir_source == f"{ENV_DATA_DIR} environment variable"


def test_research_dir_derived_from_repo_root(tmp_path: Path) -> None:
    repo = _make_repo(tmp_path)
    config = load_config({ENV_REPO_ROOT: str(repo)}, cwd=tmp_path)
    assert config.research_dir == repo / "research"
