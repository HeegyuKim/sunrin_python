#-*- coding: utf-8 -*-
from flask import Flask, request, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
	return "Hello Flask!"

@app.route("/upload", methods=["POST"])
def uploadFile():
	f = request.files['image']
	save_path = "static/" + secure_filename(f.filename)
	f.save(save_path)
	return save_path

if __name__ == "__main__":
	app.run(debug=True)