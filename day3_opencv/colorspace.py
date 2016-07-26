import cv2;

cat = cv2.imread('cat.jpg');

cat_gray = cv2.cvtColor(cat, cv2.COLOR_RGB2GRAY)

cv2.imwrite('cat_gray.jpg', cat_gray)