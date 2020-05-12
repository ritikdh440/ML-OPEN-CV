import numpy as np
import cv2

cap = cv2.VideoCapture(0)


while True:
    ret,frame = cap.read()
    blur = cv2.GaussianBlur(frame,(5,5),0)

    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

    Lower_blue = np.array([22, 100, 100])
    Upper_blue = np.array([40, 255 ,255])

    mask = cv2.inRange(hsv,Lower_blue,Upper_blue)

    contours,_ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(frame, contours, -1, (0,255,0), 3)
    cv2.imshow('mask', mask)
    cv2.imshow('frame', frame)


    if cv2.waitKey(1)  & 0xFF  == 27:
        break

cap.release()
cv2.destroyWindow()

