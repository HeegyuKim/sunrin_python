
class Cola:

	def __init__(self, size):
		print("%.2fL 콜라 생성" % size)
		self.size = size

	def __add__(self, other):
		return Cola(self.size + other.size)

	def __sub__(self, other):
		return Cola(self.size - other.size)

a = Cola(1.5)
b = Cola(0.5)
c = Cola(1.8)

a += b
d = a + b
d -= c

