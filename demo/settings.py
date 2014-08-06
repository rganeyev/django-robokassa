"""
Django settings for demo project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import site

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
path = lambda *a: os.path.join(os.path.dirname(os.path.abspath(__file__)), *a)

site.addsitedir(path('../'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@4u(fq!&e933p_7wfw85i*_gh01hc)c(0y1=&jwdsucay5-574'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'robokassa',
    'demo',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_URL = '/admin/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

"""
URLs:
    Result Url: http://127.0.0.1:8000/robokassa/result/
    Success Url: http://127.0.0.1:8000/robokassa/success/
    Fail Url: http://127.0.0.1:8000/robokassa/fail/
"""
ROBOKASSA_LOGIN = 'development-test'
ROBOKASSA_PASSWORD1 = 'DzwXYqkc1'
ROBOKASSA_PASSWORD2 = 'CHWdTxND2'

ROBOKASSA_USE_POST = False
ROBOKASSA_STRICT_CHECK = False
ROBOKASSA_TEST_MODE = True

# ROBOKASSA_EXTRA_PARAMS = ['UserId', 'SiteId']

try:
    from local_settings import *
except ImportError:
    pass
