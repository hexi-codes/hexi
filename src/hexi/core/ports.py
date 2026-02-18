from __future__ import annotations

from pathlib import Path
from typing import Protocol

from .domain import Event, ModelConfig, Policy


class ModelPort(Protocol):
    def plan_step(self, config: ModelConfig, system_prompt: str, user_prompt: str) -> str:
        """Return raw model output text that should contain ActionPlan JSON."""


class WorkspacePort(Protocol):
    def repo_root(self) -> Path:
        ...

    def read_text(self, path: str, max_chars: int) -> str:
        ...

    def write_text(self, path: str, content: str) -> None:
        ...

    def git_status(self) -> str:
        ...

    def git_diff(self, max_chars: int) -> str:
        ...


class ExecPort(Protocol):
    def run(self, command: str, policy: Policy) -> tuple[int, str, str]:
        ...


class EventSinkPort(Protocol):
    def emit(self, event: Event) -> None:
        ...


class MemoryPort(Protocol):
    def ensure_initialized(self) -> None:
        ...

    def load_model_config(self) -> ModelConfig:
        ...

    def load_policy(self) -> Policy:
        ...

    def append_runlog(self, event: Event) -> None:
        ...
