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
    file = request.files['file']
    title = request.form.get('title', 'titel')

    if not user_id:
        return jsonify({"Error":"Insert user id"}), 400
    
    if file :
        filename = secure_filename(file.filename)
        url_file = current_app.config['UPLOAD_FILE']+ filename
        file.save(url_file)
        print("file saved")
    
    text = request.form.get('text', filename)
    try:
        video = Video(title=title, text=text,video_url=url_file, thumbnaiUrl=filename,user_id=user_id)
    except Exception as e:
        return jsonify({"Error" : e}), 400 

    db.session.add(video)
    db.session.commit()

    return jsonify({"filename" : filename}), 200