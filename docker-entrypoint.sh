#!/bin/bash

set -e

cd app
pip install -r requirements.txt

#python app.py
gunicorn --bind 0.0.0.0:5001 wsgi:app

exec "$@"