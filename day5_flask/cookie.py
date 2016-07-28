#-*- coding: utf-8 -*-
from flask import Flask, request, make_response, redirect, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
	if request.cookies.get('show_event') != 'yes':
		return redirect(url_for('event'))
	else:
		return u"ㅎㅇㅎㅇ"

@app.route("/event")
def event():
	res = make_response(u"""
♨100%무료교육※웹개발★서버개발§§각종디자인§§☞부담감NO☜♬취업걱정＠필요없는♬최고의선택♬지금이순간!
㈜대선린인터넷고등학교☞대학진학률▶▶특성화고중▶▶최고▶▶디미고제외!§§대만족§§☎자녀를위해!!☎지금＠전화GOGO~~
●SUNRIN~WIKI♬2년★이상★재학시▶▶멘탈붕괴♠▶▶인내력↗상승↗▶▶지적능력↗상승↗▶▶탁월한 효과!§§다양한§§
경험§§다양한§§삽질§§헬조선적응력↗상승↗""", 200)
	res.set_cookie('show_event', 'yes')
	return res

@app.route("/clear-cookie")
def clear_cookie():
	res = make_response("쿠키가 제거되었습니다.")
	res.set_cookie('show_event', '', expires=0)
	return res

if __name__ == "__main__":
	app.secret_key = "4vJBcM2JpI"
	app.config['SESSION_TYPE'] = 'filesystem'

	app.run(debug=True)