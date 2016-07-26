import cv2
import numpy as np
from matplotlib import pyplot as plt

cat = cv2.imread('cat.jpg')
cat = cv2.cvtColor(cat, cv2.COLOR_BGR2RGB)
size = 5
kernel = np.array (
	[ 0, -1, 0,
	-1, 5, -1,
	0,	-1, 0
	]
	)
dst = cv2.filter2D(cat, -1, kernel)


plt.subplot(121),plt.imshow(cat),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Sharpen')
plt.xticks([]), plt.yticks([])
plt.show()