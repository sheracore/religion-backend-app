from werkzeug.security import generate_password_hash
from models.video import Video
from models.sound import Sound
from models.book import Book
from models.device import Device
from application.extensions import db, ma


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    hashed_password = db.Column(db.String(512), unique=True, nullable=False)
    videos = db.relationship('Video', backref='user',cascade="all, delete-orphan",lazy=True)
    sounds = db.relationship('Sound', backref='user',cascade="all, delete-orphan",lazy=True)
    books = db.relationship('Book', backref='user',cascade="all, delete-orphan",lazy=True)

    def __repr__(self):
        return self.username

    def hash_password(self, password):
        return generate_password_hash(password)


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
