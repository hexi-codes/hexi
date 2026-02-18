from __future__ import annotations

from pathlib import Path

import pytest
from typer.testing import CliRunner

from hexi.cli import app
from hexi.core.domain import ModelConfig

runner = CliRunner()


class FakeWS:
    def __init__(self, root: Path) -> None:
        self._root = root

    def repo_root(self) -> Path:
        return self._root

    def git_diff(self, max_chars: int) -> str:
        return "diff-content"


class FakeMemory:
    def __init__(self, root: Path, provider: str = "openai_compat", key_source: str | None = None) -> None:
        self.root = root
        self.provider = provider
        self._key_source = key_source
        self.config_path = root / ".hexi/config.toml"
        self.local_config_path = root / ".hexi/local.toml"
        self.runlog_path = root / ".hexi/runlog.jsonl"
        self.onboard_written: tuple[str, str, str | None, str | None] | None = None

    def ensure_initialized(self) -> None:
        return None

    def load_model_config(self) -> ModelConfig:
        return ModelConfig(provider=self.provider, model="m", base_url="u")

    def resolve_api_key(self, provider: str) -> tuple[str | None, str | None]:
        if self._key_source is None:
            return None, None
        return "k", self._key_source

    def apply_api_key_to_env(self, provider: str) -> str | None:
        return self._key_source

    def write_local_onboarding(self, provider: str, model: str, api_style: str | None, api_key: str | None) -> None:
        self.onboard_written = (provider, model, api_style, api_key)


def test_cli_init_success(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    mem = FakeMemory(tmp_path)
    monkeypatch.setattr("hexi.cli._bootstrap_memory", lambda: (mem, tmp_path, True))

    result = runner.invoke(app, ["init"])
    assert result.exit_code == 0
    assert "Initialized Hexi" in result.stdout


def test_cli_diff_success(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    ws = FakeWS(tmp_path)
    mem = FakeMemory(tmp_path)
    monkeypatch.setattr("hexi.cli._workspace_and_memory", lambda: (ws, mem))

    result = runner.invoke(app, ["diff"])
    assert result.exit_code == 0
    assert "diff-content" in result.stdout


def test_cli_doctor_warns_when_key_missing(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    mem = FakeMemory(tmp_path, provider="openrouter_http", key_source=None)
    monkeypatch.setattr("hexi.cli._bootstrap_memory", lambda: (mem, tmp_path, True))

    result = runner.invoke(app, ["doctor"])
    assert result.exit_code == 1
    assert "Missing API key" in result.stdout


def test_cli_doctor_passes_with_local_key(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    mem = FakeMemory(tmp_path, provider="openrouter_http", key_source="local")
    monkeypatch.setattr("hexi.cli._bootstrap_memory", lambda: (mem, tmp_path, True))

    result = runner.invoke(app, ["doctor"])
    assert result.exit_code == 0
    assert "API key source: local" in result.stdout


def test_cli_doctor_bootstrap_mode_without_git(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    mem = FakeMemory(tmp_path, provider="openrouter_http", key_source="local")
    monkeypatch.setattr("hexi.cli._bootstrap_memory", lambda: (mem, tmp_path, False))

    result = runner.invoke(app, ["doctor"])
    assert result.exit_code == 0
    assert "No git repository yet (bootstrap mode)" in result.stdout


def test_cli_onboard_writes_local_config(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    mem = FakeMemory(tmp_path)
    monkeypatch.setattr("hexi.cli._bootstrap_memory", lambda: (mem, tmp_path, True))

    user_input = "openrouter_http\nopenai/gpt-4o-mini\nopenai\ny\nabc123\n"
    result = runner.invoke(app, ["onboard"], input=user_input)

    assert result.exit_code == 0
    assert mem.onboard_written == ("openrouter_http", "openai/gpt-4o-mini", "openai", "abc123")


def test_cli_init_bootstrap_mode_without_git(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    mem = FakeMemory(tmp_path)
    monkeypatch.setattr("hexi.cli._bootstrap_memory", lambda: (mem, tmp_path, False))

    result = runner.invoke(app, ["init"])
    assert result.exit_code == 0
    assert "Bootstrap Mode" in result.stdout


def test_cli_plan_check_valid_inline_json() -> None:
    payload = (
        '{'
        '"summary":"one step",'
        '"actions":[{"kind":"write","path":"a.txt","content":"x"},{"kind":"run","command":"pytest -q"}]'
        '}'
    )
    result = runner.invoke(app, ["plan-check", "--json", payload])
    assert result.exit_code == 0
    assert "Plan Check Passed" in result.stdout
    assert "write" in result.stdout
    assert "run" in result.stdout


def test_cli_plan_check_invalid_inline_json() -> None:
    result = runner.invoke(app, ["plan-check", "--json", '{"summary":"x","actions":[] }'])
    assert result.exit_code == 1
    assert "Plan Check Failed" in result.stdout
