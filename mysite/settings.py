# -*- coding: utf-8 -*-
'''AWS動作確認用アプリ'''

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


PROJECT_NAME = os.path.basename(BASE_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x5nbaoq1tsoe^l86s48&sms@pc97qb1xn)=w2r9d(4xu(8qq@u'


DEBUG = True

ALLOWED_HOSTS = ['*']                           # 全てのホストからのアクセスを許容


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap4',                               # Bootstrap4(CSSフレームワーク)利用
    'shop',                                     # 開発アプリを記述←アプリをDjangoFW側に認識させるため
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],                      # テンプレート参照設定
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

WSGI_APPLICATION = 'mysite.wsgi.application'


# DB設定
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'testdb',                                                   # RDS作成時に設定した「最初のデータベース名」に合わせる→RDSにアクセスしなくて済む
        'USER': 'testuser',                                                 # AWSで設定したDBユーザ用
        'PASSWORD': 'testpassword',                                         # PWもRDSで設定したものに変更
        'HOST': 'test1.cfoy0i3ytiui.ap-northeast-1.rds.amazonaws.com',      # RDSのエンドポイントを設定
        'PORT': '3306',
    }
}



# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

# 以下追加4
# staticファイル系設定
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = '/var/www/{}/static' .format(PROJECT_NAME)

# セッション設定
SESSION_COOKIE_AGE = 600 # 10分
SESSION_SAVE_EVERY_REQUEST = True # 1リクエストごとにセッション情報を更新

