from cigo_version3.settings.base import *

DEBUG = True

ALLOWED_HOSTS = ['cigostaging.ap-south-1.elasticbeanstalk.com']

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
