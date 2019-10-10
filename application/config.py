import os
from datetime import timedelta


class Config(object):
    """
    Default Configuration
    """
    SECRET_KEY = os.environ.get('SECRET_KEY', 'ASDASDOWIQ!@&EQHC<XNYWGYW#!@')

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'SQLALCHEMY_DATABASE_URI', 'postgres://admin:islamic9251@localhost/religion')

    # UPLOAD_DIR = os.environ.get('UPLOAD_DIR', '/tmp/')

    # AGENT_URL = 'http://{}:8080/api/v1/{}/scan/'

    INSTALLED_APPS = [
        'user',
        # 'result',
        # 'report',
        # 'user',
        # 'setting',
    ]

    # CELERY_BROKER_URL = os.environ.get(
    #     'CELERY_BROKER_URL', 'redis://localhost:6379/0')
    # CELERY_RESULT_BACKEND = os.environ.get(
    #     'CELERY_RESULT_BACKEND', 'db+postgresql://multiscanner:U&r5fE$8@localhost/multiscanner')

    # MAX_DOWNLOAD_SIZE = 100 * 1024 * 1024  # 100 MB

    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=24)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=7)
    JWT_HEADER_TYPE = 'JWT'


class DevelopmentConfig(Config):
    """
    Development Configuration
    """
    DEBUG = True


class DeploymentConfig(Config):
    """
    Deployment Confugartion
    """
    DEBUG = False
