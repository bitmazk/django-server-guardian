"""Settings that need to be set in order to run the tests."""
import os


DEBUG = True
SITE_ID = 1

APP_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..'))

DJANGO_PROJECT_ROOT = os.path.join(APP_ROOT, '..')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

ROOT_URLCONF = 'server_guardian.tests.urls'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(APP_ROOT, '../app_static')
MEDIA_ROOT = os.path.join(APP_ROOT, '../app_media')
STATICFILES_DIRS = (
    os.path.join(APP_ROOT, 'static'),
)

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'APP_DIRS': True,
    'DIRS': [os.path.join(APP_ROOT, 'tests/test_app/templates')],
    'OPTIONS': {
        'context_processors': (
            'django.contrib.auth.context_processors.auth',
            'django.template.context_processors.request',
        )
    }
}]

EXTERNAL_APPS = [
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites',
]

INTERNAL_APPS = [
    'server_guardian',
    'server_guardian_api',
    'server_guardian.tests.test_app',
]

SERVER_GUARDIAN_SECURITY_TOKEN = 'foobar'

LOGIN_URL = 'admin/login/'

LOCKFILE_FOLDER = os.path.join(APP_ROOT, '../lockfile')

INSTALLED_APPS = EXTERNAL_APPS + INTERNAL_APPS

MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

SECRET_KEY = 'foobar'

FROM_EMAIL = 'foobar@example.com'
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'

ADMINS = (
    ('Fooman Barster', 'fooman.barster@example.com'),
)
