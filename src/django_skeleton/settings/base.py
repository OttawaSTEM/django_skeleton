"""
For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from os.path import dirname, join, exists, abspath
# from celery.schedules import crontab

from .allauth import *
from .compressor import *
from .crispy_form import *
from .database import *
from .email import *
from .google import *
from .timezone_language import *

# Use 12factor inspired environment variables or from a file
import environ
env = environ.Env()

# Ideally move env file should be outside the git repo, i.e. BASE_DIR.parent.parent
env_file = join(dirname(__file__), 'local.env')
if exists(env_file):
    environ.Env.read_env(str(env_file))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# ALLOWED_HOSTS
ALLOWED_HOSTS = eval(env('ALLOWED_HOSTS'))

# Sitemaps
# Need to update database table: django_site manual from example.com to domain name, which match record ID=1
SITE_ID = 1
SITE_NAME = 'django_skeleton'
SITE_URL = 'https://django_skeleton.com/' 

BASE_DIR = dirname(dirname(dirname(abspath(__file__))))

# Define Local Server MEDIA_ROOT for User-uploaded files like profile pics need to be served
STATIC_URL = '/static/'                 # Local
MEDIA_URL = '/media/'                   # Local

# SECURITY WARNING: keep the secret key used in production secret!
# Raises ImproperlyConfigured exception if SECRET_KEY not in os.environ
SECRET_KEY = env('SECRET_KEY')

# Use PBKDF2 algorithm with a SHA256 hash
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
]

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators
# https://docs.djangoproject.com/en/3.0/topics/auth/passwords/#password-validation
# AUTH_PASSWORD_VALIDATORS = [
#     {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
#     {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
#     {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
#     {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
# ]

# Use Django templates using the new Django 1.8 TEMPLATES settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            join(BASE_DIR, 'templates'),
            # insert more TEMPLATE_DIRS here
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                
                # django-allauth needs this from django
                'django.template.context_processors.request',

                # global settings for templates. Need update django_skeleton to project folder name
                'django_skeleton.context_processors.global_settings',
            ],
        },
    },
]

# Application definition
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'django.contrib.staticfiles',
  
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'captcha',
    'compressor',

    'crispy_forms',
    'dbbackup',
    
    'profiles',
    'websocket',
    'chat',
)

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'django_skeleton.urls'
ASGI_APPLICATION = 'django_skeleton.asgi.application'
