from flask import jsonify, Blueprint, request
from werkzeug.security import check_password_hash
from sqlalchemy import or_
from flask_jwt_extended import (
    jwt_required, create_access_token, get_jwt_identity)

from sqlalchemy import or_
from application.extensions import db
from models.user import User, UserSchema

blueprint = Blueprint('user', __name__, url_prefix='/api/v1')


@blueprint.route('/user/login/', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"Error": [{"Type": "I/O", "message_error": "message error is not json type"}]}), 400

    username = request.json.get('username')
    password = request.json.get('password')

    if not username:
        return jsonify({"Error": [{"Type": "I/O", "message_error": " username is not inserted"}]}), 400
    if not password:
        return jsonify({"Error": [{"Type": "I/O", "message_error": " password is not inserted"}]}), 400

    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify(type="asdsa", message="sadjashkjdah"), 400

    if check_password_hash(user.hashed_password, password):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token,
                       user=UserSchema().dump(user)), 200

    return jsonify({"Error": [{"Type": "business", "message_error": "This user can't login"}]}), 400


@blueprint.route('/users', methods=['GET'])
@jwt_required
def list_users():
    search = request.args.get('keyword', '')
    schema = UserSchema(many=True)

    if search:
        users = User.query.filter(User.username.ilike('%{}%'.format(search)))
        return jsonify(schema.dump(users)), 200

    users = User.query.all()
    return jsonify(schema.dump(users)), 200


@blueprint.route('/users', methods=['POST'])
@jwt_required
def create_user():
    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        return jsonify({"Error": [{"Type": "I/O", "message_error": "password or username is not inserted"}]}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"Error": [{"Type": "business", "message_error": "this username is not exist"}]}), 400

    user = User(username=username)
    user.hashed_password = user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify(UserSchema().dump(user)), 201


@blueprint.route('/user/<id>', methods=['GET'])
@jwt_required
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(UserSchema().dump(user))


@blueprint.route('/user/<id>', methods=['DELETE'])
@jwt_required
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify(status="User deleted", user=UserSchema().dump(user))


@blueprint.route('/user/<id>', methods=['PUT'])
@jwt_required
def update_user(id):
    user = User.query.get_or_404(id)
    username = request.json.get('username')
    password = request.json.get('password')

    if username and user.username != username:
        duplicate = User.query.filter_by(username=username).first()
        if duplicate:
            return jsonify({"Error": [{"Type": "business", "message_error": "This username is not exist"}]}), 409
        user.username = username

    db.session.commit()
    return jsonify(status="User changed", user=UserSchema().dump(user)), 200
