from flask import Flask, render_template, request
from werkzeug.utils import secure_filename # 将各种文件名转换为安全的不会异常的文件名
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploaddir/' # 建立一个叫 uploaddir 的目录

@app.route('/')
def upload_file():
    return render_template('upload10.html')

@app.route('uploader', methods = ['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['file111']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        return 'file iploaded successfully'

    elif request.method == 'GET':
        return render_template('upload10.html')

if __name__ == '__main__':
    app.run(debug = True, threaded = True)




























