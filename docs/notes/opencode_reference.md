# OpenCode Early-History Recon Notes

Reference repo inspected: `/Users/gnrfan/code/floss/opencode`
Commits reviewed (early evolution):

- `4b0ea68d7` (`initial`)
- `7844cacb2` (`add help`)
- `e7258e38a` (`initial agent setup`)
- `005b8ac16` (`initial working agent`)
- `904061c24` (`additional tools`) at a high level for guardrail trend

## What we learned
- Very early UX prioritized a simple command entrypoint with help first, then progressively added richer behavior.
- Early agent wiring used one primary request path that assembled system prompt + history + user input.
- Tooling quickly added shell execution controls and explicit command restrictions.
- Status/diff style feedback to users appeared early and improved incrementally.

## What Hexi v0.1.0 will mimic (behaviorally)
- Minimal CLI ergonomics (`init`, `run`, diagnostics-oriented commands).
- Strongly bounded one-step execution path.
- Guardrails around command execution (allowlist + bans).
- Compact operational telemetry via structured events.

## What Hexi v0.1.0 will explicitly not copy
- No direct source reuse, structure cloning, or prompt text reuse.
- No long-lived TUI loop or background subscriptions.
- No database-first persistence; we use `.hexi/` files.
- No complex agent orchestration in v0.1.0; one invocation equals one step.

## Why this is enough for v0.1.0
- Claims package space quickly while preserving clean boundaries.
- Keeps core contracts stable so internals can be refactored later without breaking adapters or CLI.
