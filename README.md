# practice

This repository contains practice code

## Installation
```
poetry install
```

## Run first command
```
$ source $(poetry env info --path)/bin/activate
$ hello
```
or
```
poetry run hello
```
## Format
```
poetry run black practice tests && poetry run isort practice tests
```