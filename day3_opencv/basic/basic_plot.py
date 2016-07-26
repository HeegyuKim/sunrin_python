#-*- coding: utf-8 -*-
import cv2;
from matplotlib import pyplot as plt

#기본값, 색상값만 읽어옴
img_bgr = cv2.imread('cat.jpg', cv2.IMREAD_UNCHANGED)

rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img_bgr, cv2.COLOR_RGB2GRAY)


plt.subplot(131), plt.imshow(img_bgr), plt.title('BGR')
plt.xticks([]), plt.yticks([])

plt.subplot(132), plt.imshow(rgb), plt.title('RGB')
plt.xticks([]), plt.yticks([])

plt.subplot(133), plt.imshow(gray, 'gray'), plt.title('GRAY')
plt.xticks([]), plt.yticks([])

plt.show()