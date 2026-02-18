# Provider Strategy

Hexi supports multiple model-provider styles through a common port.

## Current adapters

- `openrouter_http`: raw HTTP, supports OpenAI-style and Anthropic-style endpoints
- `openrouter_sdk`: official OpenRouter SDK
- `openai_compat`: OpenAI-compatible `/chat/completions`
- `anthropic_compat`: Anthropic-compatible `/messages`

## Why multiple styles matter

- SDK path gives fast stability.
- Raw HTTP path gives low-level control and transparent behavior.
- Port contract keeps orchestration independent of provider quirks.

## Config pattern

Use a selector + provider blocks:

```toml
[model]
provider = "openrouter_http"
model = "openai/gpt-4o-mini"

[providers.openrouter_http]
base_url = "https://openrouter.ai/api/v1"
api_style = "openai"
```
