**A Django project starter.**
## Features

* Ready Bootstrap-themed pages
* User Registration/Sign up
* Better Security with [12-Factor](http://12factor.net/) recommendations
* Logging/Debugging Helpers
* Works on Python 3 and Django 2

# {{ project_name }}
!!! project name CAN NOT use '-' due to python conflict

## Installation
1. Change project name and src/django_skeleton folder name

### Quick start
To set up a development environment quickly, first install Python 3. It
comes with virtualenv built-in. So create a virtual env by:

    1. `$ python3 -m venv {{ project_name }}`
    2. `$ python -m pip install --upgrade pip`
    3. `$ . {{ project_name }}/bin/activate`

Install all dependencies:

    pip install -r requirements.txt

Run migrations:
    # Update database change scripts
    python src\manage.py makemigrations

    # Update database change
    python manage.py migrate

# Production Deployment
daphne myproject.asgi:application


# django-allauth Google Authenticate
https://www.youtube.com/watch?v=NG48CLLsb1A

https://developers.google.com/gmail/api/quickstart/js
https://console.developers.google.com/

# django-autotranslate (User custom version)
(venv)$ python manage.py makemessages -a
(venv)$ python manage.py translate_messages -u -f
(venv)$ python manage.py compilemessages

# Django create app add to project
(venv)$ python manage.py startapp poll

# Update Table (Drop Table Method)
## Method 1:
1. Delete application relate tables and data
   $ python manage.py migrate registrationform zero
2. Recreate Table
   $ python manage.py ./manage.py migrate

## Method 2:
1. Export Data from Workbench (Data Only)
2. Update exported data
3. Drop Table from database
4. Update Drop Table status in Django
   $ python manage.py ./manage.py migrate --fake [table_name] zero
5. Recreate Table
   $ python manage.py ./manage.py migrate


# Django SEO
Registered your site with Google Webmaster Tools.
[Google Search Console](https://search.google.com/)

$ python manage.py ping_google