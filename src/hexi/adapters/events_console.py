from __future__ import annotations

import json

from rich.console import Console, Group
from rich.panel import Panel
from rich.syntax import Syntax
from rich.text import Text

from hexi.core.domain import Event

_EVENT_STYLES: dict[str, tuple[str, str]] = {
    "progress": ("cyan", "⏳"),
    "question": ("yellow", "❓"),
    "review": ("magenta", "🔎"),
    "artifact": ("green", "📦"),
    "error": ("red", "✖"),
    "done": ("bright_blue", "✔"),
}


class ConsoleEventSink:
    def __init__(self) -> None:
        self.console = Console()

    def emit(self, event: Event) -> None:
        color, icon = _EVENT_STYLES.get(event.type, ("white", "•"))
        title = Text(f"{icon} {event.type.upper()}", style=f"bold {color}")
        subtitle = "blocking" if event.blocking else "non-blocking"

        lines = [Text(event.one_line_summary, style="bold")]
        if event.payload:
            payload_str = json.dumps(event.payload, ensure_ascii=True, indent=2)
            lines.append(Text(""))
            lines.append(Syntax(payload_str, "json", word_wrap=True))

        self.console.print(Panel.fit(Group(*lines), title=title, subtitle=subtitle, border_style=color))
