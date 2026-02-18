from __future__ import annotations

import subprocess

import pytest

from hexi.adapters.exec_local import LocalExec
from hexi.core.domain import Policy


def test_exec_rejects_non_allowlisted_command() -> None:
    policy = Policy(allow_commands=["pytest"])
    with pytest.raises(PermissionError):
        LocalExec().run("git status", policy)


def test_exec_runs_allowlisted_command(monkeypatch: pytest.MonkeyPatch) -> None:
    policy = Policy(allow_commands=["python"])

    def fake_run(args, capture_output, text, check):
        assert args == ["python", "-V"]
        return subprocess.CompletedProcess(args=args, returncode=0, stdout="out", stderr="")

    monkeypatch.setattr("subprocess.run", fake_run)

    rc, out, err = LocalExec().run("python -V", policy)
    assert rc == 0
    assert out == "out"
    assert err == ""


def test_exec_truncates_large_output(monkeypatch: pytest.MonkeyPatch) -> None:
    policy = Policy(allow_commands=["python"])

    def fake_run(args, capture_output, text, check):
        return subprocess.CompletedProcess(args=args, returncode=0, stdout=("a" * 9001), stderr=("b" * 9001))

    monkeypatch.setattr("subprocess.run", fake_run)

    rc, out, err = LocalExec().run("python -V", policy)
    assert rc == 0
    assert len(out) == 8000
    assert len(err) == 8000
