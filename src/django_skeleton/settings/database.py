# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

from os.path import dirname, join, exists, abspath
from django.urls import reverse_lazy
import environ
env = environ.Env()
# Ideally move env file should be outside the git repo, i.e. BASE_DIR.parent.parent
env_file = join(dirname(__file__), 'local.env')
if exists(env_file):
    environ.Env.read_env(str(env_file))


DATABASES = {
    # Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
    'default': env.db()
}