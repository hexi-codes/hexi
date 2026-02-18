from __future__ import annotations

import pytest

from hexi.adapters.model_anthropic_compat import AnthropicCompatModel
from hexi.adapters.model_openai_compat import OpenAICompatModel
from hexi.core.domain import ModelConfig


def test_openai_adapter_builds_expected_request(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("OPENAI_API_KEY", "k")

    captured = {}

    def fake_post_json(url, headers, payload):
        captured["url"] = url
        captured["headers"] = headers
        captured["payload"] = payload
        return {"choices": [{"message": {"content": '{"summary":"x","actions":[{"kind":"emit","event_type":"done","message":"m","blocking":false}]}'}}]}

    monkeypatch.setattr("hexi.adapters.model_openai_compat.post_json", fake_post_json)

    cfg = ModelConfig(provider="openai_compat", model="gpt-4o-mini", base_url="https://api.example.com/v1")
    out = OpenAICompatModel().plan_step(cfg, "sys", "usr")

    assert captured["url"] == "https://api.example.com/v1/chat/completions"
    assert captured["headers"]["Authorization"] == "Bearer k"
    assert captured["payload"]["messages"][0]["content"] == "sys"
    assert out.startswith('{"summary"')


def test_anthropic_adapter_builds_expected_request(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("ANTHROPIC_API_KEY", "k")

    captured = {}

    def fake_post_json(url, headers, payload):
        captured["url"] = url
        captured["headers"] = headers
        captured["payload"] = payload
        return {"content": [{"text": '{"summary":"x","actions":[{"kind":"emit","event_type":"done","message":"m","blocking":false}]}' }]}

    monkeypatch.setattr("hexi.adapters.model_anthropic_compat.post_json", fake_post_json)

    cfg = ModelConfig(provider="anthropic_compat", model="claude-3-5-sonnet", base_url="https://anth.example.com")
    out = AnthropicCompatModel().plan_step(cfg, "sys", "usr")

    assert captured["url"] == "https://anth.example.com/v1/messages"
    assert captured["headers"]["x-api-key"] == "k"
    assert captured["payload"]["system"] == "sys"
    assert out.startswith('{"summary"')


def test_anthropic_adapter_requires_text_in_response(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("ANTHROPIC_API_KEY", "k")

    def fake_post_json(url, headers, payload):
        return {"content": []}

    monkeypatch.setattr("hexi.adapters.model_anthropic_compat.post_json", fake_post_json)

    cfg = ModelConfig(provider="anthropic_compat", model="claude-3-5-sonnet", base_url=None)
    with pytest.raises(RuntimeError):
        AnthropicCompatModel().plan_step(cfg, "sys", "usr")
