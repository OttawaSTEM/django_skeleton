from django.conf import settings
from django.core import mail

import logging
logger = logging.getLogger('project')

def SendEmail(subject, body, to=None, files=None):
    try:
        connection = mail.get_connection()
        connection.open()
        email = mail.EmailMessage(
            subject='{} - From {}'.format(subject, settings.EMAIL_HOST_USER),
            body=body,
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.EMAIL_WEBMASTER_1, settings.EMAIL_WEBMASTER_2],
            bcc=None,
            connection=connection,
        )
        email.send(fail_silently=False) 
    except Exception as e:
        logger.info('SendEmail Error: {} - '.format(e, subject))
        connection = mail.get_connection()
        connection.open()
        email = mail.EmailMessage(
            subject='{} - From {}'.format(subject, settings.EMAIL_HOST_USER),
            body=body,
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.EMAIL_WEBMASTER_1, settings.EMAIL_WEBMASTER_2],
            bcc=None,
            connection=connection,
        )
        email.send(fail_silently=False) 