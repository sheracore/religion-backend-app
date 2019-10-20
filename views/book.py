from flask import Blueprint, request, jsonify
from flask import current_app

from sqlalchemy import or_

from flask_jwt_extended import jwt_required
from models.book import Book,BookSchema
from models.user import User
from werkzeug.utils import secure_filename
from application.extensions import db

blueprint = Blueprint('book', __name__, url_prefix='/api/v1')


@blueprint.route('/book', methods=['POST'])
@jwt_required
def upload_book():
    
    if 'book' not in request.files:
        return jsonify({"Error":"Please choose an electronic book"}), 400
    
    book = request.files['book']
    user_id = request.form.get('user_id')
    title = request.form.get('title')
    author = request.form.get('author',)
    page_number = request.form.get('page_number')


    if not title:
        return jsonify({"Error":[{"Type":"I/O","message_error":"title is not inserted"}]}), 400

    if not author:
        return jsonify({"Error":[{"Type":"I/O","message_error":"author is not inserted"}]}), 400

    if not page_number:
        return jsonify({"Error":[{"Type":"I/O","message_error":"page_number is not inserted"}]}), 400

    if not user_id:
        return jsonify({"Error":[{"Type":"I/O","message_error":"user_id is not inserted"}]}), 400

    user = User.query.filter_by(id=user_id).first()
    if not user:
        return jsonify({"Error":[{"Type":"business","message_error":"user_id not found"}]}), 400 
    
    if book :
        filename = secure_filename(book.filename)
        url_file = current_app.config['UPLOAD_FILE'] + filename

        duplicate = Book.query.filter_by(book_url=url_file).first()
        if duplicate:
            return jsonify({"Error":[{"Type":"business","message_error":"This book uploaded before"}]}), 400 
        book.save(url_file)
    
    book = Book(title=title,page_number=page_number, author=author, book_url=url_file, thumbnaiUrl=filename,user_id=user_id)


    db.session.add(book)
    db.session.commit()

    return jsonify(BookSchema().dump(book)), 200

@blueprint.route('/book', methods=['GET'])
@jwt_required
def get_book():

    page_number = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 6))
    schema = BookSchema(many=True)

    books = Book.query.paginate(page_number,per_page,False)
    items = schema.dump(books.items)
    return jsonify(items=items), 200