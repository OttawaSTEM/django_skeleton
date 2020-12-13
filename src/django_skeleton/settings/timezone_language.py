# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/
from os.path import dirname, join, exists, abspath
from django.utils.translation import gettext_lazy as _
from os.path import dirname, join, exists, abspath

BASE_DIR = dirname(dirname(dirname(abspath(__file__))))

# Default data format: 2000-02-18
USE_L10N = True
USE_I18N = True
USE_TZ = True
TIME_ZONE = 'America/Toronto'

# Language
LOCALE_PATHS = (join(BASE_DIR, 'locale'),)
LANGUAGE_CODE = 'en'
LANGUAGES = (
    ('en', _('English')),
    ('fr', _('French')),
    ('zh-hans', _('Simplified Chinese')),
)
