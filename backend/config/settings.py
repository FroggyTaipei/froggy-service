"""
Django settings for froggy-service project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""
import environ
import datetime

from google.oauth2 import service_account
from django.utils.translation import ugettext_lazy as _

ROOT_DIR = environ.Path(__file__) - 2

# Load operating system environment variables and then prepare to use them
env = environ.Env()

# APP CONFIGURATION
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'django.contrib.sites',
    'suit',
    'django.contrib.admin.apps.SimpleAdminConfig',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'django_extensions',
    'ckeditor',
    'storages',
    'suit_ckeditor',
    'fsm_admin',
    'rest_framework_swagger',
    'rest_framework_jwt',
    'django_admin_lightweight_date_hierarchy',
    'date_range_filter',
    'suit_dashboard',
    'tagulous',
]

LOCAL_APPS = [
    'apps.users',
    'apps.cases',
    'apps.files',
    'apps.arranges',
    'apps.mails',
]

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# MIDDLEWARE CONFIGURATION
# ------------------------------------------------------------------------------
MIDDLEWARE = [
    'config.middlewares.HealthCheckMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# DEBUG
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool('DEBUG')
SECRET_KEY = env.str('SECRET_KEY')

# DOMAINS
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['*'])
DOMAIN = env.str('DOMAIN')

# EMAIL CONFIGURATION
# ------------------------------------------------------------------------------
EMAIL_PORT = env.int('EMAIL_PORT', default='1025')
EMAIL_HOST = env.str('EMAIL_HOST', default='mailhog')
EMAIL_HOST_USER = env.str('EMAIL_HOST_USER', default='')
SERVER_EMAIL = env.str('SERVER_EMAIL', default='')
SERVER_EMAIL_NAME = '選服魔境號'
# See: https://github.com/sendgrid/sendgrid-python
USE_SENDGRID = env.bool('USE_SENDGRID', default=False)
if USE_SENDGRID:
    # EMAIL_PORT = 587 or 2525
    EMAIL_HOST = 'smtp.sendgrid.net'
    EMAIL_HOST_PASSWORD = env.str('EMAIL_HOST_PASSWORD')
    EMAIL_USE_TLS = True
    EMAIL_BACKEND = 'sendgrid_backend.SendgridBackend'
    SENDGRID_API_KEY = env.str('SENDGRID_API_KEY')
    SENDGRID_SANDBOX_MODE_IN_DEBUG = DEBUG

# MANAGER CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = [
    ('ssivart', 'travishen.tw@gmail.com'),
    ('matt', 'fought123@gmail.com'),
    ('kai', 'ankycheng@gmail.com'),
]

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS

# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env.str('POSTGRES_DB'),
        'USER': env.str('POSTGRES_USER'),
        'PASSWORD': env.str('POSTGRES_PASSWORD'),
        'HOST': env.str('POSTGRES_HOST'),
        'PORT': 5432,
    },
}

# GENERAL CONFIGURATION
# ------------------------------------------------------------------------------
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Asia/Taipei'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'zh-hant'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True

# See: https://docs.djangoproject.com/en/2.1/topics/i18n/translation/
LOCALE_PATHS = [
    str(ROOT_DIR('locale')),
]

# See: https://docs.djangoproject.com/en/1.9/ref/settings/#date-format
DATE_FORMAT = '%Y/%m/%d'

# See: https://docs.djangoproject.com/en/1.9/ref/settings/#datetime-format
DATETIME_FORMAT = '%Y/%m/%d %H:%M'

# STATIC FILE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = str(ROOT_DIR('staticfiles'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/staticfiles/'

# See:
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [
    str(ROOT_DIR('static')),
]

# See:
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# MEDIA CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = str(ROOT_DIR('media'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'

# URL Configuration
# ------------------------------------------------------------------------------
ROOT_URLCONF = 'config.urls'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = 'config.wsgi.application'

# TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': STATICFILES_DIRS + [
            str(ROOT_DIR('templates')),
        ],
        'OPTIONS': {
            'debug': DEBUG,
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# SITE FRAMEWORK
# ------------------------------------------------------------------------------
# See https://docs.djangoproject.com/en/2.1/ref/contrib/sites/
SITE_ID = 1

# PASSWORD STORAGE SETTINGS
# ------------------------------------------------------------------------------
# See https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
]

# PASSWORD VALIDATION
# ------------------------------------------------------------------------------
# See:
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,
        },
    },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},

]

# AUTHENTICATION CONFIGURATION
# ------------------------------------------------------------------------------
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

# Custom user app defaults
# Select the correct user model
AUTH_USER_MODEL = 'users.User'

# DJANGO REST FRAMEWORK
# ------------------------------------------------------------------------------
REST_FRAMEWORK = {
    'UPLOADED_FILES_USE_URL': False,
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.FileUploadParser',
    ],
}

# RAVEN SENTRY CLIENT
# ------------------------------------------------------------------------------
# See https://docs.sentry.io/clients/python/integrations/django/
INSTALLED_APPS += ['raven.contrib.django.raven_compat']
RAVEN_MIDDLEWARE = [
    'raven.contrib.django.raven_compat.middleware.SentryResponseErrorIdMiddleware']
MIDDLEWARE = RAVEN_MIDDLEWARE + MIDDLEWARE

# Sentry Configuration
# ------------------------------------------------------------------------------
SENTRY_DSN = env.str('SENTRY_DSN')
SENTRY_CLIENT = 'raven.contrib.django.raven_compat.DjangoClient'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
                      '%(process)d %(thread)d %(message)s',
        },
    },
    'handlers': {
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'django.security.DisallowedHost': {
            'level': 'ERROR',
            'handlers': ['console', 'sentry'],
            'propagate': False,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}

RAVEN_CONFIG = {
    'DSN': SENTRY_DSN,
}

# INITIAL DATA
# ------------------------------------------------------------------------------
# See https://docs.djangoproject.com/en/2.1/howto/initial-data/
FIXTURE_DIRS = (
    str(ROOT_DIR('fixtures')),
    str(ROOT_DIR('fixtures/cases')),
    str(ROOT_DIR('fixtures/arranges')),
    str(ROOT_DIR('fixtures/mails')),
    str(ROOT_DIR('fixtures/auth')),
)

# Cloud Storage
# ------------------------------------------------------------------------------
USE_GCS = env.bool('USE_GCS', default=False)
if USE_GCS:
    STATICFILES_STORAGE = 'apps.files.storages.GoogleCloudStaticStorage'
    DEFAULT_FILE_STORAGE = 'apps.files.storages.GoogleCloudMediaStorage'
    GS_PROJECT_ID = env.str('GS_PROJECT_ID')
    GS_BUCKET_NAME = env.str('GS_BUCKET_NAME')

    GS_MEDIA_BUCKET_NAME = f'{GS_BUCKET_NAME}-media'
    GS_STATIC_BUCKET_NAME = f'{GS_BUCKET_NAME}-staticfiles'
    MEDIA_URL = f'https://{GS_MEDIA_BUCKET_NAME}.storage.googleapis.com/'
    STATIC_URL = f'https://{GS_STATIC_BUCKET_NAME}.storage.googleapis.com/'
    GS_AUTO_CREATE_BUCKET = True

    GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
        f"{ROOT_DIR}/{env.str('GS_CREDENTIALS')}",
    )


# DJANGO SUIT
# ------------------------------------------------------------------------------
SUIT_CONFIG = {
    'ADMIN_NAME': _("Froggy's Service"),
    'SEARCH_URL': '/admin/cases/case/',
    'HEADER_DATE_FORMAT': 'l, Y F j',
    'HEADER_TIME_FORMAT': 'H:i',
    'LIST_PER_PAGE': 30,
    'CONFIRM_UNSAVED_CHANGES': True,
    'MENU_EXCLUDE': ('sites',),
}

# FILES LIMIT
# ------------------------------------------------------------------------------
FILE_LIMIT_CASE = 5
FILE_LIMIT_PER_FILE = 10485760
FILE_LIMIT_PER_CASE = 52428800
FILE_LIMIT_PER_DAY = 524288000

# JWT
# ------------------------------------------------------------------------------
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=1800),
}
