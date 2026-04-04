import os
from pathlib import Path

import environ
from split_settings.tools import include

# Пути проекта
BASE_DIR = Path(__file__).resolve().parent.parent

# Енвы
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

# Импорт настроек
base_settings = [
    "components/auth.py",
    "components/database.py",
    "components/bolt.py",
]

include(*base_settings)

# Секрет проекта
SECRET_KEY = env.str("SECRET_KEY")

# Дебаг режим
DEBUG = env.bool("DEBUG", default=False)

# Разрешенные хосты
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["*"])

# Приложения
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "apps.best_pc_builds",
    "apps.users",
    "apps.components",
    "django_bolt",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "apps.best_pc_builds.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
            *[BASE_DIR / "apps" / app / "templates" for app in INSTALLED_APPS if app.startswith("apps.")],
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "apps.best_pc_builds.wsgi.application"
ASGI_APPLICATION = "apps.best_pc_builds.asgi.application"
SITE_ID = 1

# Локализация
LANGUAGE_CODE = "ru"

TIME_ZONE = "Europe/Moscow"

USE_I18N = True

USE_L10N = False

USE_TZ = False

DATE_FORMAT = "Y-m-d"

DATETIME_FORMAT = "Y-m-d H:i"

# Статические файлы (CSS, JavaScript, Images)
STATIC_URL = "/static/"
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
STATICFILES_DIR = os.path.join(BASE_DIR, "static")
STATIC_ROOT = os.path.join(BASE_DIR, "static")

# CSRF
CSRF_COOKIE_SECURE = False
CSRF_TRUSTED_ORIGINS = env.list(var="CSRF_TRUSTED_ORIGINS", default=["http://127.0.0.1:8000"])
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
