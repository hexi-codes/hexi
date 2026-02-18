# Events

Events are Hexi's operational contract.

## Event fields

- `type`: `progress | question | review | artifact | error | done`
- `one_line_summary`: concise human-readable summary
- `blocking`: whether user intervention is needed
- `payload`: structured details

## Why events are central

- Console output is just one view.
- `.hexi/runlog.jsonl` is append-only evidence of behavior.
- External tools can parse events without scraping text.

## Typical sequence

1. `progress`: run start
2. `progress`: action plan parsed
3. `artifact` / `question` / `error`: action outcomes
4. `review`: final local state summary
5. `done`: final status marker

## Event quality guidelines

- Summaries should be specific and short.
- Payload should carry machine-usable keys.
- Errors should include causal messages, not generic failure text.
