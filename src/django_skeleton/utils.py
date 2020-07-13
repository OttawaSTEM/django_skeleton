from django.conf import settings
from django.core.mail import EmailMessage

import logging
logger = logging.getLogger('project')

def SendEmail(from_email, subject, body, to=None, files=None):
    try:
        email = EmailMessage(
            subject='{} - From {}'.format(subject, from_email),
            body=body,
            from_email=settings.FROM_EMAIL,
            # from_email=from_email,
            to=[settings.WEBMASTER_1, settings.WEBMASTER_2],
            bcc=None
        )
        email.send(fail_silently=False) 
    except Exception as e:
        logger.info('SendEmail Error: {} - '.format(e, subject))
        email = EmailMessage(
            subject='{} - From {}'.format(subject, from_email),
            body=body,
             from_email=settings.FROM_EMAIL,
            # from_email=from_email,
            to=[settings.WEBMASTER_1, settings.WEBMASTER_2],
            bcc=None
        )
        email.send(fail_silently=False) 