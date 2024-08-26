"""
Django StudentV4BE 项目的设置。

通过使用 Django 3.0.14 的 'django-admin startproject' 生成。

有关此文件的更多信息，请参见
https://docs.djangoproject.com/en/3.0/topics/settings/

有关所有设置及其值的完整列表，请参见
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os, sys
from pathlib import Path

# 构建项目内路径，例如：BASE_DIR / "subdir"。
BASE_DIR = Path(__file__).resolve().parent.parent
# 为了让程序可以不只是在根目录查找，还查找指定目录
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# 快速启动开发设置 - 不适用于生产
# 详见 https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# 安全警告：在生产中保持用于生产的秘密密钥！
SECRET_KEY = 'e_$7=pplr33wg_)4q6+9)qu7v@0@1@sh09z4oxm#3+k40e4p6k'

# 安全警告：在生产中不要启用调试！
DEBUG = True

ALLOWED_HOSTS = ['192.168.138.129']  # 通过其他电脑连接时需要输入当前后端ip地址
# python manage.py runserver 192.168.138.129:8000


# 应用程序定义

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'student',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'StudentV4BE.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR.joinpath('templates'))],
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

WSGI_APPLICATION = 'StudentV4BE.wsgi.application'

# 数据库
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'StudentV4DB',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

# 密码验证
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

# 国际化
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# 静态文件（CSS、JavaScript、图像）
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
#设置上传文件的目录和外部访问路径
MEDIA_ROOT=os.path.join(BASE_DIR,'media/')
MEDIA_URL='/media/'
# 凡是出现在白名单的域名都可以访问后端接口
CORS_ALLOW_CREDENTIALS = True  # 指明在跨域访问中，后端是否支持对cookie的操作。
CORS_ALLOWED_ORIGINS = [  # 前端ip
    "http://192.168.56.1:5500",
    # 这里设置你的Vue.js应用的地址
]
