from __future__ import annotations

from hexi.core.domain import ModelConfig

from .model_http_common import post_json, require_env


class OpenAICompatModel:
    def plan_step(self, config: ModelConfig, system_prompt: str, user_prompt: str) -> str:
        api_key = require_env("OPENAI_API_KEY")
        base_url = (config.base_url or "https://api.openai.com/v1").rstrip("/")
        url = f"{base_url}/chat/completions"
        payload = {
            "model": config.model,
            "temperature": 0,
            "response_format": {"type": "json_object"},
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        }
        data = post_json(url, {"Authorization": f"Bearer {api_key}"}, payload)
        return data["choices"][0]["message"]["content"]
