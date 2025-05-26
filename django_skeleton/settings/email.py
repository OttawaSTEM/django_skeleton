from .env_vars import env

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

WEBMASTERS = eval(env("WEBMASTERS"))
