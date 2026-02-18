# Template Walkthrough

This page shows how to pick and bootstrap a template quickly.

## Choose by goal

- Library work: `hexi-python-lib`
- API service: `hexi-fastapi-service`
- CLI tool: `hexi-typer-cli`
- Data automation: `hexi-data-job`
- Embedded agent runtime: `hexi-agent-worker`

## Fast bootstrap commands

```bash
cp -R templates/hexi-typer-cli ./my-cli
cd my-cli
git init
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
make hexi-doctor
make test
```

## Run first agent step

```bash
make hexi-run TASK="Add one small improvement and matching tests"
```
