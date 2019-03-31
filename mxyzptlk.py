# -*- coding: utf-8 -*-

"""
Script to automatically configure a workspace with a list of GitHub repositories.
"""

import requests
from gitpython import Repo

def get_repo_list(username: str, token: str) -> list:
    """
    Retrieves the list of repositories for the given username.
    """
    url = 'https://api.github.com/users/{}/repos'.format(username) 
    headers = { 'Authorization': 'token {}'.format(token) }
    r = requests.get(url, headers=headers)
    return r.json()

def clone_repo(repo_ssh: str, destination: str):
    """
    """
    Repo.clone_from(repo_ssh, destination)

def action():
    """
    """
    response = get_repo_list('MulberryBeacon', '2f2edfd3564ed6832fc862267a3ced3aca80eb91')
    for x in response:
        ssh_url = x['ssh_url']
        clone_repo(ssh_url, '.')


if __name__ == '__main__':
    action()
