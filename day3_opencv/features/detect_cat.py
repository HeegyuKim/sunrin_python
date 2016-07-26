
import numpy as np
import cv2

cat_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')


img = cv2.imread('cat.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)


faces = cat_cascade.detectMultiScale(gray, 1.3, 5)

for (x, y, w, h) in faces:
	cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
