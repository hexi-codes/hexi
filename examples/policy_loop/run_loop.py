from __future__ import annotations

import subprocess

TASKS = [
    "Inspect repo and propose one safe test improvement",
    "Apply the smallest code change required",
    "Run allowlisted tests and report failures",
]


def run_step(task: str) -> int:
    print(f"\\n=== Hexi step: {task} ===")
    return subprocess.run(["hexi", "run", task], check=False).returncode


def main() -> int:
    for idx, task in enumerate(TASKS, start=1):
        rc = run_step(task)
        if rc != 0:
            print(f"Step {idx} failed with exit code {rc}. Stopping.")
            return rc
        proceed = input("Continue to next step? [y/N]: ").strip().lower()
        if proceed != "y":
            print("Stopped by user.")
            return 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
