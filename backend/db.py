import os
from dotenv import load_dotenv

import environ

env = environ.Env()
environ.Env.read_env()

#Carga las variables de entorno
load_dotenv()

POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DATABASE_BD'),
        'USER': os.getenv('DATABASE_USER'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),
        'HOST': os.getenv('DATABASE_SERVER'),
        'PORT': os.getenv('DATABASE_PORT'),
    }
}