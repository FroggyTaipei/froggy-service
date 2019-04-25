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
echo "from apps.users.tests.setup import create_superuser; create_superuser()" | python manage.py shell

python manage.py runserver_plus 0.0.0.0:8000
