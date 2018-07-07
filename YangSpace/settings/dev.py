from .base import *

# Dummy secret key for travis-ci
# Use script from following gist link
# https://gist.github.com/kingsj0405/74c9e1aa4ac5425beadfd4bb10981725
SECRET_KEY = '`m%&UP_RpZzG&c9k=GDOg}Rrx?#M7p&udg$WaKb!Mgd,E4VH)_'

DEBUG = True

# For mobile access
ALLOWED_HOSTS += ['192.168.%s.%s' % (i, j)
                  for i in range(256) for j in range(256)]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
