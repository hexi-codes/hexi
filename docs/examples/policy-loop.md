# Example: Policy Loop

Path: `examples/policy_loop`

## Pattern

Run multiple single-step invocations with explicit human checkpoints.

## Why use this pattern

- preserves single-step safety contract,
- adds controlled iteration,
- keeps responsibility with the operator.

## Run

```bash
cd examples/policy_loop
python run_loop.py
```
