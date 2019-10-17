from application.extensions import db, ma
# from models.user import User


class Video(db.Model):
    __tablename__ = 'video'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(80), nullable=False)
    video_url = db.Column(db.String(256), nullable=False)
    picture_name = db.Column(db.String(256), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class VideoSchema(ma.ModelSchema):
    class Meta:
        model = Video
