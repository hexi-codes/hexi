# First Real Run

This tutorial shows a realistic first run with decision points.

## Scenario

You want Hexi to add a small test and run pytest.

## Step-by-step

1. Create a branch.
```bash
git checkout -b codex/hexi-first-run
```

2. Run onboarding if needed.
```bash
hexi onboard
```

3. Execute a concrete task.
```bash
hexi run "Add one test for empty-input handling in parser and run pytest"
```

4. Review output.
```bash
hexi diff
```

5. Inspect event log.
```bash
tail -n 100 .hexi/runlog.jsonl
```

6. Decide next step.
- If done: keep changes.
- If partial: run a follow-up single step with a narrower task.

## Good task phrasing

- "Add one test for X and run pytest path/to/test_file.py"
- "Refactor only function Y in file Z; do not touch imports"

## Poor task phrasing

- "Improve everything"
- "Refactor the whole repo"
