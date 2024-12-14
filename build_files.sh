#!/usr/bin/env bash

# Exit on error
set -o errexit

python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

# pip install -r requirements.txt
python3  manage.py collectstatic --noinput
