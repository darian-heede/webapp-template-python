#!/bin/bash

set -e

cd app
pip install -r requirements.txt

python app.py

exec "$@"