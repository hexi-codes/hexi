from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Literal

from .domain import Event

ActionKind = Literal["read", "write", "run", "emit"]


class ActionPlanError(ValueError):
    pass


@dataclass(frozen=True)
class Action:
    kind: ActionKind
    path: str | None = None
    content: str | None = None
    command: str | None = None
    event_type: str | None = None
    message: str | None = None
    blocking: bool | None = None
    payload: dict[str, Any] | None = None


@dataclass(frozen=True)
class ActionPlan:
    summary: str
    actions: list[Action]


def event_to_dict(event: Event) -> dict[str, Any]:
    return {
        "type": event.type,
        "one_line_summary": event.one_line_summary,
        "blocking": event.blocking,
        "payload": event.payload,
    }


def parse_action_plan(raw: str) -> ActionPlan:
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ActionPlanError(f"invalid JSON: {exc}") from exc

    if not isinstance(data, dict):
        raise ActionPlanError("top-level must be an object")

    allowed_top = {"summary", "actions"}
    extra_top = set(data.keys()) - allowed_top
    if extra_top:
        raise ActionPlanError(f"unexpected top-level keys: {sorted(extra_top)}")

    summary = data.get("summary")
    if not isinstance(summary, str) or not summary.strip() or len(summary) > 400:
        raise ActionPlanError("summary must be non-empty string up to 400 chars")

    actions_raw = data.get("actions")
    if not isinstance(actions_raw, list) or not (1 <= len(actions_raw) <= 20):
        raise ActionPlanError("actions must be an array with 1..20 items")

    actions: list[Action] = []
    allowed_action_keys = {
        "kind",
        "path",
        "content",
        "command",
        "event_type",
        "message",
        "blocking",
        "payload",
    }
    valid_event_types = {"progress", "question", "review", "artifact", "error", "done"}

    for idx, item in enumerate(actions_raw):
        if not isinstance(item, dict):
            raise ActionPlanError(f"actions[{idx}] must be object")
        extra = set(item.keys()) - allowed_action_keys
        if extra:
            raise ActionPlanError(f"actions[{idx}] unexpected keys: {sorted(extra)}")
        kind = item.get("kind")
        if kind not in {"read", "write", "run", "emit"}:
            raise ActionPlanError(f"actions[{idx}] invalid kind")

        action = Action(
            kind=kind,
            path=item.get("path"),
            content=item.get("content"),
            command=item.get("command"),
            event_type=item.get("event_type"),
            message=item.get("message"),
            blocking=item.get("blocking"),
            payload=item.get("payload"),
        )

        if kind == "read":
            if not isinstance(action.path, str) or not action.path:
                raise ActionPlanError(f"actions[{idx}] read requires path")
        elif kind == "write":
            if not isinstance(action.path, str) or not action.path:
                raise ActionPlanError(f"actions[{idx}] write requires path")
            if not isinstance(action.content, str):
                raise ActionPlanError(f"actions[{idx}] write requires content")
        elif kind == "run":
            if not isinstance(action.command, str) or not action.command.strip():
                raise ActionPlanError(f"actions[{idx}] run requires command")
        elif kind == "emit":
            if action.event_type not in valid_event_types:
                raise ActionPlanError(f"actions[{idx}] emit requires valid event_type")
            if not isinstance(action.message, str) or not action.message.strip():
                raise ActionPlanError(f"actions[{idx}] emit requires message")
            if not isinstance(action.blocking, bool):
                raise ActionPlanError(f"actions[{idx}] emit requires blocking boolean")
            if action.payload is not None and not isinstance(action.payload, dict):
                raise ActionPlanError(f"actions[{idx}] emit payload must be object")

        actions.append(action)

    return ActionPlan(summary=summary.strip(), actions=actions)
