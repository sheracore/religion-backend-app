from flask import Blueprint, request, jsonify
from models.category import Category,CategorySchema
from application.extensions import db

blueprint = Blueprint('category', __name__, url_prefix='/api/v1')

@blueprint.route('/category', methods=['POST'])
def create_category():

    category_media = request.json.get('category_media')
    if not category_media:
    	return jsonify({"Error":[{"Type":"I/O","message_error":"Please insert category name"}]}), 400

    duplicate = Category.query.filter_by(category_media=category_media).first()
    if duplicate:
    	return jsonify({"Error":[{"Type":"business","message_error":"This category exist."}]}), 400

    category = Category(category_media=category_media)
    db.session.add(category)
    db.session.commit()
    return jsonify(CategorySchema().dump(category)), 201