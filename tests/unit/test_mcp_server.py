from pathlib import Path

import pytest

from alexandria.infrastructure.config import ENV_DATA_DIR, ENV_REPO_ROOT, Config
from alexandria.mcp_server import (
    _extra_allowed_hosts,
    _http_token,
    build_transport_security,
    connector_urls,
    list_research,
    main,
    render_urls,
    search_research,
    show_research,
    status,
)


@pytest.fixture
def repo(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    repo_root = tmp_path / "repo"
    (repo_root / "docs").mkdir(parents=True)
    (repo_root / "docs" / "DESIGN.md").write_text("design", encoding="utf-8")
    (repo_root / "AGENTS.md").write_text("agents", encoding="utf-8")
    monkeypatch.setenv(ENV_REPO_ROOT, str(repo_root))
    monkeypatch.setenv(ENV_DATA_DIR, str(tmp_path / "state"))
    return repo_root


def test_status_reports_not_found_without_repo(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.delenv(ENV_REPO_ROOT, raising=False)
    monkeypatch.setenv(ENV_DATA_DIR, str(tmp_path / "state"))
    monkeypatch.chdir(tmp_path)
    assert "ALEXANDRIA_REPO" in status()


def test_status_reports_empty_research(repo: Path) -> None:
    result = status()
    assert str(repo) in result
    assert "No research investigations yet" in result


def test_status_counts_investigations_by_stage_and_assurance(repo: Path) -> None:
    investigation = repo / "research" / "2026-07-28-slug"
    (investigation / "00-topic").mkdir(parents=True)
    (investigation / "00-topic" / "topic.md").write_text("x", encoding="utf-8")
    (investigation / "topic.yaml").write_text("assurance_level: bronze\n", encoding="utf-8")
    result = status()
    assert "Investigations: 1" in result
    assert "00-topic: 1" in result
    assert "bronze: 1" in result


def test_list_research_filters_by_assurance(repo: Path) -> None:
    for slug, level in [("alpha", "bronze"), ("beta", "gold")]:
        investigation = repo / "research" / slug
        investigation.mkdir(parents=True)
        (investigation / "topic.yaml").write_text(
            f"title: {slug.title()}\nassurance_level: {level}\n", encoding="utf-8"
        )
    result = list_research(assurance="gold")
    assert "beta" in result
    assert "alpha" not in result


def test_show_research_reports_missing_slug(repo: Path) -> None:
    assert "No investigation" in show_research("nope")


def test_show_research_includes_readme(repo: Path) -> None:
    investigation = repo / "research" / "alpha"
    investigation.mkdir(parents=True)
    (investigation / "topic.yaml").write_text("title: Alpha\n", encoding="utf-8")
    (investigation / "README.md").write_text("Alpha investigation notes.", encoding="utf-8")
    result = show_research("alpha")
    assert "Alpha investigation notes." in result


def test_search_research_reports_matches(repo: Path) -> None:
    investigation = repo / "research" / "alpha"
    investigation.mkdir(parents=True)
    (investigation / "README.md").write_text("mentions warp drives here", encoding="utf-8")
    result = search_research("warp drives")
    assert "alpha/README.md" in result


def test_search_research_reports_no_matches(repo: Path) -> None:
    assert "No matches" in search_research("nonexistent-term")


def test_http_token_generated_and_stable(tmp_path: Path) -> None:
    config = Config(
        data_dir=tmp_path, data_dir_source="test", repo_root=tmp_path, repo_root_source="test"
    )
    first = _http_token(config)
    second = _http_token(config)
    assert first == second
    assert oct((tmp_path / "mcp-http-token").stat().st_mode)[-3:] == "600"


def test_extra_allowed_hosts_merges_cli_and_env() -> None:
    hosts = _extra_allowed_hosts(["a.example"], env={"ALEXANDRIA_ALLOWED_HOSTS": "b.example"})
    assert hosts == ["a.example", "b.example"]


def test_connector_urls_include_token() -> None:
    pairs = connector_urls("tok123", [], port=9000)
    assert dict(pairs)["MCP over HTTP"] == "http://127.0.0.1:9000/mcp/tok123"


def test_render_urls_formats_lines() -> None:
    assert render_urls("tok123", []) == ["MCP over HTTP: http://127.0.0.1:8787/mcp/tok123"]


def test_transport_security_always_includes_loopback() -> None:
    settings = build_transport_security(["tunnel.example"])
    assert "127.0.0.1:*" in settings.allowed_hosts
    assert settings.enable_dns_rebinding_protection is True


def test_http_mode_exits_cleanly_when_repo_not_found(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    """A missing/undetectable repo must be a clean exit(1) with a stderr
    message, never an uncaught RepoNotFoundError traceback — that's the
    difference between a client seeing "server error" on every reconnect
    and seeing why, once (regression test for the bug this was).
    """
    monkeypatch.delenv(ENV_REPO_ROOT, raising=False)
    monkeypatch.setenv(ENV_DATA_DIR, str(tmp_path / "state"))
    monkeypatch.chdir(tmp_path)
    with pytest.raises(SystemExit) as exc_info:
        main(["--http"])
    assert exc_info.value.code == 1
    assert "ALEXANDRIA_REPO" in capsys.readouterr().err
