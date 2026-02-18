# Architecture Reference

Hexi uses a hexagonal split:

## `hexi.core`

- domain models
- port protocols
- action-plan validation
- orchestration service

## `hexi.adapters`

- model providers
- workspace + git operations
- command execution
- file-based memory
- event sinks

## Execution boundary

The core never calls external systems directly; all side effects flow through ports.

## Why this matters

- adapter swaps are cheap,
- tests can use fakes for every dependency,
- core behavior remains stable as provider APIs change.
