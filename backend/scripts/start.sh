#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset
set -o xtrace

python manage.py migrate
python manage.py compilemessages
python manage.py loaddata region type
python manage.py loaddata case.test.yaml arrange.test.yaml
echo "from apps.users.tests.initial import create_superuser" | python manage.py shell
python manage.py collectstatic --noinput --verbosity 0
python manage.py runserver_plus 0.0.0.0:8000
