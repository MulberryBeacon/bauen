# -*- coding: utf-8 -*-

"""
Script to automatically configure a workspace with a list of GitHub repositories.

Author: Eduardo Ferreira
"""

from pathlib import Path

import requests
from git import Repo

import mxyzptlk.config as config



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
