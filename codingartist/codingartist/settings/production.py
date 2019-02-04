from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/databases/coding_artist/db.sqlite3',
    }
}

SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    '.thecodingartist.nl',
    '.thecodingartist.com',
    '.photonicmusic.nl',
    '.photonicorchestra.com',
    '.photonicorchestra.nl',
    '.photonicorchestra.eu',
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MEDIA_ROOT = '/media/codingartist'

try:
    from .local import *
except ImportError:
    pass
