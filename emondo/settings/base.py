"""
Django settings for emondo project.

Generated by 'django-admin startproject' using Django 1.9.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from kombu import (
    Exchange,
    Queue,
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Will be override by local_settings
SECRET_KEY = 'vo!1)2*mv*zt58kl_5smk6mv4a30l7vjqg6%s8($70)w_am!&t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


RAVEN_CONFIG = {
    'dsn': 'https://5564545ed6d441e3a26a613a9c772c3e:bc234b3c419d4132a5e0237b2f6b3274@app.getsentry.com/72730',
    # If you are using git, you can also automatically configure the
    # release based on the git info.
    # 'release': raven.fetch_git_sha(os.path.dirname(__file__)),
}


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'raven.contrib.django.raven_compat',
    'storages',
    'feincms',
    'mptt',
    'cms',
    'cms.blog',
    'rest_framework',
    'core',
    'public_sitemaps',
    'hotjar',
    'intercom',
    'compressor',
    'data_explorer',
    'webpack_loader',
    'notifications',
    'google_analytics',
    'letsencrypt',
    'gunicorn',
    'accounts',
    'public',
    'docs',
]


LIBCLOUD_PROVIDERS = {
    'google': {
        'type': 'libcloud.storage.types.Provider.GOOGLE_STORAGE',
        'user': '<your_key>',
        'key': '<secret>',
        'bucket': 'emondo-media',
    },
}

DEFAULT_LIBCLOUD_PROVIDER = 'google'

DEFAULT_FILE_STORAGE = 'storages.backends.apache_libcloud.LibCloudStorage'

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'emondo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'emondo.wsgi.application'


REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    )
}



# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Australia/Sydney'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
)

COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter'
]


STATIC_ROOT = os.path.join(BASE_DIR, 'dist')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
WHITENOISE_MAX_AGE = 3600 * 24 * 30


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
                      '%(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            'level': 'ERROR', # To capture more than ERROR, change to WARNING, INFO, etc.
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
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
    },
}


WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': not DEBUG,
        'BUNDLE_DIR_NAME': 'bundles/', # must end with slash
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),
        'POLL_INTERVAL': 0.1,
        'IGNORE': ['.+\.hot-update.js', '.+\.map']
    }
}

AUTH_USER_MODEL = 'accounts.User'




# Celery


## Broker settings.
# transport://userid:password@hostname:port/virtual_host
BROKER_URL = 'amqp://guest:guest@localhost:5672//'

# Might be RAM limited https://rpm.newrelic.com/accounts/333738/servers/2434660
CELERYD_CONCURRENCY = 4
CELERYD_MAX_TASKS_PER_CHILD = 500 # Periodically restart workers
CELERYD_TASK_TIME_LIMIT = 80 # Hard limit
CELERYD_TASK_SOFT_TIME_LIMIT = 60


# By default we will route to the 'default' queue where we can't find a
# match in our CELERY_ROUTES
CELERY_DEFAULT_QUEUE = "default"
CELERY_DEFAULT_EXCHANGE = "emondo"
CELERY_DEFAULT_EXCHANGE_TYPE = "direct"
CELERY_DEFAULT_ROUTING_KEY = "default"


CELERY_QUEUES = (
    Queue('default', Exchange('emondo'), routing_key='default'),
    Queue('high', Exchange('emondo'), routing_key='high_priority'),
)

# CELERY_ROUTES = {
#     'my_taskA': {'queue': 'for_task_A', 'routing_key': 'for_task_A'}
# }


# Save one thread as we don't use this feature
CELERY_DISABLE_RATE_LIMITS = True

# Stop Celery from trying to overwrite our LOGGING configuration!
# See: https://github.com/celery/celery/issues/1867
CELERYD_HIJACK_ROOT_LOGGER = False
CELERY_REDIRECT_STDOUTS = False


CELERY_ACCEPT_CONTENT = ['json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'



## Using the database to store task state and results.
# sqlite (filename)
CELERY_RESULT_BACKEND = 'db+sqlite:///celery-results.sqlite'
CELERY_IGNORE_RESULT = True

CELERY_TIMEZONE = 'Australia/Sydney'

CELERY_TRACK_STARTED = True
CELERY_SEND_EVENTS = True


PLIVO_AUTH_ID = ''
PLIVO_TOKEN = ''

STATIC_URL = 'http://127.0.0.1:8000/static/'

FEINCMS_RICHTEXT_INIT_TEMPLATE = 'admin/content/richtext/init_ckeditor.html'

FEINCMS_RICHTEXT_INIT_CONTEXT = {
    'CKEDITOR_JS_URL': STATIC_URL + 'javascripts/ckeditor/ckeditor.js'
}

FEINCMS_UPLOAD_PREFIX = 'cms'
FEINCMS_MEDIALIBRARY_UPLOAD_TO = 'uploads'
