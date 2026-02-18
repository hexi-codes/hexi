# Troubleshooting Matrix

| Symptom | Likely cause | Fix |
|---|---|---|
| `Error: not a git repository` | command run outside git repo | `cd` into a git repo |
| Doctor reports `API key source: none` | missing env var and local secret | run `hexi onboard` or export key |
| Run fails with parse error | provider returned non-conforming JSON | narrow task prompt, retry |
| Command blocked | not allowlisted or disallowed base command | update policy allowlist carefully |
| No visible file changes | model emitted non-write actions only | tighten task to explicit file modifications |
