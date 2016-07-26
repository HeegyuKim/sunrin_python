import cv2;


#기본값, 색상값만 읽어옴
img = cv2.imread('cat.jpg')
#img = cv2.imread('cat.jpg', cv2.IMREAD_COLOR)
# 흑백 이미지로 읽어옴
#img = cv2.imread('cat.jpg', cv2.IMREAD_GRAYSCALE)
# 알파 채널까지 읽어옴
#img = cv2.imread('cat.jpg', cv2.IMREAD_UNCHANGED)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('cat_gray.jpg', img);