#-*- coding: utf-8 -*-
from flask import Flask, request, send_file
from werkzeug.utils import secure_filename
import db
import hashlib
import cv2
import os

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
	appdb = db.get()
	cur = appdb.execute("SELECT * FROM user")
	users = cur.fetchall()

	output = []
	for user in users:
		output.append(str(user))

	return"<br>".join(output)

@app.route("/upload/profile/<int:id>", methods=["POST"])
def uploadProfile(id):
	f = request.files['profile']
	temp_path = 'temp/' + secure_filename(f.filename)
	f.save(temp_path)

	image = cv2.imread(temp_path)
	height, width, depth = image.shape

	ratio = 300.0 / width
	image = cv2.resize(image, (300, int(height * ratio)), interpolation=cv2.INTER_CUBIC)
	cv2.imwrite('profile/%d.jpg' % id, image)

	os.remove(temp_path)
	return "업로드되었습니다", 202

@app.route("/profile/<int:id>", methods=["GET"])
def getProfile(id):
	return send_file('profile/%d.jpg' % id)
if __name__ == "__main__":
	app.secret_key = "4vJBcM2JpI"
	app.config['SESSION_TYPE'] = 'filesystem'

	app.run(debug=True)