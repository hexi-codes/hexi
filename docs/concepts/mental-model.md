# Mental Model

Think of Hexi as a tiny deterministic shell around non-deterministic models.

## Pipeline

1. **Input**: a task string.
2. **Context**: current git status + bounded diff.
3. **Plan**: model returns strict ActionPlan JSON.
4. **Execution**: read/write/run/emit actions under policy.
5. **Review**: final review event with status + diff snippet.
6. **Done**: process exits.

## Why this works

- Model creativity is constrained into a typed action envelope.
- Execution is policy-controlled and local-only.
- Observability is consistent via event schema.

## What Hexi does not do

- no autonomous multi-step loops,
- no daemonized task manager,
- no hidden memory store.

Those are future options, not v0.1.0 defaults.
