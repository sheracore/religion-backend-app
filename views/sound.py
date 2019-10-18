# from flask import jsonify, Blueprint, request
# from werkzeug.security import check_password_hash
# from sqlalchemy import or_
# from flask_jwt_extended import (
#     jwt_required, create_access_token, get_jwt_identity)

# from application.extensions import db
# import os
# from flask import Flask, request, redirect, url_for
# from werkzeug.utils import secure_filename



# blueprint = Blueprint('sound', __name__, url_prefix='/api/v1')


# @blueprint.route('/sounds', methods=['POST'])
# def upload_file():
#     if 'file' not in request.files:
#         return jsonify(message_text = No file part)

#     file = request.files['file']
#     if file.filename == '':
#         return jsonify(message_text = No selected file)
#     if file :
#         filename = secure_filename(file.filename)
#         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

#     return jsonify(file_name = filename)


#     if 'file' not in request.files:
#         return jsonify({"Error":"File dose not exist"}), 400
#         # flash('No file part')
#     file = request.files['file']
#     # if file.filename == '':
#     #     return jsonify({"filename":"error"}), 400

#     if file :
#         filename = secure_filename(file.filename)
#         url_file = current_app.config['UPLOAD_FILE']+ filename
#         file.save(url_file)
#         print("file saved")
    
    
#     video = Video(name="xashen",video_url=url_file, picture_name=filename)
#     db.session.add(video)
#     db.session.commit()

#     return jsonify({"filename" : filename}), 200