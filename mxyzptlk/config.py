# -*- coding: utf-8 -*-

"""
Handles the configuration file.

Author: Eduardo Ferreira
"""

import configparser
from pathlib import Path


HOME = Path.home()
_CONFIG_DIRECTORY = Path(HOME, '.mxyzptlk')
_CONFIG_FILE = Path(_CONFIG_DIRECTORY, 'git.properties')
WORK_DIRECTORY = Path(HOME, 'work')


def read_config(section: str, value: str) -> str:
    """
    Reads the token from the configuration file.

    :param section:
        The name of the section in the configuration file

    :param value:
        The value to be retrieved

    :return:
        The access token
    """
    if not _CONFIG_DIRECTORY.is_dir():
        raise FileNotFoundError(
            'Configuration directory "{}" not found.'.format(_CONFIG_DIRECTORY.resolve())
        )

    if not _CONFIG_FILE.is_file():
        raise FileNotFoundError(
            'Configuration file "{}" not found.'.format(_CONFIG_FILE.resolve())
        )

    config = configparser.ConfigParser()
    config.read(str(_CONFIG_FILE.resolve()))
    token = config.get(section, value)

    if not token:
        raise ValueError(
            'Section "{}" and parameter "{}" not found.'.format(section, value)
        )

    return token
