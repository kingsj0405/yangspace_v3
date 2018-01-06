from .base import *

DEBUG = False

ALLOWED_HOSTS = ['yangspace.co.kr']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'name',
        'USER': 'user',
        'PASSWORD': 'password'
    }
}
