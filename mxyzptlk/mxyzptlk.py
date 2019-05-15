# -*- coding: utf-8 -*-

"""
Script to automatically configure a workspace with a list of GitHub repositories.

Author: Eduardo Ferreira
"""

from pathlib import Path

import requests
from git import Repo

import mxyzptlk.config as config


BITBUCKET_DIRECTORY = Path(config.HOME, 'work', 'bitbucket')
GITHUB_DIRECTORY = Path(config.WORK_DIRECTORY, 'github2')
GITLAB_DIRECTORY = Path(config.HOME, 'work', 'gitlab')


def read_config_github() -> str:
    """
    Reads the GitHub token from the configuration file.

    :return:
        The access token
    """
    return config.read_config('GitHub', 'token')


def read_config_gitlab() -> str:
    """
    Reads the Gitlab token from the configuration file.

    :return:
        The access token
    """
    return config.read_config('GitLab', 'token')


def read_config_bitbucket() -> str:
    """
    Reads the Bitbucket token from the configuration file.

    :return:
        The access token
    """
    return config.read_config('Bitbucket', 'token')


def get_repo_list(token: str) -> list:
    """
    Retrieves the list of repositories for the given username.

    :param token:
        The GitHub Personal Access Token

    :return:
        A JSON object with the list of repositories
    """
    url = 'https://api.github.com/user/repos'
    headers = {
        'Authorization': 'token {}'.format(token)
    }
    response = requests.get(url, headers=headers)

    if response.status_code != requests.codes.get('ok'):
        response.raise_for_status()

    return response.json()


def clone_repo(repo_ssh: str) -> str:
    """
    Clones a repository.

    :param repo_ssh:
        The SSH repository address

    :return:
        True if the repository was cloned successfully; False otherwise
    """
    path = str(Path(GITHUB_DIRECTORY, Path(repo_ssh).stem).resolve())
    repo = Repo.clone_from(repo_ssh, path)
    if repo and repo.working_tree_dir == path:
        return repo.working_tree_dir

    return None


def clone_repos():
    """
    Fetches the list of repositories and clones them into the desired directory.
    """
    token = read_config_github()
    response = get_repo_list(token)

    for parameters in response:
        repo = clone_repo(parameters['ssh_url'])
        if repo:
            print('Repository "{}" created successfully.'.format(repo))
        else:
            print('Couldn\'t clone repository {}.'.format(repo))


if __name__ == '__main__':
    clone_repos()
