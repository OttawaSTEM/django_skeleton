# In production set the environment variable like this:
# DJANGO_SETTINGS_MODULE=django_skeleton.settings.production

from .base import *
import logging.config
import os

# For security and performance reasons, DEBUG is turned off
DEBUG = False
TEMPLATE_DEBUG = False

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]       # ./manager.py collectstatic from this directory
STATIC_ROOT = '/usr/share/nginx/html/static/'               # ./manager.py collectstatic to this directory
MEDIA_ROOT = '/usr/share/nginx/html/media/'

# Django Compressor
COMPRESS_OFFLINE = False

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

# Email server settings
if 'smtp' in EMAIL_CONFIG['EMAIL_BACKEND']:
    EMAIL_USE_SSL = True
    EMAIL_HOST = EMAIL_CONFIG['EMAIL_HOST']
    EMAIL_PORT = EMAIL_CONFIG['EMAIL_PORT']
    EMAIL_HOST_USER = EMAIL_CONFIG['EMAIL_HOST_USER']
    EMAIL_HOST_PASSWORD = EMAIL_CONFIG['EMAIL_HOST_PASSWORD']
    DEFAULT_FROM_EMAIL = EMAIL_CONFIG['EMAIL_HOST_USER']
    
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
