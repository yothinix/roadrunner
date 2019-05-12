#!/usr/bin/env bash

python -m black --target-version py36 --line-length 99 .
python -m isort --apply --line-width 99
python -m flake8 --max-line-length=99
python -m pytest
