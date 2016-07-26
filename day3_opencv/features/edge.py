import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('cola.png',0)

laplacian = cv2.Laplacian(img,cv2.CV_32F)
sobelx = cv2.Sobel(img,cv2.CV_32F,1,0,ksize=5)
sobely = cv2.Sobel(img,cv2.CV_32F,0,1,ksize=5)

ret, laplacian = cv2.threshold(laplacian, 127, 255, cv2.THRESH_BINARY)
ret, sobelx = cv2.threshold(sobelx, 127, 255, cv2.THRESH_BINARY)
ret, sobely = cv2.threshold(sobely, 127, 255, cv2.THRESH_BINARY)

plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

plt.show()