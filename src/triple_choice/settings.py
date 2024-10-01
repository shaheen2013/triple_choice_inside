# Django settings for triple_choice project.

# Generated by 'django-admin startproject' using Django 3.2.9.

# For more information on this file, see
# https://docs.djangoproject.com/en/3.2/topics/settings/

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--q_8buj7+%g4l-fqc94mmd8@mcaz)71iw3usd22wnr-_icphl0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # Set this to True for development mode

APP_SITE_HEADER = os.environ.get('APP_SITE_HEADER', 'TripleChoice')
APP_SITE_TITLE = os.environ.get('APP_SITE_TITLE', 'TripeChoice Admin Portal')
APP_INDEX_TITLE = os.environ.get('APP_INDEX_TITLE', 'Welcome to TripeChoice Admin Portal')

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = os.environ.get('DEBUG', "False").lower() in ('true', 1, 't')

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(' ')

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'django_userforeignkey',
    'rest_framework',
    'django_filters',
    'django_q',
    'tinymce',
    'utils',
    'product',
    'order',
    'authentication',
    'customer',
    'supplier',
    'page'
    # 'djstripe'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'triple_choice.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'page.context_processors.website',
            ],
        },
    },
]

WSGI_APPLICATION = 'triple_choice.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# Original Database Configuration
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.' + os.environ.get('DB_ENGINE', 'mysql'),
#         'NAME': os.environ.get('DB_NAME', 'triple_choice'),
#         'USER': os.environ.get('DB_USERNAME', 'root'),
#         'PASSWORD': os.environ.get('DB_PASSWORD', 'Pashandi2015$'),
#         'HOST': os.environ.get('DB_HOST', 'localhost'),
#         'PORT': os.environ.get('DB_PORT', '3306'),
#     }
# }

# Updated Database Configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'triple_choice',
        'USER': 'root',  # Using root user
        'PASSWORD': 'Pashandi2015$',  # Ensure this is correct
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ]
}

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = os.environ.get('TIME_ZONE')

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = f"/{os.environ.get('STATIC_URL')}/"

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

MEDIA_ROOT = os.path.join(BASE_DIR, os.environ.get('MEDIA_URL', 'media'))

MEDIA_URL = f"/{os.environ.get('MEDIA_URL')}/"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_HOST = os.environ.get('EMAIL_HOST', 'smtp.mailtrap.io')
EMAIL_PORT = os.environ.get('EMAIL_PORT', '2525')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '3cbeeb733c4823')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '08e12dfe03b00f')
EMAIL_USE_TLS = True
EMAIL_BACKEND = os.environ.get("EMAIL_BACKEND", 'django.core.mail.backends.smtp.EmailBackend')

DEC_LOADER = "my.package.custom_email_domain_loader"
BDEA_TIMEOUT = 2

AUTH_USER_MODEL = 'authentication.User'

Q_CLUSTER = {
    'name': 'DjangORM',
    'workers': 4,
    'timeout': 90,
    'retry': 120,
    'queue_limit': 50,
    'bulk': 10,
    'orm': 'default'
}

# stripe setup
STRIPE_SECRET_KEY = os.environ.get("STRIPE_SECRET_KEY",
                                   "sk_test_51KH0gmCEoJrUUHndM5h6g67Q1XiN4lR47mLi51VePW8MErsFLmMzL7mbVi26wgblbeynBGrSsiYMEK7WweIsHaGe00dqtbtY5u")

TINYMCE_DEFAULT_CONFIG = {
    "height": "320px",
    "width": "960px",
    "menubar": "file edit view insert format tools table help",
    "plugins": "advlist autolink lists link image charmap print preview anchor searchreplace visualblocks code "
               "fullscreen insertdatetime media table paste code help wordcount spellchecker",
    "toolbar": "undo redo | bold italic underline strikethrough | fontselect fontsizeselect formatselect | alignleft "
               "aligncenter alignright alignjustify | outdent indent |  numlist bullist checklist | forecolor "
               "backcolor casechange permanentpen formatpainter removeformat | pagebreak | charmap emoticons | "
               "fullscreen  preview save print | insertfile image media pageembed template link anchor codesample | "
               "a11ycheck ltr rtl | showcomments addcomment code",
    "custom_undo_redo_levels": 10,
}