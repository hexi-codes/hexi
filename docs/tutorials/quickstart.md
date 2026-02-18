# Quickstart

This is the fastest path to a successful run.

## 1. Install

```bash
pip install -e .
```

Optional:

```bash
pip install -e ".[openrouter-sdk]"
```

If you want the OpenRouter HTTP adapter:

```bash
pip install -e ".[openrouter-http]"
```

## 2. Enter a git repo

```bash
cd /path/to/repo
git status
```

## 3. Initialize Hexi

```bash
hexi init
```

## 4. Onboard

```bash
hexi onboard
```

Choose provider/model. Paste key if you want local key storage.

## 5. Verify

```bash
hexi doctor
```

## 6. Run one step

```bash
hexi run "Add one focused unit test for a parser edge case"
```

## 7. Inspect artifacts

```bash
hexi diff
tail -n 50 .hexi/runlog.jsonl
```
