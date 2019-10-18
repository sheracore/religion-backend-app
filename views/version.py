from flask import Blueprint, request, jsonify
from models.version import Version,VersionSchema
from application.extensions import db

blueprint = Blueprint('version', __name__, url_prefix='/api/v1')

@blueprint.route('/version', methods=['POST'])
def create_version():
    minVersion = request.json.get('minVersion')
    latest = request.json.get('latest')


    version = Version(username=username,latest=latest)
    db.session.add(version)
    db.session.commit()
    return jsonify(VersionSchema().dump(version)), 201