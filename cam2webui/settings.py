"""
Django settings for herokudemo project.
Generated by 'django-admin startproject' using Django 1.10.4.
For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/
"""
import os, sys, dj_database_url, re
import configparser
from pathlib import Path

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
BASE_DIR =  os.path.dirname(PROJECT_ROOT)

# Get Environment Variables from .env
my_env = os.environ.copy()
parser = configparser.ConfigParser({k: v.replace('$', '$$') for k, v in os.environ.items()},
         interpolation=configparser.ExtendedInterpolation())
def defaultSect(fp): yield '[DEFAULT]\n'; yield from fp
settingsFile = os.path.join(BASE_DIR, ".env")
if os.path.isfile(settingsFile):
    with open(settingsFile) as stream:
        parser.read_file(defaultSect(stream))
        for k, v in parser["DEFAULT"].items():
            my_env.setdefault(k.upper(), v)

# Environment Variables Import
try:
    # Does the site runs on production site or tested locally
    IS_PRODUCTION_SITE = bool(my_env['IS_PRODUCTION_SITE'] == "True")
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = my_env['DJANGO_SECRET_KEY']
    # Database URLS
    DATABASE_URL = my_env["DATABASE_URL"]
    # Recaptcha Keys
    GOOGLE_RECAPTCHA_SECRET_KEY = my_env['RECAPTCHA_PRIVATE_KEY']
    # Development Site Protection
    if not IS_PRODUCTION_SITE:
        BASICAUTH_USERNAME = my_env['BASICAUTH_USERNAME']
        BASICAUTH_PASSWORD = my_env['BASICAUTH_PASSWORD']
    # Github Auth
    SOCIAL_AUTH_GITHUB_KEY = my_env['GITHUB_KEY']
    SOCIAL_AUTH_GITHUB_SECRET = my_env['GITHUB_SECRET']
    # Google API KEY and Auth
    GOOGLE_API_KEY = my_env['GOOGLE_API_KEY']
    SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = my_env['GOOGLE_LOGIN_KEY']
    SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = my_env['GOOGLE_LOGIN_SECRET']
    # Email Smtp Settings
    EMAIL_HOST = my_env['EMAIL_HOST']
    EMAIL_PORT = my_env['EMAIL_PORT']
    EMAIL_HOST_USER = my_env['EMAIL_HOST_USER']
    EMAIL_HOST_PASSWORD = my_env['EMAIL_HOST_PASSWORD']
    MANAGER_EMAIL = my_env['MANAGER_EMAIL']
    if 'test' in sys.argv:
        RECAPTCHA_SITE_KEY = my_env['RECAPTCHA_TEST_SITE_KEY']
    else:
        RECAPTCHA_SITE_KEY = my_env['RECAPTCHA_SITE_KEY']
except KeyError as e:
    print('Lacking Environment Variables: ' + str(e))
    print('Visit https://purduecam2project.github.io/CAM2WebUI/basicSetup/localsite.html#exporting-config-vars for details')
    exit()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = not IS_PRODUCTION_SITE

# Defines which sites are allowed to display the site
ALLOWED_HOSTS = [
    'www.cam2project.net',
    'cam2webui.herokuapp.com',
    'cam2webui-staging.herokuapp.com',
    'cam2webui-stream.herokuapp.com',
    'localhost',
    '127.0.0.1',
]

# Receive error log
# use IGNORABLE_404_URLS to ignore error logs being sent to admin email
ADMINS = [('cam2proj', MANAGER_EMAIL)]

# Receive user feedback - manager email in environment

#ignore 404 error to be sent to admin email
#documented in https://docs.djangoproject.com/en/2.0/howto/error-reporting/
IGNORABLE_404_URLS = [
    re.compile(r'^/favicon\.ico$'),
    re.compile(r'^/robots\.txt$'),
    re.compile(r'^/&amp/'),

]

# Application definition
INSTALLED_APPS = [
	'admin_view_permission',
    'django.contrib.auth',
    'social_django',
    'app',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
    'email_system',
]

# Middleware definition
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
    'detect.middleware.UserAgentDetectionMiddleware',
]
# Basic auth
# https://djangosnippets.org/snippets/2468/

if not IS_PRODUCTION_SITE:
    MIDDLEWARE.extend(['app.middleware.basicauth.BasicAuthMiddleware'])

ROOT_URLCONF = __package__+'.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
STATIC_URL = '/static/'
# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'app/static/app'),
    os.path.join(BASE_DIR, 'email_system/static/email_system'),
)
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
WSGI_APPLICATION = __package__+'.wsgi.application'

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
    }
}


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
# Update database configuration with $DATABASE_URL.

if len(sys.argv) > 1 and sys.argv[1] == 'test':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    DATABASES = {
        'default': dj_database_url.parse(DATABASE_URL, conn_max_age=600)
    }


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/1.10/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Django social authentication
# http://python-social-auth.readthedocs.io/en/latest/configuration/
AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'index'

SOCIAL_AUTH_LOGIN_ERROR_URL = '/register/'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/oauthinfo/'
SOCIAL_AUTH_RAISE_EXCEPTIONS = False

#Email system
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' if IS_PRODUCTION_SITE \
                else 'django.core.mail.backends.console.EmailBackend'
EMAIL_USE_SSL = True
SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# Release settings
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https') if IS_PRODUCTION_SITE else None
SECURE_BROWSER_XSS_FILTER = IS_PRODUCTION_SITE
SECURE_SSL_REDIRECT = IS_PRODUCTION_SITE
