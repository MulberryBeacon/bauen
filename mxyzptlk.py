# -*- coding: utf-8 -*-

"""
Script to automatically configure a workspace with a list of GitHub repositories.
"""

from pathlib import Path

import requests
from git import Repo


_BASE_DIRECTORY = 'work2/github'
_HOME = str(Path.home().resolve())


def get_repo_list(token: str) -> list:
    """
    Retrieves the list of repositories for the given username.

    :param token:
        The GitHub Personal Access Token

    :returns:
        A JSON object with the list of repositories
    """
    url = 'https://api.github.com/user/repos'
    headers = { 'Authorization': 'token {}'.format(token) }
    r = requests.get(url, headers=headers)

    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        r.raise_for_status()


def clone_repo(repo_ssh: str) -> str:
    """
    Clones a repository.

    :param repo_ssh:
        The SSH repository address

    :returns:
        True if the repository was cloned successfully; False otherwise
    """
    path = str(Path(Path.home(), _BASE_DIRECTORY, Path(repo_ssh).stem).resolve())
    repo = Repo.clone_from(repo_ssh, path)
    if repo and repo.working_tree_dir == path:
        return repo.working_tree_dir
    else:
        return None


def clone_repos():
    """
    Fetches the list of repositories and clones them into the desired directory.
    """
    response = get_repo_list('2f2edfd3564ed6832fc862267a3ced3aca80eb91')
    for x in response:
        repo = clone_repo(x['ssh_url'])
        if repo:
            print('Repository "{}" created successfully'.format(repo))
        else:
            print('Couldn\' clone repository {}'.format(repo))


if __name__ == '__main__':
    clone_repos()
