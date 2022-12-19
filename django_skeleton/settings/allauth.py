# django-allauth settings
from .env_vars import env
from django.urls import reverse_lazy

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
ACCOUNT_LOGOUT_REDIRECT_URL = reverse_lazy('home')

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