import cv2
import numpy as np
from matplotlib import pyplot as plt


cat = cv2.imread('cat.jpg', 0)
ret, dst = cv2.threshold(cat, 127, 255, cv2.THRESH_BINARY)

cv2.imshow('Threshold', dst)
cv2.waitKey(0)

#plt.subplot(121), plt.imshow(cat, 'gray')
#plt.subplot(122), plt.imshow(dst, 'gray')
#plt.show()