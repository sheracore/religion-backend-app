# import docker as docker_engine
# from celery import Celery
# from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

from application.config import Config


db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()
jwt = JWTManager()
# cors = CORS(resources={r"/api/*": {"origins": "*"}})
# celery = Celery(__name__, broker=Config.CELERY_BROKER_URL,
#                 result_backend=Config.CELERY_RESULT_BACKEND)
# docker = docker_engine.from_env()
