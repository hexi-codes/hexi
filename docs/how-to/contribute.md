# Contribute Changes

## Local setup

```bash
pip install -e ".[dev]"
```

## Run tests

```bash
PYTHONPATH=src pytest -q
```

## Change guidelines

- Keep boundaries clean: orchestration in core, side effects in adapters.
- Prefer small PRs with clear behavior changes.
- Update docs with any contract or config change.

## Suggested PR structure

1. problem statement
2. contract impact
3. implementation notes
4. test evidence
