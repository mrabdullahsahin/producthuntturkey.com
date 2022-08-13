from .settings import *
import environ

env = environ.Env()
environ.Env.read_env()

DEBUG = False

ALLOWED_HOSTS = ['www.producthuntturkey.com','producthuntturkey.com']

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env("DATABASE_PROJECT_NAME"),
        'USER': env("DATABASE_USER_NAME"),
        'PASSWORD': env("DATABASE_PASSWORD"),
        'HOST': 'localhost',
        'PORT': '',
    }
}