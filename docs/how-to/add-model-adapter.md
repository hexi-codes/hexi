# Add A Model Adapter

To add a new provider:

## 1. Implement model adapter

Create `hexi.adapters.model_<provider>.py` implementing `plan_step(config, system_prompt, user_prompt) -> str`.

## 2. Keep adapter responsibilities narrow

- auth/header handling,
- request formatting,
- response extraction.

Do not add orchestration logic in adapters.

## 3. Register provider in CLI resolver

Update `hexi.cli._pick_model` mapping.

## 4. Add provider config block

Support `[providers.<provider>]` in TOML parsing.

## 5. Add tests

- success parse path
- non-200 / error path
- key missing path
