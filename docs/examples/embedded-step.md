# Example: Embedded Step

Path: `examples/embedded_step`

## Pattern

Instantiate adapters + `RunStepService` directly in Python.

## Why use this pattern

- richer control over service lifecycle,
- direct inspection of `StepResult`,
- easier custom event handling.

## Run

```bash
cd examples/embedded_step
python run_embedded.py "Add one tiny test"
```
