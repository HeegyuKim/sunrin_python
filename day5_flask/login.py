#-*- coding: utf-8 -*-
from flask import Flask, request, session

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
	if 'username' in session:
		return "Hello, " + session['username']
	else:
		return "Login Please"
@app.route("/login", methods=["POST"])
def login():
	username = request.form['username']
	session['username'] = username
	return 'login succeeded'

@app.route("/logout", methods=["POST"])
def logout():
	del session['username']
	return 'logout succeeded'

if __name__ == "__main__":
	app.secret_key = "4vJBcM2JpI"
	app.config['SESSION_TYPE'] = 'filesystem'

	app.run(debug=True)