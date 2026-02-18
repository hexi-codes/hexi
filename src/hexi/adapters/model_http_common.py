from __future__ import annotations

import os

import httpx


def require_env(name: str) -> str:
    value = os.getenv(name, "").strip()
    if not value:
        raise RuntimeError(f"missing environment variable: {name}")
    return value


def post_json(url: str, headers: dict[str, str], payload: dict) -> dict:
    with httpx.Client(timeout=60.0) as client:
        response = client.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()
