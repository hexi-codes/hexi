from hexi.core.domain import Policy
from hexi.core.policy import command_allowed


def test_policy_allows_prefix_match() -> None:
    policy = Policy(allow_commands=["pytest", "git status"])
    assert command_allowed("pytest -q", policy)


def test_policy_rejects_non_allowlisted_command() -> None:
    policy = Policy(allow_commands=["pytest"])
    assert not command_allowed("git status", policy)


def test_policy_rejects_disallowed_base_command_even_if_allowlisted() -> None:
    policy = Policy(allow_commands=["curl"])
    assert not command_allowed("curl https://example.com", policy)
