### Backend

Requires

    pip install -r backend/requirements.txt

Django configuration

* environment variable

  We use [django-environ](https://github.com/joke2k/django-environ), it's more easy for docker image building and CI testing. You might want to change it base on how your variable in Django settings are passing.
  For safety, we list `.env` in .gitignore.
