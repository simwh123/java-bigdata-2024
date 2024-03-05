# file : p60_opencv.py
# desc : OpenCV 이미지 처리 계속

import cv2

image = cv2.imread('./day09/cat.jpg',cv2.IMREAD_UNCHANGED)  # 원본
dst = cv2.flip(image,1) # 0은 상하반전, 1은 좌우반전

height, width, channel = image.shape
matrix = cv2.getRotationMatrix2D((width//2, height//2),90,1) # 세번쨰 옵션, scale, -1 = CW(시계방향), 1 = CCW(반시계방향) 2이상(배율)
thrd = cv2.warpAffine(image, matrix,(width,height))

reverse = cv2.bitwise_not(image)  # 역상, 반전색
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, bny = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY) # 이진화(0또는 1)

cv2.imshow('Cat', image)
cv2.imshow('Flip',dst)  # 이미지를 뒤집음
cv2.imshow('Rotation',thrd)
cv2.imshow('reverse',reverse)
cv2.imshow('gray', gray)
cv2.imshow('Binary',bny)

cv2.waitKey(0)
cv2.destroyAllWindows()