release: mkdir logs | python $PWD/src/manage.py migrate
web: gunicorn --pythonpath="$PWD/src" django_skeleton.wsgi