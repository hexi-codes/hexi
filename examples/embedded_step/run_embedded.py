from __future__ import annotations

import sys
from pathlib import Path

from hexi.adapters.events_console import ConsoleEventSink
from hexi.adapters.exec_local import LocalExec
from hexi.adapters.memory_file import FileMemory
from hexi.adapters.model_openrouter_http import OpenRouterHTTPModel
from hexi.adapters.workspace_local_git import LocalGitWorkspace
from hexi.core.service import RunStepService


def main() -> int:
    task = " ".join(sys.argv[1:]).strip() or "Create a tiny test improvement"
    ws = LocalGitWorkspace(Path.cwd())
    mem = FileMemory(ws.repo_root())
    mem.ensure_initialized()
    mem.apply_api_key_to_env(mem.load_model_config().provider)

    service = RunStepService(
        model=OpenRouterHTTPModel(),
        workspace=ws,
        executor=LocalExec(),
        events=ConsoleEventSink(),
        memory=mem,
    )
    result = service.run_once(task)
    return 0 if result.success else 1


if __name__ == "__main__":
    raise SystemExit(main())
