from __future__ import annotations

from .domain import Policy

DISALLOWED_BASE_COMMANDS = {
    "rm",
    "mv",
    "dd",
    "mkfs",
    "shutdown",
    "reboot",
    "poweroff",
    "curl",
    "wget",
    "nc",
    "telnet",
    "ssh",
    "scp",
    "rsync",
}


def command_allowed(command: str, policy: Policy) -> bool:
    normalized = " ".join(command.strip().split())
    if not normalized:
        return False
    base = normalized.split(" ", 1)[0].lower()
    if base in DISALLOWED_BASE_COMMANDS:
        return False
    return any(normalized == allowed or normalized.startswith(f"{allowed} ") for allowed in policy.allow_commands)
