from flask import Flask, render_template, request, redirect, flash, url_for
import main
import urllib.request
from app import app
from werkzeug.utils import secure_filename
from main import getPrediction
import os

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fabric/', methods = ['GET'])
def fabric():
    return render_template('fabric.html')

@app.route('/color/', methods = ['GET'])
def color():
    return render_template('color.html')

@app.route('/length/', methods = ['GET'])
def lenth():
    return render_template('length.html')



@app.route('/', methods=['POST'])
def submit_file():
    if request.method == 'POST':
        # if 'file' not in request.files:
        #     flash('No file part')
        #     return redirect(request.url)
        # file = request.files['file']
        # if file.filename == '':
        #     flash('No file selected for uploading')
        #     return redirect(request.url)
        # if file:
        filename = 'C:/Users/yoosh/PycharmProjects/pythonProject/imgUpdate/static/images/용구.jpg' #secure_filename(file.filename)
        #file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        getPrediction(filename)
        fabric, color, length = getPrediction(filename)
        flash(fabric)
        flash(color)
        flash(length)
        flash(filename)
        return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)