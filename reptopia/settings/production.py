# 실서버 설정
import json
import os
from .base import *

ROOT_DIR = os.path.dirname(BASE_DIR)
CONFIG_SECRET_DIR = os.path.join(ROOT_DIR, '.config_secret')
CONFIG_SETTINGS_COMMON_FILE = os.path.join(CONFIG_SECRET_DIR, 'settings_common.json')

config_secret = json.loads(open(CONFIG_SETTINGS_COMMON_FILE).read())

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config_secret['production']['SECRET_KEY']


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/
ALLOWED_HOSTS = [
    '.ap-northeast-2.compute.amazonaws.com',
    '.reptopia.kr',
    '15.164.125.252',
]


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    'default': config_secret['production']['DATABASES']['default']
}


EMAIL_HOST_PASSWORD = config_secret['production']['EMAIL_PASSWORD']
