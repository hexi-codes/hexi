# Configuration Reference

## Files

- `.hexi/config.toml`: shared defaults
- `.hexi/local.toml`: local overrides and optional secrets
- `.hexi/runlog.jsonl`: append-only events

## Model section

```toml
[model]
provider = "openai_compat"
model = "gpt-4o-mini"
```

Fields:
- `provider`: selected adapter key
- `model`: provider-specific model id

## Provider blocks

```toml
[providers.openrouter_http]
base_url = "https://openrouter.ai/api/v1"
api_style = "openai"
```

Fields vary by provider.

## Policy section

```toml
[policy]
allow_commands = ["git status", "git diff", "pytest"]
max_diff_chars = 4000
max_file_read_chars = 4000
```

## Secrets

Use env vars first. Optional local fallback in `.hexi/local.toml`:

```toml
[secrets]
openrouter_api_key = "..."
openai_api_key = "..."
anthropic_api_key = "..."
```
