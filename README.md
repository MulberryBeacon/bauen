# mxyzptlk

Script to automatically configure a workspace with a list of GitHub repositories.

## Description

Given that I frequently spin up disposable development workspaces, I need to
quickly fetch and clone my list of GitHub repositories.

## Configuration

The script uses a GitHub personal access token that is stored in a properties
file called `github.properties` located in a directory in the root of the
user's home directory called `.github`:

```
/home/user/.github/github.properties
```

The purpose of the properties file is to avoid having to pass the token as a
command line parameter when running the script:

```
[GitHub]
token = super_secret_token
```

The list of GitHub repositories is cloned to the directory `work/github` in the
root of the user's home directory:

```
/home/user/work/github/
```

## Instructions

To run the script, navigate to the directory with the source code and use the
Python executable:

```
cd /path/to/mxyzptlk/
python3 mxyzptlk.py
```

## Dependencies

All development and testing activities are carried out on Ubuntu 18.10 using
Python 3.6.7. The following packages are required:

* `requests`
* `gitpython`

## Disclaimer

This **is not** production ready code.

## License

Copyright (c) 2019 Eduardo Ferreira

The code in this repository is MIT licensed, and therefore free to use as you
please for commercial or non-commercial purposes (see [LICENSE](LICENSE) for
details).
