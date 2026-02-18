from __future__ import annotations

import subprocess
import sys


def main() -> int:
    task = " ".join(sys.argv[1:]).strip() or "Refine TODO comments in this repository"
    cmd = ["hexi", "run", task]
    return subprocess.run(cmd, check=False).returncode


if __name__ == "__main__":
    raise SystemExit(main())
