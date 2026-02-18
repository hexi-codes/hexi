# Write Safe Policies

Policy is the main control surface for command execution.

## Start restrictive

Example:

```toml
[policy]
allow_commands = [
  "git status",
  "git diff",
  "pytest tests/test_parser.py",
]
max_diff_chars = 3000
max_file_read_chars = 3000
```

## Policy tuning checklist

- Remove generic commands if possible.
- Prefer exact commands over broad prefixes.
- Keep output bounds reasonable.

## Review loop

1. Run tasks with strict policy.
2. Observe blocked commands in events.
3. Add only the minimum required allowlist entries.
