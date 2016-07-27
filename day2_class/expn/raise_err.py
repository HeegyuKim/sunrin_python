
try:
	num = input('숫자를 입력해 주세요: ')
	if not num.isdigit():
		raise Exception("숫자가 아니에요")

	print("입력하신 숫자는 :", num)
except Exception as e:
	print(e)

