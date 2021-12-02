# Building an API test automation framework with Python

## Setup
Also git clone people-api to set up the local database in a virtualenv

```zsh
# Activate virtualenv
pipenv shell
# Install all dependencies in your virtualenv
pipenv install
```

## How to navigate

Each chapter has its own dedicated branch in `/example/<chapter_no>_<topic>` format. For e.g.
`example/01_setup_python_dependencies`

You can either use your IDE or terminal to switch to that branch and see the last updated commit.

```zsh
# Checkout the entire branch
git checkout example/01_setup_python_dependencies
# Checkout to a specific commit, here <sha> can be found using `git log` command
git checkout <sha>
```

## How to run

```zsh
# Setup report portal on docker
# Update rp_uuid in pytest.ini with project token
docker-compose -f docker-compose.yml -p reportportal up -d

# Launch pipenv
pipenv shell

# Install all packages
pipenv install

# Run tests via pytest (single threaded)
python -m pytest

# Run tests in parallel
python -m pytest -n auto

# Report results to report portal
python -m pytest -n auto ./tests --reportportal
```

