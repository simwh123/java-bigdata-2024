# file : p61_opencv.py
# desc : OpenCV 계속

import cv2

image = cv2.imread('./day09/cat.jpg',cv2.IMREAD_UNCHANGED)

height, width, channel = image.shape

cv2.imshow('Cat', image)

cv2.waitKey(0)
cv2.destroyAllWindows()