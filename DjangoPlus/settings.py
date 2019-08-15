"""
Django settings for DjangoPlus project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8qp@7ko#54)m(&b$8-qs7)myo*ma$fh2sd15q(r&jb7a347dd1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DJANGO_LOG_LEVEL = DEBUG  # 这样可以看到Django的所以调试日志，这将会很冗长，因为它包含了所有的数据库查询记录

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'xadmin',
    'crispy_forms',
    'rest_framework',
    'debug_toolbar',
    'demo',
    'polls',
    # 'video_editing_software'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'DjangoPlus.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'DjangoPlus.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

# Celery settings
from kombu import Queue, Exchange

CELERY_CONFIG_DETAIL_DICT = dict(
    CELERY_BROKER_URL='pyamqp://guest@localhost//',  # 代理人的网址
    CELERY_ACCEPT_CONTENT=['pickle', 'json', 'msgpack', 'yaml'],  # 指定任务接受的内容序列化类型(序列化)
    # CELERY_RESULT_BACKEND='db+sqlite:///results.sqlite',  # 结果存储地址
    # CELERY_RESULT_SERIALIZER='json',  # 结果存储序列化格式为 json
    CELERYD_TASK_TIME_LIMIT=60,  # 任务超出5秒将被kill
    CELERYD_PREFETCH_MULTIPLIER=4,  # 每次预取４个
    CELERYD_FORCE_EXECV=True,  # 防止死锁
    CELERYD_MAX_TASKS_PER_CHILD=500,  # 每个worker最多执行500次个任务就会被释放掉, 可防止内存泄露
    CELERY_DISABLE_RATE_LIMITS=True,  # 关闭限速
    CELERY_TASK_SERIALIZER='json',  # 任务序列化方式

    CELERY_QUEUES=(
        Queue('default', Exchange('default'), routing_key='default', exchange_type="topic"),
        Queue('big_task', Exchange('big_task'), routing_key='big_task', exchange_type="topic"),
        # 路由键以 task. 开头的消息进入此队列
        Queue('small_task', Exchange('small_task'), routing_key='small_task', exchange_type="topic")
    ),
    CELERY_DEFAULT_QUEUE='default',  # 默认队列
    CELERY_DEFAULT_EXCHANGE='default',  # 默认交换所
    CELERY_DEFAULT_EXCHANGE_TYPE='topic',  # 默认交换所
    CELERY_DEFAULT_ROUTING_KEY='default'  # 默认交换机路由键
)

# log configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            # 它输出日志级别、日志消息，以及时间、进程、线程和生成日志消息的模块。
            'style': '{',
        },
        'simple': {
            'format': '{asctime} {module} {levelname} {message}',
            # 它只输出日志的级别（例如，DEBUG）和日志消息。
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        # 'file': {
        #     'level': 'DEBUG',
        #     'class': 'logging.FileHandler',
        #     'filename': '/Users/zhangkun/Documents/GitHub/DjangoPlus/DjangoPlus.log',
        # },
        'request': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/Users/zhangkun/Documents/GitHub/DjangoPlus/DjangoPlus_Request.log',
            'encoding': 'utf8',
        },
        'db': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/Users/zhangkun/Documents/GitHub/DjangoPlus/DjangoPlus_Db.log',
            'encoding': 'utf8',
        },
        'error': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': '/Users/zhangkun/Documents/GitHub/DjangoPlus/DjangoPlus_Error.log',
            'encoding': 'utf8',
            # 'filters': ['require_debug_true'],
        },
    },
    'loggers': {
        # django 是一个捕获所有信息的logger。消息不会直接提交给这个logger。
        # 'django': {
        #     'level': 'DEBUG',
        #     'handlers': ['file'],
        # },
        # 记录与处理请求相关的消息。5XX 响应作为ERROR 消息；4XX 响应作为WARNING 消息。
        'django.request': {
            'level': 'DEBUG',
            'handlers': ['request'],
        },
        # Log messages related to the handling of requests received by the server invoked by the runserver command. HTTP 5XX responses are logged as ERROR messages, 4XX responses are logged as WARNING messages, and everything else is logged as INFO.
        'django.server': {
            'level': 'DEBUG',
            'handlers': ['request'],
        },
        # 与数据库交互的代码相关的消息。例如，HTTP请求执行应用级别的SQL 语句将以DEBUG 级别记录到该logger。
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['db'],
        },
        'error_log': {
            'handlers': ['error'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}

# email configuration
# 可以本地 python -m smtpd -n -c DebuggingServer localhost:1025 开一个邮件服务器测试用
EMAIL_HOST = '127.0.0.1'
EMAIL_PORT = 1025
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''

# cache
# 使用文件系统缓存确保文件夹的读写权限正常
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
#         'LOCATION': '/var/tmp/django_cache',
#         'TIMEOUT': 30,
#         'OPTIONS': {
#             'MAX_ENTRIES': 1000,
#             'CULL_FREQUENCY': 2,
#         },
#         'KEY_PREFIX': 'DjangoPlus_cache',
#         'VERSION': 1,
#
#     }
# }

# 使用redis缓存
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379',
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
             # "PASSWORD": "yoursecret",
        },
    },
}


REDIS_TIMEOUT=7*24*60*60
CUBES_REDIS_TIMEOUT=60*60
NEVER_REDIS_TIMEOUT=365*24*60*60

# debug toolbar
INTERNAL_IPS = ['127.0.0.1', ]

MEDIA_ROOT = os.path.join(BASE_DIR,'media_file') # 作为Django存储上传文件的路径(从性能上考虑，这些文件不能存在数据库中。)
MEDIA_URL = 'media_file/'