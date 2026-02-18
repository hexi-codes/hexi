# Embedded Python Usage

Hexi can be used as a library from your own Python app.

## Minimal embedded flow

```python
from pathlib import Path
from hexi.adapters.workspace_local_git import LocalGitWorkspace
from hexi.adapters.memory_file import FileMemory
from hexi.adapters.exec_local import LocalExec
from hexi.adapters.events_console import ConsoleEventSink
from hexi.adapters.model_openrouter_http import OpenRouterHTTPModel
from hexi.core.service import RunStepService

ws = LocalGitWorkspace(Path.cwd())
mem = FileMemory(ws.repo_root())
mem.ensure_initialized()
mem.apply_api_key_to_env(mem.load_model_config().provider)

svc = RunStepService(
    model=OpenRouterHTTPModel(),
    workspace=ws,
    executor=LocalExec(),
    events=ConsoleEventSink(),
    memory=mem,
)

result = svc.run_once("Add one focused test")
print(result.success)
```

## When to embed

- You want custom orchestration around one-step calls.
- You need tighter integration with existing Python tooling.
