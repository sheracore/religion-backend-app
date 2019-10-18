from sqlalchemy.dialects.postgresql import JSON
from application.extensions import db, ma


class Sound(db.Model):

	__tablename__ = 'sound'

	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
	time = db.Column(db.Integer, nullable=True)
	singer = db.Column(db.String(64), nullable=True)
	sound_url = db.Column(db.String(256), nullable=False)
	name = db.Column(db.String(128), nullable=True)

   

class SoundSchema(ma.ModelSchema):
	class Meta:
		model = Sound