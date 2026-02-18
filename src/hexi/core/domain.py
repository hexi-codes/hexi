from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Literal

EventType = Literal["progress", "question", "review", "artifact", "error", "done"]


@dataclass(frozen=True)
class Event:
    type: EventType
    one_line_summary: str
    blocking: bool
    payload: dict[str, Any]


@dataclass(frozen=True)
class Thread:
    id: str
    task: str


@dataclass(frozen=True)
class ModelConfig:
    provider: str
    model: str
    base_url: str | None = None
    api_style: str | None = None


@dataclass(frozen=True)
class Policy:
    allow_commands: list[str]
    max_diff_chars: int = 4000
    max_file_read_chars: int = 4000


@dataclass
class StepResult:
    success: bool
    events: list[Event] = field(default_factory=list)
