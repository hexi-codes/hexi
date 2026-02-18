# Getting Started

## Install
```bash
pip install -e .
```

## OpenRouter support (optional)

- HTTP adapter only:
```bash
pip install -e ".[openrouter-http]"
```

- SDK adapter only:
```bash
pip install -e ".[openrouter-sdk]"
```

- Both OpenRouter adapters:
```bash
pip install -e ".[openrouter]"
```

## Initialize a repo
```bash
cd /path/to/git/repo
hexi init
```

## Onboard interactively
```bash
hexi onboard
```

This writes:
- `.hexi/config.toml` (shared defaults)
- `.hexi/local.toml` (local overrides + optional local key)
- `.hexi/runlog.jsonl` (append-only events)

## Run one step
```bash
hexi run "Add a small failing test for parser edge cases"
```

## Inspect output
```bash
hexi diff
tail -n 20 .hexi/runlog.jsonl
```
