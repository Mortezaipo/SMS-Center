# Django settings for ws project.
import os
DEBUG = True

SERVICE_URL = 'http://127.0.0.1:8000/api/wsdl'
SERVICE_USERNAME = 'username'
SERVICE_PASSWORD = 'password'
SERVICE_ID = 'free'

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'test',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'root',
        'PASSWORD': '136',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Make this unique, and don't share it with anybody.
SECRET_KEY = '^0er&7nna17+@+v1-e$t!j$y=yr1+ue+kleifumu_89@8&+l%o'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ws.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'ws.wsgi.application'


WEB_SERVICE = {
    "connect": {
        "url" : SERVICE_URL,
        "argv" : (SERVICE_USERNAME,SERVICE_PASSWORD), # order is too important!
    },
    "step1": {
        "service" : "Login",
        "argv" : (SERVICE_USERNAME,SERVICE_PASSWORD), # order is too important!
    },
    "step2": {
        "service" : "SendMessage",
        "argv" : (SERVICE_USERNAME,SERVICE_PASSWORD,'{message}','{mobile}',SERVICE_ID),  # order is too important! {} are just for message and mobile!!!
    },
}