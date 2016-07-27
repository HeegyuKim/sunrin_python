from flask import Flask, request
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
	return "Hello Flask!"

@app.route("/login", methods=["GET", "POST"])
def login(name):
	if request.method == "GET":
		return "로그인 화면"
	else:
		return "로그인이 완료되었습니다"


if __name__ == "__main__":
	app.run(debug=True)