# Django 4 Asynchronous support

[Django 4.1 - Where To Apply Async](https://medium.com/@ivan.slavko.matic.96/django-4-1-where-to-apply-async-c05f29ca2041)

## Async views

- For the function-based view, declaring the whole view using "async def"
- For the class-based view, declaring the HTTP method handlers, such as "async def get()" and "async def post()"

## Queries & the ORM

```
async for author in Author.objects.filter(name__startswith="A"):
   book = await author.books.afirst()
```

# Setup Django virtual environment

## Windows

```
python -m venv venv
venv\Scripts\activate
python -m pip install pip --upgrade
pip install -r requirements\development.txt
pip install -r requirements\production.txt
```

## MacOS,Linux

```
python3 -m venv venv
. venv/bin/activate
python -m pip install pip --upgrade
pip install -r requirements/development.txt
pip install -r requirements/production.txt
```

## Features

- Ready Bootstrap-themed pages
- User Registration/Sign up
- Better Security with [12-Factor](http://12factor.net/) recommendations
- Logging/Debugging Helpers
- Works on Python 3 and Django 2

# {{ project_name }}

!!! project name CAN NOT use '-' due to python conflict

## Installation

1. Change project name and django_skeleton folder name

### Quick start

To set up a development environment quickly, first install Python 3. It
comes with virtualenv built-in. So create a virtual env by:

    1. `$ python3 -m venv {{ project_name }}`
    2. `$ python -m pip install --upgrade pip`
    3. `$ . {{ project_name }}/bin/activate`

Install all dependencies:

    pip install -r requirements.txt

Run migrations: # Update database change scripts
python manage.py makemigrations

    # Update database change
    python manage.py migrate

    # Create superuser
    python manage.py createsuperuser

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

[PO File Translate](https://pofile.net/free-po-editor)

# Django create app add to project

(venv)$ python manage.py startapp <new_app>

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

The ping_google() command only works if you have registered your site with Google Webmaster Tools.
Registered your site with Google Webmaster Tools.
[Google Search Console](https://www.google.com/webmasters/tools/)

```
$ python manage.py ping_google
```

# Daphne

daphne django_skeleton.asgi:application

# Heroku

Procfile
requirements.txt
logs/project.log
database: db.sqlite

# Django Auto Translate - django-autotranslate

```
# Translate language
$ django-admin makemessages -l fr -i venv
$ django-admin makemessages -l zh_Hans -i venv

# Compile language po for production
$ django-admin compilemessages         # Compile all languanges
$ django-admin compilemessages -l fr
$ django-admin compilemessages -l zh_Hans
```

# gettext() vs gettext_lazy()

## Use gettext_lazy() in forms or models

In definitions like forms or models you should use gettext_lazy because the code of this definitions is only executed once (mostly on django's startup);

## use gettext()) in view

In views and similar function calls you can use gettext without problems, because everytime the view is called gettext will be newly executed, so you will always get the right translation fitting the request!

# Provide initial data

python manage.py loaddata api/books.json


# Generating an OpenAPI Schema
```
python manage.py generateschema --file static/site/openapi/schema.yaml
```

# Google Login "Invalid id_token"
django-allauth==0.50.0
dj-rest-auth==4.0.1    


# Test SendEmail
```bash
python manage.py shell

>>> from dharro.utils import SendEmail
>>> SendEmail('test', 'test')
```