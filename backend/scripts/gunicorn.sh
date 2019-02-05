#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset

python manage.py migrate
python manage.py compilemessages
gunicorn config.wsgi -w 4 --worker-class gevent -t 240 -b 0.0.0.0:8000 --chdir=/app
