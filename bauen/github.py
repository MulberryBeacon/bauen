# -*- coding: utf-8 -*-

"""
Configures a workspace with a list of GitHub repositories.

Author: Eduardo Ferreira
"""

import requests

import bauen.config as config
import bauen.repository as repository


_GITHUB_DIRECTORY = config.get_work_directory('github')


def _get_repo_list(token: str) -> list:
    """
    Retrieves the list of repositories for the authenticated user.

    :param token:
        The GitHub access token

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
    response = _get_repo_list(token)

    for parameters in response:
        repo = repository.clone_repo(_GITHUB_DIRECTORY, parameters['ssh_url'])
        if repo:
            print('Repository "{}" created successfully.'.format(repo))
        else:
            print('Couldn\'t clone repository {}.'.format(repo))
