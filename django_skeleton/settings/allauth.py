from django.urls import reverse_lazy
from .env_vars import env

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of django-allauth
    'django.contrib.auth.backends.ModelBackend',

    # django-allauth specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
DEFAULT_FROM_EMAIL = "info@django.com"
# Get Errno 10013: an attempt was made to access a socket in a way forbidden by its access permissions.
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'        # 'mandatory' or 'optional'
# django-allauth > 65.2.0, conflict with dj-rest-auth 7.0.1
# ACCOUNT_LOGIN_METHODS = {'email'}
# ACCOUNT_SIGNUP_FIELDS = ['email*', 'username*', 'password1*', 'password2*']

ACCOUNT_FORMS = {
    'signup': 'django_skeleton.forms.AllauthSignupForm',
    'login': 'django_skeleton.forms.AllauthSigninForm',
}
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = True
LOGIN_REDIRECT_URL = reverse_lazy('profiles:show_self')     # Redirect after sign in
# LOGIN_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_REDIRECT_URL = reverse_lazy('home')

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': env('GOOGLE_AUTH_CLIENT_ID'),
            'secret': env('GOOGLE_AUTH_SECRET'),
            'key': env('GOOGLE_AUTH_KEY'),
        }
    }
}
