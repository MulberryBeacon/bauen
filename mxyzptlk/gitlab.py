# -*- coding: utf-8 -*-

"""
Script to automatically configure a workspace with a list of GitLab repositories.

Author: Eduardo Ferreira
"""

import requests

import mxyzptlk.config as config
import mxyzptlk.repository as repository


_GITLAB_DIRECTORY = config.get_work_directory('gitlab')


def _get_repo_list(token: str) -> list:
    """
    Retrieves the list of repositories for the given username.

    :param token:
        The GitLab access token

    :return:
        A JSON object with the list of repositories
    """
    url = 'https://gitlab.com/api/v4/projects'

    headers = {
        'Private-Token': token
    }

    params = {
        'simple': True,
        'owned': True
    }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code != requests.codes.get('ok'):
        response.raise_for_status()

    return response.json()


def clone_repos():
    """
    Fetches the list of repositories and clones them into the desired directory.
    """
    token = config.read_config('GitLab', 'token')
    response = get_repo_list(token)

    for parameters in response:
        repo = repository.clone_repo(_GITLAB_DIRECTORY, parameters['ssh_url'])
        if repo:
            print('Repository "{}" created successfully.'.format(repo))
        else:
            print('Couldn\'t clone repository {}.'.format(repo))


if __name__ == '__main__':
    token = config.read_config('GitLab', 'token')
    response = _get_repo_list(token)
    print(response)