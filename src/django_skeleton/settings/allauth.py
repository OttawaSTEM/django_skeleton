# django-allauth settings
from os.path import dirname, join, exists, abspath
from django.urls import reverse_lazy
import environ
env = environ.Env()
# Ideally move env file should be outside the git repo, i.e. BASE_DIR.parent.parent
env_file = join(dirname(__file__), 'local.env')
if exists(env_file):
    environ.Env.read_env(str(env_file))


AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of django-allauth
    'django.contrib.auth.backends.ModelBackend',

    # django-allauth specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'          # Get Errno 10013: an attempt was made to access a socket in a way forbidden by its access permissions.
# ACCOUNT_EMAIL_VERIFICATION = 'optional'
ACCOUNT_FORMS = {
    'signup': 'django_skeleton.forms.AllauthSignupForm',
    'login': 'django_skeleton.forms.AllauthLoginForm',
}
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 300
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = True
LOGIN_REDIRECT_URL = reverse_lazy('profiles:show_self')     # Redirect after sign 
# LOGIN_REDIRECT_URL = '/'        
ACCOUNT_LOGOUT_ON_GET = True                                # Logout without confirm
ACCOUNT_LOGOUT_REDIRECT_URL = reverse_lazy('home')
# LOGOUT_REDIRECT_URL = '/'
SOCIALACCOUNT_PROVIDERS = dict
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': env('GOOGLE_AUTH_CLIENT_ID'),
            'secret': env('GOOGLE_AUTH_SECRET'),
            'key': env('GOOGLE_AUTH_KEY'),
        }
    }
}