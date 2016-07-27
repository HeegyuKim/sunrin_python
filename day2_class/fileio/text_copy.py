

with open('textfile.txt', 'r') as file, \
	open('textfile-copy.txt', 'w') as copy:
	text = file.read()

	print(text)

	copy.write(text)

