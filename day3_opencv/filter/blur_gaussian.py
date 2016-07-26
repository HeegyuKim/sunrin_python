
import cv2
import numpy as np
from matplotlib import pyplot as plt

cat = cv2.cvtColor(cv2.imread('cat.jpg'), cv2.COLOR_BGR2RGB)

dst = cv2.GaussianBlur(cat, (25, 25), 0)


plt.subplot(121),plt.imshow(cat),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Gaussian')
plt.xticks([]), plt.yticks([])
plt.show()