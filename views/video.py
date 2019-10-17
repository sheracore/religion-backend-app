from flask import Blueprint, request, jsonify
from flask import current_app

from models.video import Video,VideoSchema
from werkzeug.utils import secure_filename
from application.extensions import db

blueprint = Blueprint('video', __name__, url_prefix='/api/v1')


@blueprint.route('/upload_video_pic/', methods=['POST'])
def upload_video_pic():
    
    if 'file' not in request.files:
        return jsonify({"Error":"File dose not exist"}), 400
    
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({"Error":"Insert user id"}), 400
    # if file.filename == '':
    #     return jsonify({"filename":"error"}), 400
    
    file = request.files['file']
    if file :
        filename = secure_filename(file.filename)
        url_file = current_app.config['UPLOAD_FILE']+ filename
        file.save(url_file)
        print("file saved")

    description = request.form.get('description', filename)
    
    video = Video(text=description,video_url=url_file, picture_name=filename,user_id=user_id)
    db.session.add(video)
    db.session.commit()

    return jsonify({"filename" : filename}), 200