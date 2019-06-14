# -*- coding: utf8 -*-

"""
Command line interface.

Author: Eduardo Ferreira
"""

from enum import Enum
import argparse
import logging

import mxyzptlk.__version__ as version
import mxyzptlk.bitbucket as bitbucket
import mxyzptlk.github as github
import mxyzptlk.gitlab as gitlab

logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)


class GitName(Enum):
    """
    Names of the Git providers.
    """
    BITBUCKET = 'bitbucket'
    GITHUB = 'github'
    GITLAB = 'gitlab'


def keyboard_interrupt():
    _logger.warn('\nThe program execution was interrupted!\n')


def parse_options(program: str, description: str, version: str) -> argparse.Namespace:
    """
    Parses and retrieves the values for the full set of command line arguments.

    :param program:
        The name of the program
    :param description:
        The description of the program
    :param decode:
        Flag the indicates if it's an encoding or decoding operation
    :return:
        The list of command line arguments
    """
    parser = argparse.ArgumentParser(prog=program, description=description)
    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + version)
    parser.add_argument('-g', '--git', type=str, choices=[entry.value for entry in GitName],
        dest='git_name', help='git provider', required=True)

    return parser.parse_args()


def run():
    """
    """
    try:
        args = parse_options(version.__title__, version.__description__, version.__version__)

        print(args.git_name)
        method = {
            GitName.BITBUCKET.value: bitbucket.clone_repos,
            GitName.GITHUB.value: github.clone_repos,
            GitName.GITLAB.value: gitlab.clone_repos
        }.get(args.git_name)

        return method()
    except KeyboardInterrupt as e:
        keyboard_interrupt()
        exit(1)
