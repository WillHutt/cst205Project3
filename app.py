import flask
import os
from flask import request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import send_from_directory

UPLOAD_FOLDER = 'static/pictures' #location that the desired photo will be saved
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg']) #only these formats will be allowed to upload

app = flask.Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 
def allowed_file(filename): #grabs the user's picture file name
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST']) #basic site
def index():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flask.flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flask.flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename): #if the form has been properly completed
            
            # saves the photo to the desired place
            filename = secure_filename(file.filename)
            filename = "user_upload.jpg"
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            success = "Uploaded!"
            return flask.render_template("index.html", success=success)
    return flask.render_template("index.html")

app.run(
    host = os.getenv('IP', '0.0.0.0'),
    port = int(os.getenv('PORT', 8080))
)
    