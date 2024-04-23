
## prerequisite

* `poetry` package manager

## Installtion

### Homebrew

```sh
brew install poetry
brew install pyenv
```

```sh
pyenv install -v 3.8.12 # virtual python 3.8 environment
poetry env use 3.8.12 # use python virtual environment
poetry install # install dependencies
```

## Usage

```
poetry run flask --app api run
```
