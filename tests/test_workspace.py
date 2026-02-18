from pathlib import Path

import pytest

from hexi.adapters.workspace_local_git import PathSafetyError, resolve_repo_path


def test_resolve_repo_path_inside_root(tmp_path: Path) -> None:
    out = resolve_repo_path(tmp_path, "src/main.py")
    assert str(out).startswith(str(tmp_path))


def test_resolve_repo_path_rejects_traversal(tmp_path: Path) -> None:
    with pytest.raises(PathSafetyError):
        resolve_repo_path(tmp_path, "../../etc/passwd")
