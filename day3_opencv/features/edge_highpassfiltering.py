#-*- coding: utf-8 -*-
import numpy as np
import cv2
from matplotlib import pyplot as plt


img = cv2.imread("cola.png", 0)

print(img)

cv2.imshow("cola", img)
kernel = np.array(
		[-1, -1, -1,
		-1, 9, -1,
		-1, -1, -1]
	)


dst = cv2.filter2D(img, 0, kernel)
ret, sub = cv2.threshold(
	cv2.subtract(dst, img), 
	127,
	255,
	cv2.THRESH_BINARY
	)

plt.subplot(221), plt.imshow(img, cmap='gray'), plt.title('Original')
plt.subplot(223), plt.imshow(dst, cmap='gray'), plt.title('highpass')
plt.subplot(222), plt.imshow(sub, 'gray'), plt.title('Edge')
plt.show()
'''
cv2.imshow('highpass filtered', dst)
cv2.imshow('subtraction', sub)
cv2.waitKey(0)
'''