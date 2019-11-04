from flask import Blueprint, request, jsonify
from models.version import Version, VersionSchema
from flask_jwt_extended import jwt_required
from application.extensions import db

blueprint = Blueprint('version', __name__, url_prefix='/api/v1')


@blueprint.route('/version', methods=['POST'])
@jwt_required
def create_version():
    minVersion = request.json.get('minVersion')
    if not minVersion:
        return jsonify({"Error": [{"Type": "I/O", "message_error": "Insert min version"}]}), 400
    latest = request.json.get('latest')
    if not latest:
        return jsonify({"Error": [{"Type": "I/O", "message_error": "Insert latest version"}]}), 400

    version = Version(minVersion=minVersion, latest=latest)
    db.session.add(version)
    db.session.commit()
    return jsonify(VersionSchema().dump(version)), 201


@blueprint.route('/version', methods=['GET'])
@jwt_required
def list_versions():
    search = request.args.get('keyword', '')
    schema = VersionSchema(many=True)
    page_number = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 20))

    if search:
        versions = Version.query.filter(or_(Version.minVersion.ilike('%{}%'.format(
            search)), Version.latest.ilike('%{}%'.format(search))))
        return jsonify(schema.dump(versions)), 200

    versions = Version.query.paginate(page_number, per_page, False)

    items = schema.dump(versions.items)
    return jsonify(items=items, total=versions.total), 200


@blueprint.route('/version/<id>', methods=['PUT'])
@jwt_required
def update_version(id):
    version = Version.query.get_or_404(id)
    minVersion = request.json.get('minVersion')
    latest = request.json.get('latest')

    version.minVersion = minVersion
    if latest and version.latest != latest:
        duplicate = Version.query.filter_by(latest=latest).first()
        version.latest = latest

    db.session.commit()
    return jsonify(VersionSchema().dump(version)), 200
