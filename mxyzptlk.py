# -*- coding: utf-8 -*-

"""
Script to automatically configure a workspace with a list of GitHub repositories.

Author: Eduardo Ferreira
"""

import configparser
from pathlib import Path

import requests
from git import Repo


_HOME = Path.home()
_CONFIG_DIRECTORY = Path(_HOME, '.mxyzptlk')
_CONFIG_FILE = Path(_CONFIG_DIRECTORY, 'git.properties')
_BITBUCKET_DIRECTORY = Path(_HOME, 'work', 'bitbucket')
_GITHUB_DIRECTORY = Path(_HOME, 'work', 'github')
_GITLAB_DIRECTORY = Path(_HOME, 'work', 'gitlab')


def read_config_github() -> str:
    """
    Reads the GitHub token from the configuration file.

    :return:
        The access token
    """
    return _read_config('GitHub', 'token')


def read_config_gitlab() -> str:
    """
    Reads the Gitlab token from the configuration file.

    :return:
        The access token
    """
    return _read_config('GitLab', 'token')


def read_config_bitbucket() -> str:
    """
    Reads the Bitbucket token from the configuration file.

    :return:
        The access token
    """
    return _read_config('Bitbucket', 'token')


def _read_config(section: str, value: str) -> str:
    """
    Reads the Bitbucket token from the configuration file.

    :param section:
        The name of the section in the configuration file

    :param value:
        The value to be retrieved

    :return:
        The access token
    """
    if not _CONFIG_DIRECTORY.is_dir():
        raise FileNotFoundError('Configuration directory "{}" not found.'.format(_CONFIG_DIRECTORY.resolve()))

    if not _CONFIG_FILE.is_file():
        raise FileNotFoundError('Configuration file "{}" not found.'.format(_CONFIG_FILE.resolve()))

    config = configparser.ConfigParser()
    config.read(str(_CONFIG_FILE.resolve()))
    
    return config.get(section, value)


def get_repo_list(token: str) -> list:
    """
    Retrieves the list of repositories for the given username.

    :param token:
        The GitHub Personal Access Token

    :return:
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

    :return:
        True if the repository was cloned successfully; False otherwise
    """
    path = str(Path(_WORK_DIRECTORY, Path(repo_ssh).stem).resolve())
    repo = Repo.clone_from(repo_ssh, path)
    if repo and repo.working_tree_dir == path:
        return repo.working_tree_dir
    else:
        return None


def clone_repos():
    """
    Fetches the list of repositories and clones them into the desired directory.
    """
    token = read_config_github()
    if not token:
        raise FileNotFoundError('Configuration file "{}" not found.'.format(_CONFIG_FILE))

    response = get_repo_list(token)
    for x in response:
        repo = clone_repo(x['ssh_url'])
        if repo:
            print('Repository "{}" created successfully.'.format(repo))
        else:
            print('Couldn\' clone repository {}.'.format(repo))


if __name__ == '__main__':
    clone_repos()
