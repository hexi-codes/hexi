# Hexi Documentation

Hexi is a compact, contract-driven coding-agent runtime for local repositories.

This documentation is organized as a practical handbook:

- **Concepts** explain the execution model and design boundaries.
- **Tutorials** walk you through concrete usage end-to-end.
- **How-to guides** solve focused operational tasks.
- **Reference** documents exact behavior, schemas, and interfaces.
- **Internals** explain implementation tradeoffs in v0.1.0.

## Who this is for

- Engineers who want an auditable local agent runtime.
- Teams that need policy controls before adding automation scale.
- Maintainers who prefer simple contracts and swappable adapters.

## Core promise

One invocation, one step, clean event trail.

```bash
hexi run "Add one focused test for parser edge case"
```

Hexi will:
1. Load config and policy from `.hexi/`.
2. Ask a model for one machine-readable action plan.
3. Execute allowed actions only.
4. Emit structured events to console + `.hexi/runlog.jsonl`.
5. Exit.

Continue with [Vision](preface/vision.md) or jump to [Quickstart](tutorials/quickstart.md).
