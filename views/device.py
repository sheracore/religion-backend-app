from flask import Blueprint, request, jsonify
from models.device import Device, DeviceSchema
from flask_jwt_extended import jwt_required
from application.extensions import db

blueprint = Blueprint('device', __name__, url_prefix='/api/v1')


@blueprint.route('/device', methods=['POST'])
@jwt_required
def create_device():
    device_id = request.json.get('device_id')
    if not device_id:
        return jsonify({"Error": [{"Type": "I/O", "message_error": "Insert device id"}]}), 400
    duplicate = Device.query.filter_by(device_id=device_id).first()
    if duplicate:
            return jsonify({"Error": [{"Type": "business", "message_error": "device_id is a duplicate"}]}), 409
    versionName = request.json.get('versionName')
    if not versionName:
        return jsonify({"Error": [{"Type": "I/O", "message_error": "Insert version name"}]}), 400
    duplicate = Device.query.filter_by(versionName=versionName).first()
    if duplicate:
            return jsonify({"Error": [{"Type": "business", "message_error": "versionName is a duplicate"}]}), 409
    applicationName = request.json.get('applicationName')
    if not applicationName:
        return jsonify({"Error": [{"Type": "I/O", "message_error": "Insert application name"}]}), 400
    deviceName = request.json.get('deviceName')
    if not deviceName:
        return jsonify({"Error": [{"Type": "I/O", "message_error": "Insert device name"}]}), 400
    systemName = request.json.get('systemName')
    if not systemName:
        return jsonify({"Error": [{"Type": "I/O", "message_error": "Insert system name"}]}), 400

    device = Device(device_id=device_id, versionName=versionName,
                    applicationName=applicationName, deviceName=deviceName, systemName=systemName)
    db.session.add(device)
    db.session.commit()
    return jsonify(DeviceSchema().dump(device)), 201


@blueprint.route('/device', methods=['GET'])
@jwt_required
def list_device():
    search = request.args.get('keyword', '')
    schema = DeviceSchema(many=True)
    page_number = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 20))

    if search:
        devices = Device.query.filter(Device.deviceName.ilike('%{}%'.format(
            search)))
        return jsonify(schema.dump(devices)), 200

    devices = Device.query.paginate(page_number, per_page, False)

    items = schema.dump(devices.items)
    return jsonify(items=items, total=devices.total), 200
