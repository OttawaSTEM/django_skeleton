REST_FRAMEWORK = {
    # Disable Web Browsable API render of django-rest-framework
    # 'DEFAULT_RENDERER_CLASSES': (
    #     'rest_framework.renderers.JSONRenderer',
    # ),
    # Use Django's standard `django.contrib.auth` permissions, or allow read-only access for unauthenticated users.
    "DEFAULT_PERMISSION_CLASSES": [
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
        # 'rest_framework.permissions.IsAdminUser',
        # 'rest_framework.permissions.IsAuthenticated',
        # 'rest_framework.permissions.AllowAny',
    ],
    # REST API
    "DEFAULT_AUTHENTICATION_CLASSES": [
        # Enables simple CLI authentication
        # 'rest_framework.authentication.BasicAuthentication',
        "rest_framework.authentication.TokenAuthentication",
        # 'rest_framework.authentication.SessionAuthentication',
    ],
    # Pagination to control how many objects per page are returned
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # 'PAGE_SIZE': 10
}

# REST_AUTH_CALLBACK_URL = '/api/auth/login/callback'
REST_AUTH_GOOGLE_CALLBACK_URL = "/api/auth/google/callback"
