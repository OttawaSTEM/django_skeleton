"""
ASGI config for deployment and production.

It exposes the ASGI callable as a module-level variable named ``application``.
For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/asgi/
"""
import os

if os.environ.get('DJANGO_ENVIRONMENT') == 'Development':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_skeleton.settings.development')
elif os.environ.get('DJANGO_ENVIRONMENT') == 'VirtualMachine':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_skeleton.settings.virtualmachine')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_skeleton.settings.container')

from django.core.asgi import get_asgi_application
application = get_asgi_application()
