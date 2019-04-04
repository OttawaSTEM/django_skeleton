# In production set the environment variable like this:
#    DJANGO_SETTINGS_MODULE=mingvisa.settings.production
from .base import *             # NOQA
import logging.config

# For security and performance reasons, DEBUG is turned off
DEBUG = False
TEMPLATE_DEBUG = False

# Cache the templates in memory for speed-up
loaders = [
    ('django.template.loaders.cached.Loader', [
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    ]),
]

TEMPLATES[0]['OPTIONS'].update({"loaders": loaders})
TEMPLATES[0].update({"APP_DIRS": False})

# Use local server Define STATIC_ROOT for the collectstatic command  - Deprecated
# STATIC_ROOT = '/usr/share/nginx/html/static/'                 # ./manager.py collectstatic to this directory

# Define Local Server MEDIA_ROOT for User-uploaded files like profile pics need to be served
# MEDIA_URL = 'https://s3.{}.amazonaws.com/{}/media/'.format(AWS_S3_REGION_NAME, AWS_STORAGE_BUCKET_NAME)
# MEDIA_ROOT = '/usr/share/nginx/html/media/'

# Amaxon AWS S3 Static Settings
# AWS_S3_CUSTOM_DOMAIN = 's3.{}.amazonaws.com'.format(AWS_S3_REGION_NAME)  # Use S3 as a CDN (via CloudFront)
# STATIC_URL = 'https://{}/{}/static/'.format(AWS_S3_CUSTOM_DOMAIN, AWS_STORAGE_BUCKET_NAME)        # Use Amazon CloudFront CDN
STATIC_URL = 'https://s3.{}.amazonaws.com/{}/static/'.format(AWS_S3_REGION_NAME, AWS_STORAGE_BUCKET_NAME)
AWS_STATIC_LOCATION = 'static'
STATICFILES_STORAGE = 'rentbnb.storage_backends.StaticStorage'

AWS_PUBLIC_MEDIA_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'rentbnb.storage_backends.PublicMediaStorage'            # easy_thumbnail use this for read

AWS_PRIVATE_MEDIA_LOCATION = 'private'
PRIVATE_FILE_STORAGE = 'rentbnb.storage_backends.PrivateMediaStorage'

# Define MEDIA_ROOT for User-uploaded files like profile pics need to be served
MEDIA_URL = 'https://s3.{}.amazonaws.com/{}/media/'.format(AWS_S3_REGION_NAME, AWS_STORAGE_BUCKET_NAME)

# Backend storage for user.profile Avatar thumbnail
AVATAR_STORAGE = 'S3'                             # 'S3': Amazon S3, 'Local': Local storage 


# Private Storage
# PRIVATE_STORAGE_ROOT = '/home/admin/files/'
# Django DBBackup
# DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
# DBBACKUP_STORAGE_OPTIONS = {'location': join(PRIVATE_STORAGE_ROOT, 'backups')}


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
        'kijiji_log_file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': join(LOGFILE_ROOT, 'kijiji.log'),
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
        },
        'kijiji': {
            'handlers': ['kijiji_log_file'],
            'level': 'DEBUG',
        }
    }
}

logging.config.dictConfig(LOGGING)
