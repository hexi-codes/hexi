# Storage Layering

Hexi uses three repo-scoped files under `.hexi/`.

## `config.toml`

Shared, commit-friendly defaults.

## `local.toml`

Machine-local overrides and optional local secrets.

## `runlog.jsonl`

Append-only event stream for every run.

## Merge behavior

Hexi deep-merges `local.toml` over `config.toml`.

## Key resolution

For provider credentials:
1. environment variable
2. local secrets block
3. missing

Doctor reports resolved key source.
