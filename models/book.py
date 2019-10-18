from application.extensions import db, ma



class Book(db.Model):
    __tablename__ = 'book'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(64), nullable=True)
    author = db.Column(db.String(256), nullable=True)
    page_number = db.Column(db.Integer, nullable=True)
    book_url = db.Column(db.String(256), nullable=False)
    thumbnaiUrl = db.Column(db.String(256), nullable=True)
    

class BookSchema(ma.ModelSchema):
    class Meta:
        model = Book
