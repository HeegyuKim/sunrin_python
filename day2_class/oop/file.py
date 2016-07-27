
class File:

	def __init__(self, name, openmode):
		self.file = open(name, openmode)
		self.name = name
		print("객체 생성")

	def close(self):
		self.file.close()

	def __del__(self):
		self.close()
		print("객체 제거 완료")


if __name__ == "__main__":
	f = File("album.py", 'r')
	print(f.name)
	