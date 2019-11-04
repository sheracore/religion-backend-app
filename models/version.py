from application.extensions import db, ma



class Version(db.Model):
    __tablename__ = 'version'

    id = db.Column(db.Integer, primary_key=True)
    minVersion = db.Column(db.String(80),nullable=True)
    latest = db.Column(db.String(80),nullable=True)

class VersionSchema(ma.ModelSchema):
    class Meta:
        model = Version