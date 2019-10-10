import importlib
import logging
import logging.config

from flask import Flask

from application.extensions import db, ma, migrate,jwt


def create_app(config_filename):
    """
    Flask application factory

    :param config_filename: Config to use
    :returns: Flask app instance
    """
    app = Flask(__name__)
    app.config.from_object(config_filename)

    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    # logging.config.fileConfig('application/logging.config')
   # logging.getLogger('sysLogLogger').critical('critical message')

    for installed_app in app.config['INSTALLED_APPS']:
        view = importlib.import_module('views.{}'.format(installed_app))
        app.register_blueprint(view.blueprint)

    # get_config_args(app)

    return app


# def get_config_args(app):
#     """
#     set config param from setting database 
#     """
#     # TODO :solve problem of start management
#     with app.app_context():
#         try:
#             setting = Setting.query.first()
#             if setting:
#                 app.config['SETTING'] = Setting.query.first().data
#         except:
#             pass


# @task_prerun.connect
# def on_task_init(*args, **kwargs):
#     """
#     Handle multiprocessing in sqlalchemy
#     """
#     db.engine.dispose()
