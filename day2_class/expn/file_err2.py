
try:
	f = open("짱짱멋진파일", 'r')

except FileNotFoundError as e:
	print(e)
except IndexError as e:
	print(e)