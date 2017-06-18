from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = config('DEBUG')

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

SECRET_KEY = config('SECRET_KEY')

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}


try:
    from .local import *
except ImportError:
    pass
