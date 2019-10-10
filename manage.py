import json
from datetime import datetime

import requests
from flask_script import Manager
from flask_migrate import MigrateCommand

from application.app import create_app
from application.extensions import db
from models.user import User



app = create_app('application.config.DeploymentConfig')
manager = Manager(app)



@manager.command
def get_user():
    u=User.query.all()
    print(u)

@manager.command
def create_user(username, password):
    user = User(username=username)
    user.hashed_password = user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    print("Added user")




@manager.command
def create_db():
    """Create Database"""
    db.create_all()


@manager.command
def drop_db():
    """Drop Database"""
    db.drop_all()



if __name__ == '__main__':
    manager.run()
