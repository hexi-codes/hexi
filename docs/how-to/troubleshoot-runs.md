# Troubleshoot Failing Runs

Use this flow when a run fails.

## 1) Check doctor

```bash
hexi doctor
```

If key source is `none`, fix credentials first.

## 2) Check runlog

```bash
tail -n 100 .hexi/runlog.jsonl
```

Look for:
- parse errors,
- disallowed commands,
- file/path errors.

## 3) Narrow task scope

Broad tasks increase plan ambiguity. Use precise, local instructions.

## 4) Verify policy

If command execution failed, compare command to allowlist entries.

## 5) Retry with bounded goal

Example:

```bash
hexi run "Only update tests/test_parser.py; do not modify source files"
```
