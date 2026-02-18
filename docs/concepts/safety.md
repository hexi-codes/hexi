# Safety Model

Hexi applies safety at three layers.

## 1) Path safety

Workspace writes are resolved against repo root. Path traversal is rejected.

## 2) Command safety

Only allowlisted commands run. Certain destructive/network command bases are blocked.

## 3) Scope safety

Single-step execution naturally limits blast radius.

## Safe-by-default behavior

- bounded diff and file reads,
- no background jobs,
- explicit provider key checks,
- complete runlog trail.

## What to harden first in production usage

- tighten allowlist by repo,
- lower diff/read caps if needed,
- enforce branch protections around generated edits,
- add CI checks on runlog anomalies.
