from cigo_version3.settings.base import *

DEBUG = False

ALLOWED_HOSTS = ['cigoproduction.ap-south-1.elasticbeanstalk.com', 'www.cigo.co.in', 'cigo.co.in']

STATIC_ROOT = os.path.join(BASE_DIR, 'static')



SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True


# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        # 'NAME':'CigoProdDatabase',
        'NAME':'postgres',
        'USER':'postgres',
        'PASSWORD':'rroonnyy',
        'HOST':'aa687e5wvo7evp.cjiavj7zji11.ap-south-1.rds.amazonaws.com',
        'PORT':'5432'

    }
}

AWS_ACCESS_KEY_ID = 'AKIAX3RRDD2KGR5JQSJE' 
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'cigo-bucket'

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME


AWS_S3_FILE_OVERWRITE = False

AWS_DEFAULT_ACL = None

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'


