# mxyzptlk

Script to automatically configure a workspace with a list of GitHub repositories.

Given that I frequently spin up disposable development workspaces, I need to
quickly fetch and clone my list of GitHub repositories.

The script looks for a GitHub Personal Access Token in a directory called `.github`
in the root of the user's home directory. The list of GitHub repositories is
cloned to the directory `work/github` in the root of the user's home directory.

This *is not* production ready code.

## License

Copyright (c) 2019 Eduardo Ferreira

The code in this repository is MIT licensed, and therefore free to use as you
please for commercial or non-commercial purposes (see [LICENSE](LICENSE) for
details).
