import os
from flask import Flask, request, redirect, url_for, render_template
# from werkzeug import secure_filename

app = Flask(__name__)
ALLOWED_EXTENSIONS = app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'html'])
app.config['DEBUG'] = True

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/api/file-upload", methods=['POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join('uploads/', filename))
            uploaded = "File was uploaded"
            return "uploaded", 200
            # return render_template("index.html",uploaded = uploaded)
        uploaded = "something went wrong!"
        return uploaded, 405
        # return render_template("index.html",uploaded = uploaded)
    return 405, "only POST request supported"
    # return render_template("index.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.debug = True
    app.run(port=8083, host='0.0.0.0')