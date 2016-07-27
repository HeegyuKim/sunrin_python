from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
	return "Hello Flask!"

@app.route("/hello/<string:name>")
def hello(name):
	return "Hello, " + name

if __name__ == "__main__":
	app.run(debug=True)