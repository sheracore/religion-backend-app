from flask import Blueprint, request, jsonify
from models.category import Category, CategorySchema
from flask_jwt_extended import jwt_required
from application.extensions import db

blueprint = Blueprint('category', __name__, url_prefix='/api/v1')


@blueprint.route('/category', methods=['POST'])
@jwt_required
def create_category():
    category_media = request.json.get('category_media')
    if not category_media:
        return jsonify({"Error": [{"Type": "I/O", "message_error": "Insert category of media"}]}), 400
    duplicate = Category.query.filter_by(category_media=category_media).first()
    if duplicate:
            return jsonify({"Error": [{"Type": "business", "message_error": "category is a duplicate"}]}), 409

    category = Category(category_media=category_media)
    db.session.add(category)
    db.session.commit()
    return jsonify(CategorySchema().dump(category)), 201


@blueprint.route('/category', methods=['GET'])
@jwt_required
def list_categories():
    search = request.args.get('keyword', '')
    schema = CategorySchema(many=True)
    page_number = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 20))

    if search:
        categories = Category.query.filter(Category.category_media.ilike('%{}%'.format(
            search)))
        return jsonify(schema.dump(categories)), 200

    categories = Category.query.paginate(page_number, per_page, False)

    items = schema.dump(categories.items)
    return jsonify(items=items, total=categories.total), 200