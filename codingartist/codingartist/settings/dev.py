from __future__ import absolute_import, unicode_literals

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

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


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$_1v=t)iy^z++27@od=2srl&y8%7d$blw56fuqtjqobucf=12y'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
COMPRESS_ENABLED = True

try:
    from .local import *
except ImportError:
    pass
