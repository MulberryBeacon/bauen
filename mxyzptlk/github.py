# -*- coding: utf-8 -*-

"""
Script to automatically configure a workspace with a list of GitHub repositories.

Author: Eduardo Ferreira
"""

from pathlib import Path

import requests

import mxyzptlk.config as config
import mxyzptlk.repository as repository


_GITHUB_DIRECTORY = Path(config.WORK_DIRECTORY, 'github')


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


def clone_repos():
    """
    Fetches the list of repositories and clones them into the desired directory.
    """
    token = config.read_config('GitHub', 'token')
    response = get_repo_list(token)

    for parameters in response:
        repo = repository.clone_repo(_GITHUB_DIRECTORY, parameters['ssh_url'])
        if repo:
            print('Repository "{}" created successfully.'.format(repo))
        else:
            print('Couldn\'t clone repository {}.'.format(repo))
