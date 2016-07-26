import cv2
import numpy as np
from matplotlib import pyplot as plt

cat = cv2.imread('cat.jpg')

kernel = np.array(
		[-2, -2, 0,
		-2, 6, 0,
		0, 0, 0]
	)

dst = cv2.filter2D(cat, -1, kernel)


plt.subplot(121),plt.imshow(cat),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Emboss')
plt.xticks([]), plt.yticks([])
plt.show()