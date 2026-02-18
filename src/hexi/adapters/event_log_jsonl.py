from __future__ import annotations

import json
from pathlib import Path

from hexi.core.domain import Event
from hexi.core.schemas import event_to_dict


class JsonlRunlogEventSink:
    def __init__(self, runlog_path: Path) -> None:
        self.runlog_path = runlog_path

    def emit(self, event: Event) -> None:
        self.runlog_path.parent.mkdir(parents=True, exist_ok=True)
        with self.runlog_path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(event_to_dict(event), ensure_ascii=True) + "\n")
