from cigo_version3.settings.base import *

DEBUG = False

ALLOWED_HOSTS = ['cigoprod.ap-south-1.elasticbeanstalk.com', 'www.cigo.co.in', 'cigo.co.in']

STATIC_ROOT = os.path.join(BASE_DIR, 'static')



# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# SECURE_SSL_REDIRECT = True


# # SESSION_COOKIE_SECURE = True
# # CSRF_COOKIE_SECURE = True

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         # 'NAME':'CigoProdDatabase',
#         'NAME':'postgres',
#         'USER':'postgres',
#         'PASSWORD':'rroonnyy',
#         'HOST':'aa687e5wvo7evp.cjiavj7zji11.ap-south-1.rds.amazonaws.com',
#         'PORT':'5432'

#     }
# }
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	}
}