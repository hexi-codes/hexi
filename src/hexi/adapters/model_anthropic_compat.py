from __future__ import annotations

from hexi.core.domain import ModelConfig

from .model_http_common import post_json, require_env


class AnthropicCompatModel:
    def plan_step(self, config: ModelConfig, system_prompt: str, user_prompt: str) -> str:
        api_key = require_env("ANTHROPIC_API_KEY")
        base_url = (config.base_url or "https://api.anthropic.com").rstrip("/")
        url = f"{base_url}/v1/messages"
        payload = {
            "model": config.model,
            "max_tokens": 2048,
            "temperature": 0,
            "system": system_prompt,
            "messages": [{"role": "user", "content": user_prompt}],
        }
        data = post_json(
            url,
            {
                "x-api-key": api_key,
                "anthropic-version": "2023-06-01",
            },
            payload,
        )
        content = data.get("content", [])
        if not content:
            raise RuntimeError("anthropic response missing content")
        first = content[0]
        text = first.get("text") if isinstance(first, dict) else None
        if not text:
            raise RuntimeError("anthropic response missing text")
        return text
