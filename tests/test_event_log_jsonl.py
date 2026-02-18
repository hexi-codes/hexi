from __future__ import annotations

import json
from pathlib import Path

from hexi.adapters.event_log_jsonl import JsonlRunlogEventSink
from hexi.core.domain import Event


def test_jsonl_event_sink_appends_line(tmp_path: Path) -> None:
    path = tmp_path / ".hexi/runlog.jsonl"
    sink = JsonlRunlogEventSink(path)

    sink.emit(Event(type="progress", one_line_summary="line1", blocking=False, payload={"a": 1}))
    sink.emit(Event(type="done", one_line_summary="line2", blocking=False, payload={"b": 2}))

    lines = path.read_text(encoding="utf-8").splitlines()
    assert len(lines) == 2
    assert json.loads(lines[0])["one_line_summary"] == "line1"
    assert json.loads(lines[1])["type"] == "done"
