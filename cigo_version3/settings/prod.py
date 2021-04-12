from cigo_version3.settings.base import *

DEBUG = False

ALLOWED_HOSTS = ['cigoproduction.ap-south-1.elasticbeanstalk.com', 'www.cigo.co.in', 'cigo.co.in']

STATIC_ROOT = os.path.join(BASE_DIR, 'static')



SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True