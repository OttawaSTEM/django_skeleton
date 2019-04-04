# source ./scripts/start.sh
pg_ctl -D /usr/local/var/postgres start
. /Volumes/Data/Workspace/Django/Rentbnb/venv/bin/activate
cd /Volumes/Data/Workspace/Django/Rentbnb/src
./manage.py runserver 0.0.0.0:8000
