# Golden Path Demo

```bash
cd /path/to/your/repo
hexi init
hexi doctor
hexi run "Add a small unit test for X and run pytest"
hexi diff
tail -n 20 .hexi/runlog.jsonl
```

Expected flow:
1. `.hexi/config.toml` is created.
2. `hexi run` emits `progress` events and finishes with `review` + `done`.
3. File edits appear in `git diff`.
4. Run log entries are appended to `.hexi/runlog.jsonl`.
