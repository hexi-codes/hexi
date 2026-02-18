# Python API Reference

## Core domain

`hexi.core.domain`:

- `Event`
- `Thread`
- `ModelConfig`
- `Policy`
- `StepResult`

## Core ports

`hexi.core.ports`:

- `ModelPort`
- `WorkspacePort`
- `ExecPort`
- `EventSinkPort`
- `MemoryPort`

## Core service

`hexi.core.service.RunStepService`

Primary method:

```python
run_once(task: str) -> StepResult
```

## Key adapters

- `hexi.adapters.memory_file.FileMemory`
- `hexi.adapters.workspace_local_git.LocalGitWorkspace`
- `hexi.adapters.exec_local.LocalExec`
- `hexi.adapters.events_console.ConsoleEventSink`
- `hexi.adapters.model_openrouter_http.OpenRouterHTTPModel`
- `hexi.adapters.model_openrouter_sdk.OpenRouterSDKModel`
