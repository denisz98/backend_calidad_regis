from datetime import timedelta
from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-f9naf=1($zukwi&ve*(g@l_v5!c2etmtebp-5g(^yd@*65_4!m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True




# Application definition

BASE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
LOCAL_APPS = [
    'apps.user',
    'apps.carreras',

]
THIRD_APPS = [
  'rest_framework',
   "corsheaders",
  'rest_framework_simplejwt',
  'rest_framework_simplejwt.token_blacklist',  

  'simple_history',
  'drf_yasg',
]

INSTALLED_APPS = BASE_APPS + LOCAL_APPS + THIRD_APPS

    
SWAGGER_SETTINGS = {
    'USE_SESSION_AUTH': True, 
    'DOC_EXPANSION': 'none',
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header',
        },
    },
}
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
        #'rest_framework.permissions.IsAuthenticated',
    ],
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

CORS_ORIGIN_WHITELIST = [
    config('HOST_FRONTEND'),
    config('HOST_BACKEND'),
]
# CORS_ALLOWED_ORIGINS = [
# # config('HOST_FRONTEND'),
# # config('HOST_BACKEND'),
# 'http://localhost:3000',
# 'http://localhost:8000',
# 'http://proyecto-calidad-frontend.onrender.com',
# 'http://proyecto-calidad-backend.onrender.com',
# 'https://proyecto-calidad-frontend.onrender.com',
# 'https://proyecto-calidad-backend.onrender.com'

# ]
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
)
ROOT_URLCONF = 'SEA_Carrera_API.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'SEA_Carrera_API.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'es-ue'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
AUTH_USER_MODEL = 'user.User'
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=10),
    'REFRESH_TOKEN_LIFETIME': timedelta(minutes=30),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True
}

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CSRF_TRUSTED_ORIGINS = ["http://localhost:8000"]