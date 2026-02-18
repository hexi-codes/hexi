from __future__ import annotations

import json
from pathlib import Path

import pytest

from hexi.adapters.memory_file import FileMemory
from hexi.core.domain import Event


def test_memory_initializes_default_files(tmp_path: Path) -> None:
    mem = FileMemory(tmp_path)
    mem.ensure_initialized()
    assert mem.config_path.exists()
    assert mem.local_config_path.exists()
    assert mem.runlog_path.exists()


def test_memory_loads_defaults(tmp_path: Path) -> None:
    mem = FileMemory(tmp_path)
    mem.ensure_initialized()
    cfg = mem.load_model_config()
    policy = mem.load_policy()

    assert cfg.provider == "openai_compat"
    assert cfg.model == "gpt-4o-mini"
    assert cfg.base_url == "https://api.openai.com/v1"
    assert "pytest" in policy.allow_commands


def test_memory_local_toml_overrides_main_config(tmp_path: Path) -> None:
    mem = FileMemory(tmp_path)
    mem.ensure_initialized()
    mem.local_config_path.write_text(
        """
[model]
provider = "openrouter_http"
model = "anthropic/claude-sonnet-4-6"

[providers.openrouter_http]
api_style = "anthropic"
""".strip(),
        encoding="utf-8",
    )

    cfg = mem.load_model_config()
    assert cfg.model == "anthropic/claude-sonnet-4-6"
    assert cfg.api_style == "anthropic"


def test_memory_resolve_api_key_from_local(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    mem = FileMemory(tmp_path)
    mem.ensure_initialized()
    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
    mem.local_config_path.write_text(
        """
[secrets]
openrouter_api_key = "abc"
""".strip(),
        encoding="utf-8",
    )

    key, source = mem.resolve_api_key("openrouter_http")
    assert key == "abc"
    assert source == "local"


def test_memory_rejects_invalid_allow_commands(tmp_path: Path) -> None:
    mem = FileMemory(tmp_path)
    mem.ensure_initialized()
    mem.config_path.write_text(
        """
[policy]
allow_commands = "pytest"
""".strip(),
        encoding="utf-8",
    )
    with pytest.raises(ValueError):
        mem.load_policy()


def test_memory_append_runlog_writes_jsonl(tmp_path: Path) -> None:
    mem = FileMemory(tmp_path)
    mem.ensure_initialized()

    ev = Event(type="progress", one_line_summary="hello", blocking=False, payload={"n": 1})
    mem.append_runlog(ev)

    lines = mem.runlog_path.read_text(encoding="utf-8").strip().splitlines()
    assert len(lines) == 1
    data = json.loads(lines[0])
    assert data["type"] == "progress"
    assert data["payload"]["n"] == 1
