from __future__ import annotations

import subprocess
from pathlib import Path

import pytest

from hexi.adapters.workspace_local_git import LocalGitWorkspace


def _init_repo(path: Path) -> None:
    subprocess.run(["git", "init", "-q"], cwd=path, check=True)
    subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=path, check=True)
    subprocess.run(["git", "config", "user.name", "Test"], cwd=path, check=True)
    (path / "README.md").write_text("hello\n", encoding="utf-8")
    subprocess.run(["git", "add", "README.md"], cwd=path, check=True)
    subprocess.run(["git", "commit", "-m", "init", "-q"], cwd=path, check=True)


def test_workspace_detects_repo_and_reads_writes(tmp_path: Path) -> None:
    _init_repo(tmp_path)
    ws = LocalGitWorkspace(tmp_path)

    ws.write_text("src/x.txt", "abc")
    assert ws.read_text("src/x.txt", max_chars=10) == "abc"


def test_workspace_git_status_and_diff(tmp_path: Path) -> None:
    _init_repo(tmp_path)
    ws = LocalGitWorkspace(tmp_path)

    ws.write_text("README.md", "hello\nchanged\n")
    status = ws.git_status()
    diff = ws.git_diff(max_chars=10000)

    assert "README.md" in status
    assert "changed" in diff


def test_workspace_requires_git_repo(tmp_path: Path) -> None:
    with pytest.raises(RuntimeError):
        LocalGitWorkspace(tmp_path)
