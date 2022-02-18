from cigo_version3.settings.base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	}
}

# AWS_ACCESS_KEY_ID = 'AKIA4KY24AYIV3KBBJCE'
# AWS_SECRET_ACCESS_KEY = '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'
# AWS_STORAGE_BUCKET_NAME = 'cigo-bucket'

# AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME


# AWS_S3_FILE_OVERWRITE = False

# AWS_DEFAULT_ACL = None

# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# # STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'
