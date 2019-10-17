from application.extensions import db, ma

class Video(db.Model):
    __tablename__ = 'video'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    video_url = db.Column(db.String(256), nullable=False)
    picture_name = db.Column(db.String(256), nullable=False) 

class VideoSchema(ma.ModelSchema):
    class Meta:
        model = Video
        # exclude = ['hashed_password']
