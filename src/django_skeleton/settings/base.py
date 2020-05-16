"""
Django settings for baiju project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from os.path import dirname, join, exists, abspath
# from celery.schedules import crontab

# Use 12factor inspired environment variables or from a file
import environ
env = environ.Env()

# Ideally move env file should be outside the git repo
# i.e. BASE_DIR.parent.parent
env_file = join(dirname(__file__), 'local.env')
if exists(env_file):
    environ.Env.read_env(str(env_file))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# Sitemaps
# Need to update database table: django_site manual from example.com to domain name, which match record ID=1
SITE_ID = 1
SITE_NAME = 'django_skeleton'
SITE_URL = 'https://django_skeleton.com/' 

BASE_DIR = dirname(dirname(dirname(abspath(__file__))))

# Local - Build paths inside the project like this: join(BASE_DIR, "directory")
STATICFILES_DIRS = [join(BASE_DIR, 'static')]           # For ./manager.py collectstatic
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/
MEDIA_ROOT = join(BASE_DIR, 'media')

# Define Local Server MEDIA_ROOT for User-uploaded files like profile pics need to be served
STATIC_URL = '/static/'                 # Local
MEDIA_URL = '/media/'                 # Local

# To use this setting, install the Argon2 password hashing algorithm.
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
]

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
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                
                # Need update django_skeleton to project folder name
                'django_skeleton.context_processors.global_settings'
            ],
        },
    },
]


# SECURITY WARNING: keep the secret key used in production secret!
# Raises ImproperlyConfigured exception if SECRET_KEY not in os.environ
SECRET_KEY = env('SECRET_KEY')

# ALLOWED_HOSTS
ALLOWED_HOSTS = eval(env('ALLOWED_HOSTS'))

# Application definition
INSTALLED_APPS = (
    'registration',
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'django.contrib.staticfiles',
  
    'authtools',
    'autotranslate',
    'crispy_forms',
    # 'dbbackup',
    
    'accounts',
    'profiles',
)

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'django_skeleton.urls'

WSGI_APPLICATION = 'django_skeleton.wsgi.application'

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    # Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
    'default': env.db()
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

# Default data format: 2000-02-18
USE_I18N = True
USE_L10N = True
TIME_ZONE = 'America/Toronto'
USE_TZ = True

# Language
LOCALE_PATHS = (join(BASE_DIR, 'locale'),)
LANGUAGE_CODE = 'en'
LANGUAGES = (
    ('en', _('English')),
    ('fr', _('French')),
    ('zh-cn', _('Simplified Chinese'))
)


# Crispy Form Theme - Bootstrap 3
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# For Bootstrap 3, change error alert to 'danger'
from django.contrib import messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}

# Authentication Settings
AUTH_USER_MODEL = 'authtools.User'
LOGIN_REDIRECT_URL = reverse_lazy("profiles:show_self")
LOGIN_URL = reverse_lazy("accounts:login")

# For django-registration-redux Settings
ACCOUNT_ACTIVATION_DAYS = 1         # One-day activation window
REGISTRATION_EMAIL_HTML = False     # Only use templates/registration/activation_email.txt

# Google reCAPTCHA
RECAPTCHA_SITE_KEY = env('RECAPTCHA_SITE_KEY')
RECAPTCHA_SECRET_KEY = env('RECAPTCHA_SECRET_KEY')

GOOGLE_ANALYTICS_TRACKING_ID = env('GOOGLE_ANALYTICS_TRACKING_ID')

# django-autotranslate change translation service
# AUTOTRANSLATE_TRANSLATOR_SERVICE = 'autotranslate.services.GoSlateTranslatorService'
# AUTOTRANSLATE_TRANSLATOR_SERVICE = 'autotranslate.services.GoogleWebTranslatorService'
AUTOTRANSLATE_TRANSLATOR_SERVICE = 'autotranslate.services.AzureAPITranslatorService'
AZURE_TRANSLATOR_SECRET_KEY = env('AZURE_TRANSLATOR_SECRET_KEY')