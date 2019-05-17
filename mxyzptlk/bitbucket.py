# -*- coding: utf-8 -*-

"""
Script to automatically configure a workspace with a list of Bitbucket repositories.

Author: Eduardo Ferreira
"""

from pathlib import Path

import requests

import config as config
import repository as repository


_BITBUCKET_DIRECTORY = Path(config.WORK_DIRECTORY, 'bitbucket')


def get_access_token(key: str, secret: str, code: str) -> str:
    """
    """
    url = 'https://bitbucket.org/site/oauth2/access_token'
    data = {
        'grant_type': 'authorization_code',
        'code': code
    }
    response = requests.post(url, data, auth=(key, secret))

    if response.status_code != requests.codes.get('ok'):
        response.raise_for_status()

    return response.json()['access_token']


def get_repo_list(user: str, token: str) -> list:
    """
    Retrieves the list of repositories for the given username.

    :param token:
        The GitHub Personal Access Token

    :return:
        A JSON object with the list of repositories
    """
    url = 'https://api.bitbucket.org/2.0/repositories/{}'.format(user)
    headers = {
        'Authorization': 'Bearer {}'.format(token)
    }
    response = requests.get(url, headers=headers)

    if response.status_code != requests.codes.get('ok'):
        response.raise_for_status()

    return response.json()


def clone_repos():
    """
    Fetches the list of repositories and clones them into the desired directory.
    """
    key = config.read_config('Bitbucket', 'key')
    secret = config.read_config('Bitbucket', 'secret')
    code = config.read_config('Bitbucket', 'code')
    token = get_access_token(key, secret, code)
    print(token)

    for parameters in response:
        repo = repository.clone_repo(_BITBUCKET_DIRECTORY, parameters['ssh_url'])
        if repo:
            print('Repository "{}" created successfully.'.format(repo))
        else:
            print('Couldn\'t clone repository {}.'.format(repo))


if __name__ == '__main__':
    clone_repos()
