#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset
set -o xtrace

python manage.py migrate
python manage.py compilemessages
python manage.py collectstatic --noinput --verbosity 0

python manage.py loaddata region type site sendgrid-template.yaml
python manage.py loaddata cases.test.yaml arranges.test.yaml

python manage.py init_superuser test@test.test 123456

python manage.py runserver 0.0.0.0:8000
