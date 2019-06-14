# -*- coding: utf-8 -*-

"""
Setup module.

Author: Eduardo Ferreira
"""

from setuptools import setup, find_packages

setup(
    name='mxyzpltk',
    version='0.0.1',
    description='Script to automatically configure a workspace with a list of Git repositories.',
    author='Eduardo Ferreira',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'mxyzptlk = mxyzptlk.cli:run'
        ]
    }
)
