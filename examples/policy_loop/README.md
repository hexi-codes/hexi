# policy_loop

Iterative wrapper that runs Hexi in multiple explicit steps with human checkpoints.

This is not a daemon; each iteration is a separate `hexi run` invocation.

## Setup
```bash
pip install -e ../..
```

## Run
```bash
python run_loop.py
```

Edit `TASKS` in `run_loop.py` to adjust behavior.
