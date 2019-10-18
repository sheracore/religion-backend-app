from application.extensions import db, ma
from models.video import Video
from models.sound import Sound


class Category(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    category_media = db.Column(db.String(80), unique=True, nullable=False)
    videos = db.relationship('Video', backref='category',cascade="all, delete-orphan",lazy=True)
    sounds = db.relationship('Sound', backref='category',cascade="all, delete-orphan",lazy=True)


class CategorySchema(ma.ModelSchema):
    class Meta:
        model = Category
