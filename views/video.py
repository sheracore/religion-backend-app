from flask import Blueprint, request, jsonify
from flask import current_app

from werkzeug.utils import secure_filename

from flask_jwt_extended import jwt_required
from models.video import Video,VideoSchema
from models.category import Category, CategorySchema
from models.user import User
from application.extensions import db

blueprint = Blueprint('video', __name__, url_prefix='/api/v1')


@blueprint.route('/video', methods=['POST'])
@jwt_required
def upload_video():
    
    if 'file' not in request.files:
        return jsonify({"Error":"File dose not exist"}), 400
    
    file = request.files['file']
    user_id = request.form.get('user_id')
    category_id = request.form.get('category_id')
    title = request.form.get('title')
    text = request.form.get('text')

    if not title:
        return jsonify({"Error":[{"Type":"I/O","message_error":"title is not inserted"}]}), 400
    
    if not text:
        return jsonify({"Error":[{"Type":"I/O","message_error":"text is not inserted"}]}), 400

    if not user_id:
        return jsonify({"Error":[{"Type":"I/O","message_error":"user_id is not inserted"}]}), 400

    user = User.query.filter_by(id=user_id).first()
    if not user:
        return jsonify({"Error":[{"Type":"business","message_error":"This user is not exist"}]}), 400 

    category = Category.query.filter_by(id=category_id).first()
    if not category:
        return jsonify({"Error":[{"Type":"business","message_error":"This category is not exist"}]}), 400 

    
    if file :
        filename = secure_filename(file.filename)
        url_file = current_app.config['UPLOAD_FILE']+ filename

        duplicate = Video.query.filter_by(video_url=url_file).first()
        if duplicate:
            return jsonify({"Error":[{"Type":"business","message_error":"This video uploaded before"}]}), 400 
        file.save(url_file)
        print("file saved")
    
    video = Video(title=title, text=text,video_url=url_file, category_id=category_id, thumbnaiUrl=filename,user_id=user_id)
    

    db.session.add(video)
    db.session.commit()

    return jsonify(VideoSchema().dump(video)), 201


@blueprint.route('/video', methods=['GET'])
@jwt_required
def video_list():

    schema = VideoSchema(many=True)

    page_number = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 20))
    category_id = request.args.get('category_id')

    if category_id: 
        category = Category.query.filter_by(id=category_id).first()
        if not category:
            return jsonify({"Error":[{"Type":"business","message_error":"This category is not exist"}]}), 400
    else:
        video = Video.query.filter_by(category_id=category_id).paginate(page_number,per_page,False)

    video = Video.query.paginate(page_number,per_page,False)
    items = schema.dump(video.items)
    return jsonify(items=items), 200