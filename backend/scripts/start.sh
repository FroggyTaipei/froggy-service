#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset
set -o xtrace

python manage.py migrate
echo "from apps.users.models import User; User.objects.create_superuser('admin@example.com', 'pass')" | python manage.py shell
python manage.py compilemessages
python manage.py loaddata region status type
python manage.py loaddata case.test.yaml arrange.test.yaml
python manage.py collectstatic --noinput --verbosity 0
python manage.py runserver_plus 0.0.0.0:8000
