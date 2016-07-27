
class FilterError(Exception):

	def __str__(self):
		return "권욱제는 허용되지 않습니다"



name = input("이름을 입력해 주세요: ")
if name == "권욱제":
	raise FilterError()