ECHO OFF
SET current_path=%cd%

cd src
%current_path%\venv\Scripts\python manage.py makemessages -a
%current_path%\venv\Scripts\python manage.py translate_messages -u -f
%current_path%\venv\Scripts\python manage.py compilemessages
cd ..