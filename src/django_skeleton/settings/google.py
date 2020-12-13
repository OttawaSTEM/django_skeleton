# Google reCAPTCHA & Google Analytics
from os.path import dirname, join, exists, abspath
import environ

env = environ.Env()
# Ideally move env file should be outside the git repo, i.e. BASE_DIR.parent.parent
env_file = join(dirname(__file__), 'local.env')
if exists(env_file):
    environ.Env.read_env(str(env_file))
    
RECAPTCHA_PUBLIC_KEY = env('RECAPTCHA_SITE_KEY')
RECAPTCHA_PRIVATE_KEY  = env('RECAPTCHA_SECRET_KEY')

GOOGLE_ANALYTICS_TRACKING_ID = env('GOOGLE_ANALYTICS_TRACKING_ID')

