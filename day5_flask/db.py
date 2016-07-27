import sqlite3
from run import app
from flask import g

DATABASE = 'app.db'

def get():
	db = getattr(g, '_database', None)
	if db is None:
		db = g._database = sqlite3.connect(DATABASE)
		db.text_factory = str
	return db

@app.teardown_appcontext
def close_connection(e):
	db = getattr(g, '_database', None)
	if db is not None:
		db.close()
