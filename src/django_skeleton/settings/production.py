# In production set the environment variable like this:
# DJANGO_SETTINGS_MODULE=django_skeleton.settings.production

from .base import *
import logging.config

# For security and performance reasons, DEBUG is turned off
DEBUG = False
TEMPLATE_DEBUG = False

# Use local server Define STATIC_ROOT for the collectstatic command  - Deprecated
STATIC_ROOT = '/usr/share/nginx/html/static/'                 # ./manager.py collectstatic to this directory

# Define Local Server MEDIA_ROOT for User-uploaded files like profile pics need to be served
MEDIA_ROOT = '/usr/share/nginx/html/media/'

# Cache the templates in memory for speed-up
loaders = [
    ('django.template.loaders.cached.Loader', [
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    ]),
]

TEMPLATES[0]['OPTIONS'].update({"loaders": loaders})
TEMPLATES[0].update({"APP_DIRS": False})

ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'                   # For production only

# Log everything to the logs directory at the top
LOGFILE_ROOT = join(dirname(BASE_DIR), 'logs')

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
            'filename': join(LOGFILE_ROOT, 'project.log'),
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
