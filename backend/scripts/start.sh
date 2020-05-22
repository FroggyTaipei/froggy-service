#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset
set -o xtrace

python manage.py migrate
python manage.py compilemessages
python manage.py collectstatic --noinput --verbosity 0

# Load test data
python manage.py loaddata region type site sendgrid-template.yaml marquee.yaml
python manage.py loaddata cases.test.yaml arranges.test.yaml

# Create a dev user
python manage.py init_superuser test@test.test 123456

# Store insights to cache
python manage.py cache_insights

python manage.py runserver 0.0.0.0:8000
