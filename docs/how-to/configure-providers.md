# Configure Providers

Hexi supports multiple providers via `[model]` + `[providers.*]` blocks.

## OpenRouter package install options

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

## OpenRouter HTTP

```toml
[model]
provider = "openrouter_http"
model = "openai/gpt-4o-mini"

[providers.openrouter_http]
base_url = "https://openrouter.ai/api/v1"
api_style = "openai"
```

## OpenRouter SDK

```toml
[model]
provider = "openrouter_sdk"
model = "openai/gpt-4o-mini"
```

## OpenAI-compatible

```toml
[model]
provider = "openai_compat"
model = "gpt-4o-mini"

[providers.openai_compat]
base_url = "https://api.openai.com/v1"
```

## Anthropic-compatible

```toml
[model]
provider = "anthropic_compat"
model = "claude-3-5-sonnet-latest"

[providers.anthropic_compat]
base_url = "https://api.anthropic.com"
```
