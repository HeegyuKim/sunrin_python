#-*- coding: utf-8 -*-
from flask import Flask, request
import db
import hashlib

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


@app.route("/user", methods=["POST"])
def user():
	name = request.form['name']
	password = request.form['password']
	password = hashlib.sha1(password).digest()

	appdb = db.get()
	appdb.execute("INSERT INTO user (name, password) VALUES (?, ?)",
		[name, password])
	appdb.commit()
	return "추가되었습니다", 201

@app.route("/user/<int:id>", methods=["DELETE"])
def delete_user(id):
	appdb = db.get()
	appdb.execute("DELETE FROM user WHERE id=?", (id,))
	appdb.commit()
	return "죽.여.버.렸.다!", 202
	
if __name__ == "__main__":
	app.secret_key = "4vJBcM2JpI"
	app.config['SESSION_TYPE'] = 'filesystem'

	app.run(debug=True)