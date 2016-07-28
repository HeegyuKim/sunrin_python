#-*- coding: utf-8 -*-
from flask import Flask, request, send_from_directory, redirect, url_for
from werkzeug import secure_filename
import os
import cv2

app = Flask(__name__)

@app.route("/findface", methods=["POST"])
def find_face():
	image = request.files['image']
	filename = secure_filename(image.filename)
	path = 'temp/' + filename
	image.save(path)

	faceImage = cv2.imread(path)
	face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
	faces = face_cascade.detectMultiScale(faceImage, 1.3, 5)

	for x, y, w, h in faces:
		cv2.rectangle(faceImage, (x, y), (x+w, y+h), (0, 0, 255), 4)

	static_path = 'static/' + filename
	cv2.imwrite(static_path, faceImage)

	uploads = os.path.join(app.root_path, 'static')
	return send_from_directory(uploads, filename)

if __name__ == "__main__":
	app.run(debug=True)