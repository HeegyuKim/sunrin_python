#-*- coding: utf-8 -*-
from flask import Flask, request, url_for
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
	return "Hello Flask!"

@app.route("/cat")
def login():
	return url_for('static', filename='cat.jpg')


if __name__ == "__main__":
	app.run(debug=True)