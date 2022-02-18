# """
# # Django settings for cigo_version3 project.

# Generated by 'django-admin startproject' using Django 2.1.5.

# For more information on this file, see
# https://docs.djangoproject.com/en/2.1/topics/settings/

# For the full list of settings and their values, see
# https://docs.djangoproject.com/en/2.1/ref/settings/
# """

# import os
# from django.contrib.messages import constants as messages

# # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# # Quick-start development settings - unsuitable for production
# # See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = '97quixm#*05p9d5f(w%11f96nutg82dw*+lgdn)bfp$3xi@@oh'

# # SECURITY WARNING: don't run with debug turned on in production!
# # DEBUG = True


# ALLOWED_HOSTS = ['cigostaging.ap-south-1.elasticbeanstalk.com','cigoproduction.ap-south-1.elasticbeanstalk.com', 'www.cigo.co.in', 'cigo.co.in']

# # ALLOWED_HOSTS = ['*']


# # Application definition

# INSTALLED_APPS = [
# 	'qr_code',
# 	'accounts.apps.AccountsConfig',
# 	'setup.apps.SetupConfig',
# 	'home.apps.HomeConfig',
# 	'dashboard.apps.DashboardConfig',
# 	'help.apps.HelpConfig',
# 	'app_eordering.apps.App_eorderingConfig',
# 	'django.contrib.admin',
# 	'django.contrib.auth',
# 	'django.contrib.contenttypes',
# 	'django.contrib.sessions',
# 	'django.contrib.messages',
# 	'django.contrib.staticfiles',

# 	'django.contrib.sites',
 
# 	'allauth',
# 	'allauth.account', 
# 	'allauth.socialaccount', 
# 	'allauth.socialaccount.providers.google',

# 	'storages',

# 	'onlymenuapp.apps.OnlymenuappConfig',
# ]

# SITE_ID = 2
# LOGIN_REDIRECT_URL = '/customerapp/redirect'


# MIDDLEWARE = [
# 	'django.middleware.security.SecurityMiddleware',
# 	'django.contrib.sessions.middleware.SessionMiddleware',
# 	'django.middleware.common.CommonMiddleware',
# 	'django.middleware.csrf.CsrfViewMiddleware',
# 	'django.contrib.auth.middleware.AuthenticationMiddleware',
# 	'django.contrib.messages.middleware.MessageMiddleware',
# 	'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]

# ROOT_URLCONF = 'cigo_version3.urls'

# TEMPLATES = [
# 	{
# 		'BACKEND': 'django.template.backends.django.DjangoTemplates',
# 		'DIRS': ['templates'],
# 		'APP_DIRS': True,
# 		'OPTIONS': {
# 			'context_processors': [
# 				'django.template.context_processors.debug',
# 				'django.template.context_processors.request',
# 				'django.contrib.auth.context_processors.auth',
# 				'django.contrib.messages.context_processors.messages',
# 			],
# 		},
# 	},
# ]

# WSGI_APPLICATION = 'cigo_version3.wsgi.application'


# # Database
# # https://docs.djangoproject.com/en/2.1/ref/settings/#databases

# # DATABASES = {
# # 	'default': {
# # 		'ENGINE': 'django.db.backends.sqlite3',
# # 		'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
# # 	}
# # }

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

# # Password validation
# # https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
# 	{
# 		'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
# 	},
# 	{
# 		'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
# 	},
# 	{
# 		'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
# 	},
# 	{
# 		'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
# 	},
# ]


# # Internationalization
# # https://docs.djangoproject.com/en/2.1/topics/i18n/

# LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'

# USE_I18N = True

# USE_L10N = True

# USE_TZ = True


# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/2.1/howto/static-files/

# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# # STATICFILES_DIRS = [
# #     os.path.join(BASE_DIR, "static"),
# # ]

# # Managing media
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# MEDIA_URL = '/media/'

# MESSAGE_TAGS = {
# 	messages.ERROR: 'danger'
# }

# AUTHENTICATION_BACKENDS = (
#  'django.contrib.auth.backends.ModelBackend',
#  'allauth.account.auth_backends.AuthenticationBackend',
#  )

# # ---------------------------for https ----------------------------------------
# # if os.getcwd() == '/app':
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# SECURE_SSL_REDIRECT = True
# DEBUG = False


# AWS_ACCESS_KEY_ID = 'AKIA4KY24AYIV3KBBJCE'
# AWS_SECRET_ACCESS_KEY = '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'
# AWS_STORAGE_BUCKET_NAME = 'cigo-bucket'

# AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME


# AWS_S3_FILE_OVERWRITE = False

# AWS_DEFAULT_ACL = None

# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# # STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'