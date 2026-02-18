from __future__ import annotations

import shlex
import subprocess

from hexi.core.domain import Policy
from hexi.core.policy import command_allowed


class LocalExec:
    def run(self, command: str, policy: Policy) -> tuple[int, str, str]:
        if not command_allowed(command, policy):
            raise PermissionError(f"command is not allowlisted: {command}")
        args = shlex.split(command)
        proc = subprocess.run(args, capture_output=True, text=True, check=False)
        return proc.returncode, proc.stdout[-8000:], proc.stderr[-8000:]
