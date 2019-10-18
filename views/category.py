from flask import Blueprint, request, jsonify
from models.category import Category,CategorySchema
from application.extensions import db

blueprint = Blueprint('category', __name__, url_prefix='/api/v1')

@blueprint.route('/category', methods=['POST'])
def create_category():
    category_media = request.json.get('category_media')

    category = Category(category_media=category_media)
    db.session.add(category)
    db.session.commit()
    return jsonify(VersionSchema().dump(category)), 201