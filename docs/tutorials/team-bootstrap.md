# Team Bootstrap

Use this process to roll Hexi out to a small engineering team.

## Repo setup

1. Add Hexi as a dev dependency in your standard environment.
2. Add `.hexi/local.toml` and `.hexi/runlog.jsonl` to `.gitignore`.
3. Commit `.hexi/config.toml` baseline policy for the repo.

## Suggested baseline policy

- allow only `git status`, `git diff`, repo-specific test commands.
- avoid broad shell permissions early.

## Team workflow

1. Engineer runs `hexi onboard` locally.
2. Engineer executes narrow tasks using `hexi run`.
3. Engineer reviews diff + runlog before commit.

## Governance tips

- Keep run scope small.
- Review event logs in PR discussion when needed.
- Rotate API keys regularly.
