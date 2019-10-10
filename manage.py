import json
from datetime import datetime

import requests
from flask_script import Manager
from flask_migrate import MigrateCommand

from application.app import create_app
from application.extensions import db
# from models.scanner import Scanner
from models.user import User
# from models.setting import Setting


app = create_app('application.config.DeploymentConfig')
manager = Manager(app)


# @manager.command
# def sync():
#     """
#     Check status of scanners and remove unnecessary ones
#     """
#     scanners = Scanner.query.all()
#     for scanner in scanners:
#         try:
#             url = 'http://' + scanner.ip + ':8080/api/v1/status/agent/'
#             resp = requests.get(url)

#             scanner.checked_at = datetime.utcnow()

#             if resp.status_code != 200:
#                 db.session.delete(scanner)

#         except requests.exceptions.ConnectionError:
#             db.session.delete(scanner)

#     db.session.commit()
#     print("Sync done.")


@manager.command
def create_user(username, password):
    user = User(username=username)
    user.hashed_password = user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    print("Added user")


# @manager.command
# def create_setting():
#     settings = Setting.query.all()
#     for setting in settings:
#         db.session.delete(setting)

#     with open('settings.json') as json_data:
#         setting = Setting(data=json.load(json_data))
#         db.session.add(setting)

#     db.session.commit()
#     print("Added setting")


manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
