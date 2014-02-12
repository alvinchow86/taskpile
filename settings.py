# Django settings for taskmaster project.
import userconfig

import os, sys
ROOT_PATH = os.path.dirname(__file__)
sys.path.append(ROOT_PATH)

DEBUG = getattr(userconfig, 'DEBUG', False)
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = getattr(userconfig, 'DATABASE_ENGINE', 'mysql')           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = getattr(userconfig, 'DATABASE_NAME', 'taskmaster')            # Or path to database file if using sqlite3.
DATABASE_USER = getattr(userconfig, 'DATABASE_USER', 'django')             # Not used with sqlite3.
DATABASE_PASSWORD = getattr(userconfig, 'DATABASE_PASSWORD', 'r31nh@rdt')         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
#MEDIA_ROOT = os.path.join(ROOT_PATH, 'media')
MEDIA_ROOT = getattr(userconfig, 'MEDIA_ROOT', '/home/bankingzen/www/media/tasks/public/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = getattr(userconfig, 'MEDIA_URL', "/media/tasks/public/")

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = getattr(userconfig, 'ADMIN_MEDIA_PREFIX', '/media/tasks/admin/')

# Make this unique, and don't share it with anybody.
SECRET_KEY = '-b)(093*n)u4ai-p(0rqvcsr1pq4$r119p2=7c9j#2$u@)*x_-'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
   
)

ROOT_URLCONF = 'taskmaster.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(ROOT_PATH, 'taskpile/templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'taskmaster.extra_context.global_settings', )

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'taskpile',
)

# Root project URL (e.g. '/'. or '/tasks/')
ROOT_URL = getattr(userconfig, 'ROOT_URL', '/')
LOGIN_URL = ROOT_URL + 'login/'
LOGIN_REDIRECT_URL = ROOT_URL

#LOGIN_URL = getattr(userconfig, 'LOGIN_URL', '/login/')
#LOGIN_REDIRECT_URL = getattr(userconfig, 'LOGIN_REDIRECT_URL', '/')

AUTH_PROFILE_MODULE = 'taskpile.UserProfile'

