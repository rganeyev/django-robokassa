#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.management import call_command
from django.conf import settings
import django


if django.VERSION < (1, 7):
    installed_apps = ('robokassa', 'south',)
else:
    installed_apps = ('robokassa',)

settings.configure(
    INSTALLED_APPS=installed_apps,
    DATABASE_ENGINE='sqlite3',
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3'
        }
    },

    ROBOKASSA_LOGIN='test_login',
    ROBOKASSA_PASSWORD1='test_password',
    ROBOKASSA_PASSWORD2='test_password2',
    ROBOKASSA_EXTRA_PARAMS=['param1', 'param2'],
)

if hasattr(django, 'setup'):
    django.setup()

if __name__ == "__main__":
    call_command('test', 'robokassa')
