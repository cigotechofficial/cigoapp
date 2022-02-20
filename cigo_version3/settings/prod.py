from cigo_version3.settings.base import *

DEBUG = True

ALLOWED_HOSTS = ['cigo-env.eba-steer7fa.ap-south-1.elasticbeanstalk.com','cigoprod.ap-south-1.elasticbeanstalk.com', 'www.cigo.co.in', 'cigo.co.in']

STATIC_ROOT = os.path.join(BASE_DIR, 'static')



# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# SECURE_SSL_REDIRECT = True
SECURE_SSL_REDIRECT = False


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

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         # 'NAME':'CigoProdDatabase',
#         'NAME':'cigoproduction_database',
#         'HOST':'database-cigo.cckg5toxqpnf.ap-south-1.rds.amazonaws.com',
#         'USER':'cigo_ryan',
#         'PASSWORD':'cigo_2022',
#         'PORT':'3306',

#     }
# }

AWS_ACCESS_KEY_ID = 'AKIAX3RRDD2KLDJMSWL4' 
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'cigo-statics'

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME


AWS_S3_FILE_OVERWRITE = False

AWS_DEFAULT_ACL = None

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'


