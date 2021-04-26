"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import dj_database_url
# Build paths inside the project like this: BASE_DIR / 'subdir'.
import sys

sys.modules['django.utils.six.moves.urllib.parse'] = __import__('six.moves.urllib_parse', fromlist=['urlencode'])
sys.modules['django.utils.six.moves.urllib.request'] = __import__('six.moves.urllib_request', fromlist=['urlopen'])

BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2(uy1d5cnvn!8^yh7-@&g6(leguuus5(fkn+i6w-5i6!nq7jy('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'photo',
    'accounts',
    'disqus',
    'django.contrib.sites',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # 추가
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
DATABASES['default'].update(dj_database_url.config(conn_max_age=500))

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / "media"  # django 3.x

AUTH_USER_MODEL = 'photo.User'

LOGIN_REDIRECT_URL = '/'

DISQUS_WEBSITE_SHORTNAME = 'dstagram-jjw'  # Disqus 사이트에 작성한 이름을 써야함
SITE_ID = 1  # sites 앱에 등록된 현재 사이트의 번호, 기본적으로 1번으로 설정

AWS_ACCESS_KEY_ID = 'AKIAXCXC4GTOY4GNEU6E'
AWS_SECRET_ACCESS_KEY = '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'
AWS_REGION = 'ap-northeast-2'
AWS_STORAGE_BUCKET_NAME = 'dstagram-jungjw'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.%s.amazonaws.com' % (AWS_STORAGE_BUCKET_NAME, AWS_REGION)
AWS_S3_FILE_OVERWRITE = False  # 같은 이름 파일이 있는 경우 덮어 쓸지 설정
# 파일 받아갔을 때 cache를 얼마나 유지할 것인지 설정
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_DEFAULT_ACL = 'public-read'  # 이렇게 설정하지 않으면 외부 접근이 안되서 못보는 경우가 생김
AWS_LOCATION = 'static'

# STATIC_URL = '/static/' --> 위에 정의되 있던 것을 아래 코드로 변경
STATIC_URL = 'http://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

DEFAULT_FILE_STORAGE = 'config.asset_storage.MediaStorage'

STATIC_ROOT = [BASE_DIR / 'staticfiles']  # django 3.x
