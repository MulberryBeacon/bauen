# -*- coding: utf-8 -*-

"""
Repository management operations.

Author: Eduardo Ferreira
"""

from pathlib import Path

from git import Repo


def clone_repo(directory: str, repo_ssh: str) -> str:
    """
    Clones a repository.

    :param directory:
        The directory into which the repository will be cloned
    :param repo_ssh:
        The SSH repository address
    :return:
        True if the repository was cloned successfully; False otherwise
    """
    path = str(Path(directory, Path(repo_ssh).stem).resolve())
    repo = Repo.clone_from(repo_ssh, path)
    if repo and repo.working_tree_dir == path:
        return repo.working_tree_dir

    return None
