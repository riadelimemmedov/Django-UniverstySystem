from pathlib import Path
import os
from decouple import config


from django.utils.translation import gettext_lazy as _

#!Your everywhere service name
SITE_NAME = "" #Domain Name

#!Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

#!App Name
APP_NAME = "ADMIN" #Default Admin

#!SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')


#!Application definition
DEFAULT_APPS = [
    'jet.dashboard',
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

#!Third Part App
THIRD_PARTY_APPS = [
    'django_cleanup',
    'multiselectfield'
]

#!Created Apps
CREATED_APPS = [
    'abstract',
    'account'
]  

#!Installed Apps
INSTALLED_APPS = DEFAULT_APPS + CREATED_APPS + THIRD_PARTY_APPS


#!Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

#!Root UrlConf
ROOT_URLCONF = 'config.urls'

#!Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

#!Wsgi Application
WSGI_APPLICATION = 'config.wsgi.application'

AUTH_USER_MODEL = 'account.Account'

#!Auth Password Validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

#!Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/
LANGUAGE_CODE = "az"

LANGUAGES = [
    ("az", _("Azerbaijani")),
    ("en", _("English")),
    ("ru", _("Russian")),
]
TIME_ZONE = 'Asia/Baku'
USE_I18N = True #A boolean that specifies whether Django's translation system should be enabled
USE_L10N = True #Numbers and dates using the format of the current locale.
USE_TZ = True

DATE_INPUT_FORMATS = ['%m-%d-%Y']


#!Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATIC_URL = 'static/'


#!Default Auto Field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


#!Static Files
ENVIRONMENT = config('ENVIRONMENT')
if ENVIRONMENT == 'LOCAL':
    STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]
else:#if site deployed to production
    STATIC_ROOT = os.path.join(BASE_DIR,'static')#for production

#!MediuUrl and MediaRoot
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR,'media')


#!Jet Themes
JET_DEFAULT_THEME = 'light-violet'


#Create requirements.txt file
#python -m pip freeze
#pip freeze > requirements.txt