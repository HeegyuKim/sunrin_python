#-*- coding: utf-8 -*-
from flask import Flask, send_file, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
	return "Hello Flask!"

@app.errorhandler(404)
def page_not_found(e):
	return send_file('static/404.jpg', mimetype='image/jpg'), 404

	
if __name__ == "__main__":
	app.run(debug=True)