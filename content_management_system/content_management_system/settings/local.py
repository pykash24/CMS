from .base import *
import os
from dotenv import load_dotenv
load_dotenv()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('NEW_DB_NAME'),
        'USER': os.getenv('NEW_DB_USER'),
        'PASSWORD': os.getenv('NEW_DB_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '3306',
    }
}