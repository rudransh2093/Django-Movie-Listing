import dj_database_url
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-q32*t6sqmw+dg-kr%-e0n#1sbe_!_8yy#+eonak-9zw(f1(e%n'

DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition
INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',  # Added Django Storages
    'movies',
    'user',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = '1movies.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = '1movies.wsgi.application'

# Database
DATABASES = {
    'default': dj_database_url.config(default="postgresql://postgres.aerkffomdjbghaeigbsf:rudu0508@aws-0-us-west-1.pooler.supabase.com:5432/postgres")
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# **Use Supabase Storage for media files**
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
AWS_ACCESS_KEY_ID = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFlcmtmZm9tZGpiZ2hhZWlnYnNmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Mzk5OTA4MzUsImV4cCI6MjA1NTU2NjgzNX0.WwGoRB5lCr7qf5daeAaYo1QGXAVJ3xS7P2R1XeZ8a2M"
AWS_SECRET_ACCESS_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFlcmtmZm9tZGpiZ2hhZWlnYnNmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Mzk5OTA4MzUsImV4cCI6MjA1NTU2NjgzNX0.WwGoRB5lCr7qf5daeAaYo1QGXAVJ3xS7P2R1XeZ8a2M"
AWS_STORAGE_BUCKET_NAME = "movie-images"
AWS_S3_ENDPOINT_URL = "https://xyz.supabase.co/storage/v1"
AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.xyz.supabase.co"
MEDIA_URL = f"{AWS_S3_CUSTOM_DOMAIN}/"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
