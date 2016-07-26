import cv2
import numpy as np
from matplotlib import pyplot as plt

cat = cv2.imread('cat.jpg')

size = 5
kernel = np.zeros(size**2, np.float32)

for i in range(size):
	kernel[size * (i - 1) + size / 2] = 1.0 / size

dst = cv2.filter2D(cat, -1, kernel)


plt.subplot(121),plt.imshow(cat),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Motion %d' % (size))
plt.xticks([]), plt.yticks([])
plt.show()