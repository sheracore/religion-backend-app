from application.extensions import db, ma



class Version(db.Model):
    __tablename__ = 'version'

    id = db.Column(db.Integer, primary_key=True)
    minVersion = db.Column(db.Integer, nullable=True)
    latest = db.Column(db.Integer, nullable=True)

class VersionSchema(ma.ModelSchema):
    class Meta:
        model = Version