# file : p63_opencv.py
# desc : OpenCV 영상처리

import cv2

smaple = './day09/earth.mp4'
cap = cv2.VideoCapture(smaple)   # 0은 웹캠, 문자열로 동영상 경로

while True:
    ret, frame = cap.read()

    if not ret:
        cap = cv2.VideoCapture(smaple)
        continue

    ## 영상 편집
    blur = cv2.blur(frame,(10,10))
    flip = cv2.flip(frame,0)

    cv2.imshow('original', frame)
    cv2.imshow('blur',blur)
    cv2.imshow('flip',flip)

    key = cv2.waitKey(5) # 5ms waitKey 딜레이
    if key == 27: # esc 키를 누르면 닫힘, ord('q')는 q를 누르면 닫힘
        break
    elif key == ord('c'): #화면캡쳐
        cv2.imwrite('./day09/capt.jpg', frame)

cap.release()
cv2.destroyAllWindows()