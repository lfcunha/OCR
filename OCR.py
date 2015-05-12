import os
from flask import Flask
from flask import Blueprint, request, render_template, redirect, url_for
from werkzeug import secure_filename

from rq import Queue
from rq.job import Job
from worker import conn
q = Queue(connection=conn)

UPLOAD_FOLDER = '/home/luis/PycharmProjects/OCR/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


class Ocr:
    queue = "OCR"
    def __init__(self,filename):
        self.filename = filename
        
    @staticmethod
    def perform(self):
        import pytesseract
        import requests
        from PIL import Image
        from PIL import ImageFilter
        from StringIO import StringIO
        image = Image.open(StringIO(requests.get(self.filename).content))
        image.filter(ImageFilter.SHARPEN)
        return pytesseract.image_to_string(image)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def ocr():
    if request.method == 'GET':
        return render_template('OCR/index.html')
    else:
        pass

@app.route('/uploads', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template('OCR/upload.html')
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        job = q.enqueue_call(
            func=ocr, args=(filename,), result_ttl=5000
        )
        return redirect(url_for('uploaded_file', filename=filename))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8081, debug=True)
