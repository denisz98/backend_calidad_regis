from .base import*
from decouple import config

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#ALLOWED_HOSTS = ['*']
#CSRF_TRUSTED_ORIGINS = ['https://proyecto-calidad-backend.onrender.com']

# ALLOWED_HOSTS = [config('HOST_BACKEND'), config('HOST_FRONTEND')]

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),

    }
}

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

