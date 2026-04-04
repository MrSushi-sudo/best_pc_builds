"""Настройки базы данных"""
from config.settings import env

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': env('POSTGRES_DB_HOST', default=''),
        'NAME': env('POSTGRES_DB'),
        'USER': env('POSTGRES_DB_USER'),
        'PASSWORD': env('POSTGRES_DB_PASSWORD'),
        'PORT': env.int('POSTGRES_DB_PORT', default=''),
    }
}
