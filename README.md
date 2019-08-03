# bauen

Configures a workspace with a list of Git repositories.

## Description

Given that I frequently spin up disposable development workspaces, I need to
quickly fetch and clone the set of git repositories in my accounts on Bitbucket,
GitHub, and GitLab.

## Configuration

The script uses the personal access information stored in a properties file
called `git.properties` located in a directory in the root of the user's home
directory called `.bauen`:

```
/home/user/.bauen/git.properties
```

The purpose of the properties file is to avoid having to pass the information as
command line parameters when running the script:

```
[Bitbucket]
key = super_key
secret = super_secret
user = super_user

[GitHub]
token = super_token

[GitLab]
token = super_token
```

The repositories are cloned to sub-directories of the directory `work` in the
root of the user's home directory:

* Bitbucket: `/home/user/work/bitbucket/`
* GitHub: `/home/user/work/github/`
* GitLab: `/home/user/work/gitlab/`

## Install

* Clone the repository

```
$ git clone git@github.com:MulberryBeacon/bauen.git
```

* Install with `pip`

```
$ cd /path/to/bauen
$ pip install .
```

## Instructions

The `bauen` program has the following set of options:

    usage: bauen [-h] [-v] -g {bitbucket,github,gitlab}

    Configures a workspace with a list of Git repositories.

    optional arguments:
    -h, --help            show this help message and exit
    -v, --version         show program's version number and exit
    -g {bitbucket,github,gitlab}, --git {bitbucket,github,gitlab}
                          git provider

The current syntax for the programs requires that the location of both input
and output files be defined explicitly.

## Examples

To clone the list of repositores on GitHub:

    bauen -g github

## Dependencies

All development and testing activities are carried out on Windows 10 using
Python 3.7.4. The following packages are required:

* `requests`
* `gitpython`

## Code metrics

`CLOC`

    github.com/AlDanial/cloc v 1.80  T=0.50 s (18.0 files/s, 1088.0 lines/s)
    -------------------------------------------------------------------------------
    Language                     files          blank        comment           code
    -------------------------------------------------------------------------------
    Python                           8            115            143            186
    Markdown                         1             34              0             66
    -------------------------------------------------------------------------------
    SUM:                             9            149            143            252
    -------------------------------------------------------------------------------

## Disclaimer

This **is not** production ready code.

## License

Copyright (c) 2019 Eduardo Ferreira

The code in this repository is MIT licensed, and therefore free to use as you
please for commercial or non-commercial purposes (see [LICENSE](LICENSE) for
details).
