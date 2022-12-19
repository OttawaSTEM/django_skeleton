from .env_vars import BASE_DIR
from .base import *
import logging.config

# For security and performance reasons, DEBUG is turned off
DEBUG = False           # Must run "python manage.py collect static", otherwise cause Server Error (500)
TEMPLATE_DEBUG = False
CSRF_TRUSTED_ORIGINS = eval(env('CSRF_TRUSTED_ORIGINS'))      # When DEBUG=False in Deployment

STATIC_ROOT = BASE_DIR.joinpath('static')
MEDIA_ROOT = BASE_DIR.joinpath('media')

# Django Compressor for css and javascript
# COMPRESS_OFFLINE = True
# COMPRESS_ENABLED = True

# Cache the templates in memory for speed-up
loaders = [
    ('django.template.loaders.cached.Loader', [
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    ]),
]

TEMPLATES[0]['OPTIONS'].update({"loaders": loaders})
TEMPLATES[0].update({"APP_DIRS": False})

ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'                   # django-allauth For production only

# Disable browsable API render of django-rest-framework
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}

# Log everything to the logs directory at the top
LOGFILE_ROOT = BASE_DIR.joinpath('logs')

# Reset logging
LOGGING_CONFIG = None
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(pathname)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'proj_log_file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': LOGFILE_ROOT.joinpath('project.log'),
            'encoding': 'utf-8',
            'formatter': 'verbose'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        }
    },
    # In production, log to file
    'loggers': {
        'project': {
            'handlers': ['proj_log_file'],
            'level': 'DEBUG',
        }
    }
}

logging.config.dictConfig(LOGGING)
