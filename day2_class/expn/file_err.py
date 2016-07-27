
f = None
try:
	f = open("file_err2.py", 'r')

except:
	print("파일을 못읽어부렸어!")
else:
	print("파일을 읽어부렸어!")
	f.close()
finally:
	print("프로그램을 종.료.합.니.다")