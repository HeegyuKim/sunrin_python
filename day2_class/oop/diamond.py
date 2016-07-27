
class A:
	def __init__(self):
		print("A")

class B(A):
	def __init__(self):
		super().__init__()
		#A.__init__(self)
		print ("B")

class C(A):
	def __init__(self):
		super().__init__()
		#A.__init__(self)
		print ("C")

class D(B, C):
	def __init__(self):
		#B.__init__(self)
		#C.__init__(self)
		#A.__init__(self)
		super().__init__()
		print("D")
d = D()