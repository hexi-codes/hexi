# Configuration

Hexi uses layered TOML + env var precedence.

## Precedence order
1. Environment variables
2. `.hexi/local.toml`
3. `.hexi/config.toml`
4. Internal defaults

## Multi-provider structure
```toml
[model]
provider = "openai_compat"
model = "gpt-4o-mini"

[providers.openrouter_http]
base_url = "https://openrouter.ai/api/v1"
api_style = "openai"

[providers.openrouter_sdk]
base_url = "https://openrouter.ai/api/v1"

[providers.openai_compat]
base_url = "https://api.openai.com/v1"

[providers.anthropic_compat]
base_url = "https://api.anthropic.com"
```

## Secrets
Recommended: env vars.

- `OPENROUTER_API_KEY`
- `OPENAI_API_KEY`
- `ANTHROPIC_API_KEY`

For local-only workflows, `hexi onboard` can write key values into `.hexi/local.toml` under `[secrets]`.
