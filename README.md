# mxyzptlk

Script to automatically configure a workspace with a list of GitHub repositories.

Given that I frequently spin up disposable development workspaces, I need to
quickly fetch and clone my list of GitHub repositories.

The script uses a GitHub personal access token stored in a directory in the root
of the user's home directory called `.github`. Its purpose is to avoid having to
pass the token as a command line parameter when running script. The list of GitHub
repositories is cloned to the directory `work/github` in the root of the user's
home directory.

This _is not_ production ready code.

## License

Copyright (c) 2019 Eduardo Ferreira

The code in this repository is MIT licensed, and therefore free to use as you
please for commercial or non-commercial purposes (see [LICENSE](LICENSE) for
details).
