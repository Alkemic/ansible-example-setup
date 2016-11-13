# -*- coding:utf-8 -*-
"""
Installation specific settings.
Copy this file to settings_local.py, and fill up.
"""
from settings import PROJECT_NAME

ADMINS = (
    ('admin', 'admin@dummy-domain.com'),
)

MANAGERS = ADMINS

LOCAL_MIDDLEWARE_CLASSES = ()

LOCAL_INSTALLED_APPS = ()

MEDIA_URL = '/media/'
STATIC_URL = '/static/'

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

GOOGLE_SITE_VERIFICATION = ''

ALLOWED_HOSTS = ['*']

DEBUG = False
TEMPLATE_DEBUG = DEBUG

IS_WIP = False
