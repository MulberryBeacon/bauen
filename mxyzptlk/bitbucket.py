# -*- coding: utf-8 -*-

"""
Script to automatically configure a workspace with a list of Bitbucket repositories.

Author: Eduardo Ferreira
"""

import requests

import mxyzptlk.config as config
import mxyzptlk.repository as repository


_BITBUCKET_DIRECTORY = config.get_work_directory('bitbucket')


def _get_access_token(key: str, secret: str) -> str:
    """
    Requests an access token from Bitbucket.

    :param key:
        The OAuth consumer key

    :param secret:
        The OAuth consumer secret

    :return:
        The Bitbucket access token
    """
    url = 'https://bitbucket.org/site/oauth2/access_token'
    data = {
        'grant_type': 'client_credentials'
    }
    response = requests.post(url, data, auth=(key, secret))

    if response.status_code != requests.codes.get('ok'):
        response.raise_for_status()

    return response.json()['access_token']


def _get_repo_list(user: str, token: str) -> list:
    """
    Retrieves the list of repositories for the given username.

    :param user:
        The Bitbucket username

    :param token:
        The Bitbucket access token

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

    return response.json()['values']


def clone_repos():
    """
    Fetches the list of repositories and clones them into the desired directory.
    """
    key = config.read_config('Bitbucket', 'key')
    secret = config.read_config('Bitbucket', 'secret')
    user = config.read_config('Bitbucket', 'user')

    token = _get_access_token(key, secret)
    response = _get_repo_list(user, token)

    for parameters in response:
        repo = repository.clone_repo(_BITBUCKET_DIRECTORY, parameters['links']['clone'][1]['href'])
        if repo:
            print('Repository "{}" created successfully.'.format(repo))
        else:
            print('Couldn\'t clone repository {}.'.format(repo))
