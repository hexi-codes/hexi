from __future__ import annotations

import asyncio
import sys
import types
from typing import Any

import pytest

from hexi.adapters.model_openrouter_http import OpenRouterHTTPModel
from hexi.adapters.model_openrouter_sdk import OpenRouterSDKModel
from hexi.core.domain import ModelConfig


class _FakeResponse:
    def __init__(self, status_code: int, payload: dict[str, Any], text: str = "") -> None:
        self.status_code = status_code
        self._payload = payload
        self.text = text or str(payload)

    def json(self) -> dict[str, Any]:
        return self._payload


def test_openrouter_http_openai_sync(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("OPENROUTER_API_KEY", "k")

    captured: dict[str, Any] = {}

    def fake_post(url: str, headers: dict[str, str], json: dict[str, Any], timeout: int) -> _FakeResponse:
        captured["url"] = url
        captured["headers"] = headers
        captured["json"] = json
        return _FakeResponse(200, {"choices": [{"message": {"content": '{"summary":"ok","actions":[{"kind":"emit","event_type":"done","message":"m","blocking":false}]}'}}]})

    class _ReqLib:
        @staticmethod
        def post(url: str, headers: dict[str, str], json: dict[str, Any], timeout: int) -> _FakeResponse:
            return fake_post(url, headers, json, timeout)

    monkeypatch.setattr("hexi.adapters.model_openrouter_http.requests_lib", _ReqLib)

    model = OpenRouterHTTPModel()
    cfg = ModelConfig(provider="openrouter_http", model="openai/gpt-4o-mini", base_url="https://openrouter.ai/api/v1", api_style="openai")
    out = model.plan_step(cfg, "sys", "usr")

    assert captured["url"].endswith("/chat/completions")
    assert captured["headers"]["Authorization"] == "Bearer k"
    assert captured["json"]["messages"][0]["role"] == "system"
    assert out.startswith('{"summary"')


def test_openrouter_http_anthropic_sync_error(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("OPENROUTER_API_KEY", "k")

    def fake_post(url: str, headers: dict[str, str], json: dict[str, Any], timeout: int) -> _FakeResponse:
        return _FakeResponse(401, {"error": "unauthorized"}, text="unauthorized")

    class _ReqLib:
        @staticmethod
        def post(url: str, headers: dict[str, str], json: dict[str, Any], timeout: int) -> _FakeResponse:
            return fake_post(url, headers, json, timeout)

    monkeypatch.setattr("hexi.adapters.model_openrouter_http.requests_lib", _ReqLib)

    model = OpenRouterHTTPModel()
    cfg = ModelConfig(provider="openrouter_http", model="anthropic/claude-sonnet-4-6", base_url=None, api_style="anthropic")
    with pytest.raises(RuntimeError):
        model.plan_step(cfg, "sys", "usr")


def test_openrouter_http_openai_async(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("OPENROUTER_API_KEY", "k")

    class _FakeAsyncClient:
        def __init__(self, timeout: float) -> None:
            self.timeout = timeout

        async def __aenter__(self) -> "_FakeAsyncClient":
            return self

        async def __aexit__(self, exc_type, exc, tb) -> None:
            return None

        async def post(self, url: str, headers: dict[str, str], json: dict[str, Any]) -> _FakeResponse:
            return _FakeResponse(200, {"choices": [{"message": {"content": '{"summary":"ok","actions":[{"kind":"emit","event_type":"done","message":"m","blocking":false}]}'}}]})

    monkeypatch.setattr("httpx.AsyncClient", _FakeAsyncClient)

    model = OpenRouterHTTPModel()
    cfg = ModelConfig(provider="openrouter_http", model="openai/gpt-4o-mini", base_url=None, api_style="openai")
    out = asyncio.run(model.aplan_step(cfg, "sys", "usr"))
    assert out.startswith('{"summary"')


def test_openrouter_http_requires_requests_dependency(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("OPENROUTER_API_KEY", "k")
    monkeypatch.setattr("hexi.adapters.model_openrouter_http.requests_lib", None)

    model = OpenRouterHTTPModel()
    cfg = ModelConfig(provider="openrouter_http", model="openai/gpt-4o-mini", base_url=None, api_style="openai")
    with pytest.raises(RuntimeError):
        model.plan_step(cfg, "sys", "usr")


def test_openrouter_sdk_sync(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("OPENROUTER_API_KEY", "k")

    class _Resp:
        def __init__(self) -> None:
            self.choices = [types.SimpleNamespace(message=types.SimpleNamespace(content='{"summary":"ok","actions":[{"kind":"emit","event_type":"done","message":"m","blocking":false}]}'))]

    class _Chat:
        def send(self, messages, model):
            return _Resp()

        async def send_async(self, messages, model):
            return _Resp()

    class _Client:
        def __init__(self, api_key: str) -> None:
            self.chat = _Chat()

    fake_module = types.SimpleNamespace(OpenRouter=_Client)
    monkeypatch.setitem(sys.modules, "openrouter", fake_module)

    model = OpenRouterSDKModel()
    cfg = ModelConfig(provider="openrouter_sdk", model="openai/gpt-4o-mini", base_url=None)
    out = model.plan_step(cfg, "sys", "usr")
    assert out.startswith('{"summary"')


def test_openrouter_sdk_async(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("OPENROUTER_API_KEY", "k")

    class _Resp:
        def __init__(self) -> None:
            self.choices = [types.SimpleNamespace(message=types.SimpleNamespace(content='{"summary":"ok","actions":[{"kind":"emit","event_type":"done","message":"m","blocking":false}]}'))]

    class _Chat:
        def send(self, messages, model):
            return _Resp()

        async def send_async(self, messages, model):
            return _Resp()

    class _Client:
        def __init__(self, api_key: str) -> None:
            self.chat = _Chat()

    fake_module = types.SimpleNamespace(OpenRouter=_Client)
    monkeypatch.setitem(sys.modules, "openrouter", fake_module)

    model = OpenRouterSDKModel()
    cfg = ModelConfig(provider="openrouter_sdk", model="openai/gpt-4o-mini", base_url=None)
    out = asyncio.run(model.aplan_step(cfg, "sys", "usr"))
    assert out.startswith('{"summary"')
