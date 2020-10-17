import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)


while True:
    ret,frame = cap.read()
    blur = cv.GaussianBlur(frame,(5,5),0)

    hsv = cv.cvtColor(blur, cv.COLOR_BGR2HSV)

    Lower_blue = np.array([22, 100, 100])
    Upper_blue = np.array([40, 255 ,255])

    mask = cv.inRange(hsv,Lower_blue,Upper_blue)

    contours,_ = cv.findContours(mask,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
    cv.drawContours(frame, contours, -1, (0,255,0), 3)
    cv.imshow('mask', mask)
    cv.imshow('frame', frame)


    if cv.waitKey(1)  & 0xFF  == 27:
        break

cap.release()
cv.destroyWindow()

