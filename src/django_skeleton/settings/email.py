# django-allauth settings
from os.path import dirname, join, exists, abspath
import environ

env = environ.Env()
# Ideally move env file should be outside the git repo, i.e. BASE_DIR.parent.parent
env_file = join(dirname(__file__), 'local.env')
if exists(env_file):
    environ.Env.read_env(str(env_file))

WEBMASTER_1 = env('WEBMASTER_1')
WEBMASTER_2 = env('WEBMASTER_2')
