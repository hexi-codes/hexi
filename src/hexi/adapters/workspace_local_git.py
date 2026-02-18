from __future__ import annotations

import subprocess
from pathlib import Path


class PathSafetyError(ValueError):
    pass


def resolve_repo_path(repo_root: Path, requested: str) -> Path:
    if not requested:
        raise PathSafetyError("empty path")
    candidate = (repo_root / requested).resolve()
    root = repo_root.resolve()
    if candidate != root and root not in candidate.parents:
        raise PathSafetyError(f"path escapes repo root: {requested}")
    return candidate


class LocalGitWorkspace:
    def __init__(self, cwd: Path) -> None:
        self._cwd = cwd
        self._repo_root = self._discover_repo_root(cwd)

    @staticmethod
    def _discover_repo_root(cwd: Path) -> Path:
        proc = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            cwd=cwd,
            capture_output=True,
            text=True,
            check=False,
        )
        if proc.returncode != 0:
            raise RuntimeError("not a git repository")
        return Path(proc.stdout.strip()).resolve()

    def repo_root(self) -> Path:
        return self._repo_root

    def read_text(self, path: str, max_chars: int) -> str:
        p = resolve_repo_path(self._repo_root, path)
        if not p.exists():
            raise FileNotFoundError(path)
        content = p.read_text(encoding="utf-8")
        return content[:max_chars]

    def write_text(self, path: str, content: str) -> None:
        p = resolve_repo_path(self._repo_root, path)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")

    def git_status(self) -> str:
        proc = subprocess.run(
            ["git", "status", "--short"],
            cwd=self._repo_root,
            capture_output=True,
            text=True,
            check=False,
        )
        return proc.stdout.strip()

    def git_diff(self, max_chars: int) -> str:
        proc = subprocess.run(
            ["git", "diff", "--"],
            cwd=self._repo_root,
            capture_output=True,
            text=True,
            check=False,
        )
        return proc.stdout[:max_chars]
