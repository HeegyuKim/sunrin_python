import cv2;


cat = cv2.imread('cat.jpg')
cola = cv2.imread('cola.png')


result = cv2.addWeighted(cat, 1.0, cola, 0, 0)

imshow('result', result)