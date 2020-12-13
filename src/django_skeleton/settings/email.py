# django-allauth settings
from os.path import dirname, join, exists, abspath
import environ

env = environ.Env()
# Ideally move env file should be outside the git repo, i.e. BASE_DIR.parent.parent
env_file = join(dirname(__file__), 'local.env')
if exists(env_file):
    environ.Env.read_env(str(env_file))

# Email Server Settings
EMAIL_CONFIG = env.email_url('EMAIL_URL', default='consolemail://')
if 'smtp' in EMAIL_CONFIG['EMAIL_BACKEND']:
    EMAIL_USE_TLS = EMAIL_CONFIG['EMAIL_USE_TLS']
    EMAIL_HOST = EMAIL_CONFIG['EMAIL_HOST']
    EMAIL_PORT = EMAIL_CONFIG['EMAIL_PORT']
    EMAIL_HOST_USER = EMAIL_CONFIG['EMAIL_HOST_USER']
    EMAIL_HOST_PASSWORD = EMAIL_CONFIG['EMAIL_HOST_PASSWORD']
else:
    # For developing, email sent to console
    # Commen local.env "EMAIL_URL" to use console Email backend
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'     

WEBMASTER_1 = env('WEBMASTER_1')
WEBMASTER_2 = env('WEBMASTER_2')
