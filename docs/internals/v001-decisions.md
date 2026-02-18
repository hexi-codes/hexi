# v0.1.0 Scope Decisions

These decisions are intentional, not omissions.

## Included

- single-step runtime
- local git workspace operations
- strict action plan contract
- structured event logging
- multi-provider model adapters

## Excluded

- background workers
- multi-step autonomous loops
- database persistence
- plugin/registry systems

## Why this was chosen

- ship fast,
- keep architecture coherent,
- preserve refactor freedom.

The next versions can add capabilities without changing core contracts.
