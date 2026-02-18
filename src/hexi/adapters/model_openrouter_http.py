from __future__ import annotations

import os
from typing import Any

import httpx
try:
    import requests as requests_lib
except Exception:  # pragma: no cover
    requests_lib = None

from hexi.core.domain import ModelConfig


class OpenRouterHTTPModel:
    def __init__(self) -> None:
        api_key = os.getenv("OPENROUTER_API_KEY", "").strip()
        if not api_key:
            raise EnvironmentError("OPENROUTER_API_KEY is required for OpenRouter HTTP adapter")
        self.api_key = api_key

    def plan_step(self, config: ModelConfig, system_prompt: str, user_prompt: str) -> str:
        style = (config.api_style or "openai").strip().lower()
        if style == "anthropic":
            return self._plan_step_anthropic(config, system_prompt, user_prompt)
        return self._plan_step_openai(config, system_prompt, user_prompt)

    async def aplan_step(self, config: ModelConfig, system_prompt: str, user_prompt: str) -> str:
        style = (config.api_style or "openai").strip().lower()
        if style == "anthropic":
            return await self._aplan_step_anthropic(config, system_prompt, user_prompt)
        return await self._aplan_step_openai(config, system_prompt, user_prompt)

    def _base_url(self, config: ModelConfig) -> str:
        return (config.base_url or "https://openrouter.ai/api/v1").rstrip("/")

    def _plan_step_openai(self, config: ModelConfig, system_prompt: str, user_prompt: str) -> str:
        if requests_lib is None:
            raise RuntimeError("requests is required for openrouter_http adapter. Install with: pip install -e '.[openrouter-http]'")
        url = f"{self._base_url(config)}/chat/completions"
        payload = {
            "model": config.model,
            "temperature": 0,
            "response_format": {"type": "json_object"},
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        }
        response = requests_lib.post(
            url,
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            json=payload,
            timeout=60,
        )
        if response.status_code != 200:
            raise RuntimeError(f"OpenRouter OpenAI-style request failed: status={response.status_code}, body={response.text}")
        data: dict[str, Any] = response.json()
        return str(data["choices"][0]["message"]["content"])

    async def _aplan_step_openai(self, config: ModelConfig, system_prompt: str, user_prompt: str) -> str:
        url = f"{self._base_url(config)}/chat/completions"
        payload = {
            "model": config.model,
            "temperature": 0,
            "response_format": {"type": "json_object"},
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        }
        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.post(
                url,
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json",
                },
                json=payload,
            )
        if response.status_code != 200:
            raise RuntimeError(f"OpenRouter OpenAI-style request failed: status={response.status_code}, body={response.text}")
        data: dict[str, Any] = response.json()
        return str(data["choices"][0]["message"]["content"])

    def _plan_step_anthropic(self, config: ModelConfig, system_prompt: str, user_prompt: str) -> str:
        if requests_lib is None:
            raise RuntimeError("requests is required for openrouter_http adapter. Install with: pip install -e '.[openrouter-http]'")
        url = f"{self._base_url(config)}/messages"
        payload = {
            "model": config.model,
            "max_tokens": 2048,
            "system": system_prompt,
            "messages": [{"role": "user", "content": user_prompt}],
        }
        response = requests_lib.post(
            url,
            headers={
                "x-api-key": self.api_key,
                "anthropic-version": "2023-06-01",
                "Content-Type": "application/json",
            },
            json=payload,
            timeout=60,
        )
        if response.status_code != 200:
            raise RuntimeError(f"OpenRouter Anthropic-style request failed: status={response.status_code}, body={response.text}")
        data: dict[str, Any] = response.json()
        return str(data["content"][0]["text"])

    async def _aplan_step_anthropic(self, config: ModelConfig, system_prompt: str, user_prompt: str) -> str:
        url = f"{self._base_url(config)}/messages"
        payload = {
            "model": config.model,
            "max_tokens": 2048,
            "system": system_prompt,
            "messages": [{"role": "user", "content": user_prompt}],
        }
        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.post(
                url,
                headers={
                    "x-api-key": self.api_key,
                    "anthropic-version": "2023-06-01",
                    "Content-Type": "application/json",
                },
                json=payload,
            )
        if response.status_code != 200:
            raise RuntimeError(f"OpenRouter Anthropic-style request failed: status={response.status_code}, body={response.text}")
        data: dict[str, Any] = response.json()
        return str(data["content"][0]["text"])
