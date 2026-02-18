# Event Schema

Canonical JSON schema is stored at:
- `docs/contracts/event.schema.json`

## Required fields

- `type`
- `one_line_summary`
- `blocking`
- `payload`

## Event types

- `progress`
- `question`
- `review`
- `artifact`
- `error`
- `done`

## Example

```json
{
  "type": "review",
  "one_line_summary": "Step review",
  "blocking": false,
  "payload": {
    "git_status": " M src/parser.py",
    "git_diff": "diff --git ...",
    "suggestion": "Run tests next"
  }
}
```
