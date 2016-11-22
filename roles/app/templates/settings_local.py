# -*- coding:utf-8 -*-
from default import *

ADMINS = (
    ('admin', 'admin@dummy-domain.com'),
)

MANAGERS = ADMINS

DEBUG = False
TEMPLATE_DEBUG = DEBUG
COMPRESS_ENABLED = True

MEDIA_URL = '/media/'
MEDIA_PATH = '{{ app_media_path }}'

STATIC_URL = '/static/'
STATIC_PATH = '{{ app_static_path }}'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '{{ database_name }}',
        'USER': '{{ database_user }}',
        'PASSWORD': '{{ database_pass }}',
        'HOST': '{{ groups['db'][0] }}',
        'PORT': 3306,
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '{{ groups['cache'][0] }}:11211',
    }
}
