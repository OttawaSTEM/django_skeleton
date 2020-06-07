release: mkdir logs
release: python manage.py migrate
web: gunicorn --pythonpath="$PWD/src" django_skeleton.wsgi