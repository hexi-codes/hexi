# Template Catalog

Hexi ships five native templates designed for immediate real use.

All templates include built-in Hexi integration from day one.

## 1) `hexi-python-lib`

Use for package/library work.

Includes:

- `src/` package + unit tests
- `.hexi/` defaults
- Make targets for `test`, `hexi-doctor`, `hexi-run`

## 2) `hexi-fastapi-service`

Use for API service starts.

Includes:

- FastAPI app with `/health`
- API tests
- `.hexi/` defaults + runner targets

## 3) `hexi-typer-cli`

Use for developer CLI tooling.

Includes:

- Typer command app
- CLI tests
- `.hexi/` defaults + helper targets

## 4) `hexi-data-job`

Use for ETL/report style scripts.

Includes:

- dry-run command
- data input/output folders
- test harness
- `.hexi/` defaults

## 5) `hexi-agent-worker`

Use for embedding Hexi runtime directly.

Includes:

- `RunStepService` embedded entrypoint
- adapter wiring example
- `.hexi/` defaults and helper targets

## Bootstrap pattern

```bash
cp -R templates/hexi-python-lib /tmp/my-new-project
cd /tmp/my-new-project
git init
hexi doctor
```
