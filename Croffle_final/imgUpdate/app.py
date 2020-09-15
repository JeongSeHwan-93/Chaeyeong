from flask import Flask

#이거 경로 수정

UPLOAD_FOLDER = 'C:/Users/yoosh/PycharmProjects/pythonProject/imgUpdate/uploads'

app = Flask(__name__)

app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER