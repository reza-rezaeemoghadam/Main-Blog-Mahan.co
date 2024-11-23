"""
Django settings for src project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import os
import environ
from pathlib import Path
from datetime import timedelta
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Initialize environment variables
env = environ.Env()

# Read .env file
env.read_env(os.path.join(BASE_DIR,'.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', default=False)


ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])


# Application definition

INSTALLED_APPS = [
    # django built-in apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # custom apps
    'blog',
    'user',
    
    # third-party apps
    'rest_framework',           # REST framework
    "rest_framework_simplejwt", # JWT authentication
    'drf_yasg',                 # Swagger documentation
    'parler',                   # Django parler for multilingual support
    "corsheaders",              # CORS middleware
    "django_ckeditor_5"         # Django CKEditor RichText editor
]

MIDDLEWARE = [
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',             # Internationalization purpose
    'corsheaders.middleware.CorsMiddleware',                 # CORS middleware
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'src.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'temlpates'],
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

WSGI_APPLICATION = 'src.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': str(env('DB_NAME')),
        'USER': str(env('DB_USER')),
        'PASSWORD': str(env('DB_PASSWORD')),
        'HOST': str(env('DB_HOST')),   
        'PORT': str(env('DB_PORT')),
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = (
    ('en', _('English')),
    ('fa', _('Farsi')),
)

PARLER_LANGUAGES = {
    None: (
        {'code': 'en',}, # English
        {'code': 'fa',}, # Farsi
    ),
    'default': {
        'fallbacks': ['en'],
        'hide_untranslated': False,
    }
}

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/'),
]
STATIC_URL = '/static/'

# Medua files (Images, Videos, etc.)
MEDIA_ROOT = 'media/'
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Rest framework configuration

# Swagger configuration
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization',
            'description': 'JWT Authorization header using the Bearer scheme. Example: "Authorization: Bearer {token}"'
        }
    }
}

# JWT configuration
SIMPLE_JWT = {'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5), 
              'REFRESH_TOKEN_LIFETIME': timedelta(days=1), 
              'ROTATE_REFRESH_TOKENS': True, 
              'BLACKLIST_AFTER_ROTATION': True, 
              'ALGORITHM': 'HS256', 
              'SIGNING_KEY': SECRET_KEY, 
              'VERIFYING_KEY': None, 
              'AUTH_HEADER_TYPES': ('Bearer',), 
              'USER_ID_FIELD': 'id', 
              'USER_ID_CLAIM': 'user_id', 
              'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',), 
              'TOKEN_TYPE_CLAIM': 'token_type', 
}

# CORS configuration
CORS_ALLOWED_ORIGINS = []


# Ckeditor configuration
CKEDITOR_5_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage' 
CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': [
            'heading', '|', 'bold', 'italic', 'link', 'bulletedList', 'numberedList', 'blockQuote', 'imageUpload', 'fontSize', 'fontFamily', 'fontColor'
        ],
        'font': {
            'options': [
                'Arial', 'Times New Roman', 'Georgia', 'Courier New', 'Verdana'
            ]
        },
        'fontSize': {
            'options': [
                'small', 'normal', 'big', 'huge'
            ]
        },
        'fontColor': {
            'options': [
                'black', 'red', 'green', 'blue', 'yellow', 'purple', 'orange', 'pink'
            ]
        }
    }
}
