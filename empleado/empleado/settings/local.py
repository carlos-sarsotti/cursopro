
from .base import *
#from .db import MYSQL
import os
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
#DATABASES = MYSQL
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': str(os.path.join(BASE_DIR , 'db.sqlite3')),
#    }
#}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
         'NAME': 'dbempleado',
         'USER': 'sarsoc',
         'PASSWORD':'1v72c9123',
         'HOST': 'localhost',
         'PORT':'5432',

    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
#STATICFILES_DIRS = ["C:/Users/pc1/Documents/cursopro/empleado/static"]
#STATICFILES_DIRS = [BASE_DIR.child("static")]
#MEDIA_URL='/media/'
#MEDIA_ROOT =['C:/Users/pc1/Documents/cursopro/empleado/media']
STATICFILES_DIRS = [BASE_DIR / 'static'] # carpeta base static

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media' # carpeta base media