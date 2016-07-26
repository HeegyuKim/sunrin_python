import cv2
import numpy as np
from matplotlib import pyplot as plt

cat = cv2.cvtColor(cv2.imread('cat.jpg'), cv2.COLOR_BGR2RGB)

size = 25
kernel = np.ones((size, size), np.float32) / size ** 2

dst1 = cv2.filter2D(cat, 0, kernel)


plt.subplot(121),plt.imshow(cat),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst1),plt.title('Box Blur(%dx%d)' % (size, size))
plt.xticks([]), plt.yticks([])
plt.show()