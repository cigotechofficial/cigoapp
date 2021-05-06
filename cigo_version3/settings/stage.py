from cigo_version3.settings.base import *

DEBUG = True

ALLOWED_HOSTS = ['cigostaging.ap-south-1.elasticbeanstalk.com']

STATIC_ROOT = os.path.join(BASE_DIR, 'static')



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