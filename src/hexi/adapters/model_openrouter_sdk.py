from __future__ import annotations

import os
from typing import Any

from hexi.core.domain import ModelConfig


class OpenRouterSDKModel:
    def __init__(self) -> None:
        api_key = os.getenv("OPENROUTER_API_KEY", "").strip()
        if not api_key:
            raise EnvironmentError("OPENROUTER_API_KEY is required for OpenRouter SDK adapter")

        try:
            from openrouter import OpenRouter  # type: ignore
        except Exception as exc:  # pragma: no cover
            raise RuntimeError("openrouter package is required for OpenRouterSDKModel") from exc

        self._client = OpenRouter(api_key=api_key)

    def plan_step(self, config: ModelConfig, system_prompt: str, user_prompt: str) -> str:
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]
        response = self._client.chat.send(messages=messages, model=config.model)
        return str(response.choices[0].message.content)

    async def aplan_step(self, config: ModelConfig, system_prompt: str, user_prompt: str) -> str:
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]
        response = await self._client.chat.send_async(messages=messages, model=config.model)
        return str(response.choices[0].message.content)
