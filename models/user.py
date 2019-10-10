from werkzeug.security import generate_password_hash
from sqlalchemy.dialects.postgresql import JSON

from application.extensions import jwt, db, ma
# from models.scanner import Scan, File


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    hashed_password = db.Column(db.String(512), unique=True, nullable=False)

    def __repr__(self):
        return self.username

    def hash_password(self, password):
        return generate_password_hash(password)

class UserSchema(ma.ModelSchema):
    # role = ma.Nested('RoleSchema', many=False, exclude=['users'])

    class Meta:
        model = User
        exclude = ['hashed_password']
