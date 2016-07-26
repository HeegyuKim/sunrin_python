
import cv2
import numpy as np

width = 500
height = 500


img = cv2.imread('cat.jpg')
iwidth, iheight, ichannel = img.shape

cv2.circle(img, (100, 150), 50, (255, 0, 0), 2)
cv2.line(img, (0, 0), (iwidth, iheight), (0, 255, 0), 4)
cv2.rectangle(img, (150, 150), (350, 500), (255, 0, 255), 3)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


cv2.imwrite('drawing.jpg', img)