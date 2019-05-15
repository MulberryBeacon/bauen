# -*- coding: utf-8 -*-

"""
Script to automatically configure a workspace with a list of GitHub repositories.

Author: Eduardo Ferreira
"""

from pathlib import Path

import requests
from git import Repo

import mxyzptlk.config as config


BITBUCKET_DIRECTORY = Path(config.WORK_DIRECTORY, 'bitbucket')
