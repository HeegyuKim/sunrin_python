

class Pet:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def play(self):
		pass
	def say(self):
		pass
	def travel(self, place):
		print("%s가 %s로 이동" % (self.name, place))


class Dog(Pet):

	def __init__(self, name, age):
		Pet.__init__(self, name,age)

	def play(self):
		print("주인님과 공놀이를 하였다")

	def say(self):
		print("!엄안마로망!!아ㅓㅁㄴ롬널!!!")

	def travel(self, place):
		print("멍멍!! %s는 주인님이랑 %s로 갔다!!" % (self.name, place))

class Parrot(Pet):
	def __init__(self, name, age):
		Pet.__init__(self, name,age)

	def play(self):
		print("주인님을 피해 날아다녔다!")

	def say(self):
		print("엄마 밥줘!")

	def travel(self, place):
		print("날아간다! 날아간다! %s %s로 나라간다!(슝)" % (self.name, place))


dog = Dog('비글', 5)
dog.play()
dog.say()
dog.travel('공원')

parrot = Parrot('짹짹이', 2)
parrot.play()
parrot.say()
parrot.travel('뒷산')