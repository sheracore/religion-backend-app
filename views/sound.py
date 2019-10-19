from flask import Blueprint, request, jsonify
from flask import current_app
from models.user import User
from models.category import Category
from models.sound import Sound,SoundSchema
from werkzeug.utils import secure_filename
from application.extensions import db

blueprint = Blueprint('sound', __name__, url_prefix='/api/v1')


@blueprint.route('/sound', methods=['POST'])
def create_sound():
    
    if 'file' not in request.files:
        return jsonify({"Error":[{"Type":"I/O","message_error":"No file part"}]}), 400

    
    user_id = request.form.get('user_id')
    category_id = request.form.get('category_id')
    file = request.files['file']
    name = request.form.get('name')
    time = request.form.get('time')
    singer = request.form.get('singer')

    if not user_id:
        return jsonify({"Error":[{"Type":"I/O","message_error":"Insert user id"}]}), 400
    user = User.query.filter_by(id=user_id).first()
    if not user:
        return jsonify({"Error":[{"Type":"business","message_error":"user_id not found"}]}), 400
    if not category_id:
        return jsonify({"Error":[{"Type":"I/O","message_error":"Insert category id"}]}), 400
    category = Category.query.filter_by(id=category_id).first()
    if not category:
        return jsonify({"Error":[{"Type":"business","message_error":"category_id not found"}]}), 400 
    if file.filename == '':
        return jsonify({"Error":[{"Type":"I/O","message_error":"No selected file"}]}), 400
    if not name:
        return jsonify({"Error":[{"Type":"I/O","message_error":"Insert name"}]}), 400
    if not time:
        return jsonify({"Error":[{"Type":"I/O","message_error":"Insert time"}]}), 400
    if not singer:
        return jsonify({"Error":[{"Type":"I/O","message_error":"Insert singer"}]}), 400


    
    if file :
        filename = secure_filename(file.filename)
        url_file = current_app.config['UPLOAD_FILE']+ filename
        file.save(url_file)
    
    sound = Sound(user_id=user_id, category_id=category_id,name=name, time=time,singer=singer,sound_url=url_file)
  

    db.session.add(sound)
    db.session.commit()

    return jsonify(SoundSchema().dump(sound)), 201


@blueprint.route('/sound', methods=['GET'])
def list_sound():
    schema = SoundSchema(many=True)


    page_number = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 20))
    category_id = request.args.get('category_id','')

    if category_id:
        category = Category.query.filter_by(id=category_id).first()
        if not category:
            return jsonify({"Error":[{"Type":"business","message_error":"category_id not found"}]}), 400 
        sound = Sound.query.filter_by(category_id=category_id).paginate(page_number,per_page,False)
    else:
        sound = Sound.query.paginate(page_number,per_page,False)

    items = SoundSchema(many=True).dump(sound.items)
    return jsonify(items=items, total=sound.total)
