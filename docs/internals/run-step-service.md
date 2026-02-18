# RunStepService Walkthrough

`RunStepService` is the orchestration center of Hexi.

## Responsibilities

1. initialize memory state
2. load model config and policy
3. emit start event
4. gather git status + diff context
5. request and parse action plan
6. execute actions with safety checks
7. emit final review + done events

## Failure handling

- model parse failures produce `error` and terminal `done`.
- action failures produce `error`, then review + terminal `done`.

## Intentional limitations

- no retries,
- no background loops,
- no concurrency.

This keeps behavior auditable for v0.1.0.
