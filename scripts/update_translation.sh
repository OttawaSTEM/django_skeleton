cd /Volumes/Data/Workspace/Django/Baiju/src
source /Volumes/Data/Workspace/Django/venv/bin/activate && ./manage.py makemessages -a
source /Volumes/Data/Workspace/Django/venv/bin/activate && ./manage.py translate_messages -u
source /Volumes/Data/Workspace/Django/venv/bin/activate && ./manage.py compilemessages
