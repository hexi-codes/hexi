# FAQ

## Is Hexi a full autonomous agent platform?
No. Hexi v0.1.0 is intentionally single-step and local-first.

## Can I use Hexi without OpenRouter?
Yes. OpenAI-compatible and Anthropic-compatible adapters are included.

## Where should API keys live?
Prefer environment variables. Local TOML secret fallback exists for convenience.

## Is run history persisted?
Yes, in `.hexi/runlog.jsonl`.

## Does Hexi edit files outside the repo?
No. Path traversal checks block writes outside repo root.
