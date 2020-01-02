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
    '.zonsondergangconcert.nl',
]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.fastmail.com'
EMAIL_HOST_USER = os.environ.get('EMAIL_USERNAME')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True

MEDIA_ROOT = '/media/codingartist'

try:
    from .local import *
except ImportError:
    pass
