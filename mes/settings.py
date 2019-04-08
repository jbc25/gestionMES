"""
Django settings for vicci project.

Generated by 'django-admin startproject' using Django 1.11.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from django.utils.translation import gettext as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = os.path.abspath(os.path.join(BASE_DIR, os.pardir))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'uzekt30thl4&hw)p@c#ht=b8mn!3l080kmnuk7ez+g5l%lb*p9'
AUTH_USER_MODEL = 'core.User'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'accounts',
    'simple_bpm',
    'management',
    'payments',
    'core',
    'currency',
    'jet',
    'sermepa',
    'django_filters',
    'ckeditor',
    'qrcode',
    'sass_processor',
    'polymorphic',
    'localflavor',
    'imagekit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'core.middleware.LoginRequiredMiddleware',
]

ROOT_URLCONF = 'mes.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ os.path.join(BASE_DIR, 'templates') ],
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

WSGI_APPLICATION = 'mes.wsgi.application'

MEMBER_CONSUMER = 'consumidora'
MEMBER_COLAB = 'colaboradora'
MEMBER_PROV = 'proveedora'
MEMBER_TYPES = (
    (MEMBER_CONSUMER, 'Socia consumidora'),
    (MEMBER_COLAB, 'Socia colaboradora'),
    (MEMBER_PROV, 'Socia proveedora'),
)



# Jet admin configs

JET_SIDE_MENU_COMPACT = True
JET_CHANGE_FORM_SIBLING_LINKS = False
JET_SIDE_MENU_ITEMS = [  # A list of application or custom item dicts
    {'label': 'General', 'items': [
        {'name': 'core.user'},
    ]},
    {'label': 'Seguridad', 'items': [
        {'name': 'auth.group'},
        {'name': 'auth.permission'},
    ]},
]
JET_THEMES = [
    {
        'theme': 'mes',
        'color': '#cf821c',
        'title': 'MES'
    }
]

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = False
SITE_ID = 1

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]
STATIC_ROOT = ROOT_DIR + '/static'
MEDIA_ROOT = ROOT_DIR + '/media'
MEDIA_URL = '/media/'
STATIC_URL = '/static/'
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_REDIRECT_URL = '/'

LOGIN_EXEMPT_URLS = [
    r'^accounts/signup/provider/',
    r'^accounts/signup/success/',
    r'^accounts/signup/consumer/',
    r'^api/*',
    r'^pay/*',
    r'^payments/pay/*',
    r'^payments/end/*',
    r'^invite/[0-9a-zA-Z\-]+/',
    r'^password_reset/*',
    r'^reset/*',
]

INLINE_INPUT_SEPARATOR = '&&&'

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'sass_processor.finders.CssFinder',
]

TASTYPIE_DEFAULT_FORMATS = ['json']

EMAIL_SEND_FROM = 'noreply@mercadosocial.net'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'width':'100%',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline', 'Format', 'FontSize','TextColor', 'BGColor'],
            ['NumberedList', 'BulletedList', '-',  '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', 'Link', 'Unlink'],
        ]
    },
}

# Import secret settings (see settings_secret.py.template for reference)
from settings_secret import *