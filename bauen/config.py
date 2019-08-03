# -*- coding: utf-8 -*-

"""
Handles the configuration file.

Author: Eduardo Ferreira
"""

import configparser
from pathlib import Path


_HOME = Path.home()
_CONFIG_DIRECTORY = Path(_HOME, '.bauen')
_CONFIG_FILE = Path(_CONFIG_DIRECTORY, 'git.properties')
_WORK_DIRECTORY = Path(_HOME, 'work')


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


def get_home_directory() -> str:
    """
    Gets the home directory of the current user.

    :return:
        The absolute path to the home directory
    """
    return _HOME


def get_work_directory(directory: str) -> Path:
    """
    Gets the work directory.

    :param directory:
        The specific work directory

    :return:
        The absolute path to the work directory
    """
    return Path(_WORK_DIRECTORY, directory)
