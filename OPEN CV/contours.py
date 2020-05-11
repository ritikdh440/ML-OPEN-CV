import cv2
import numpy as np

img = cv2.imread("/home/ritik/Documents/input images/flower.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret, threshold = cv2.threshold(gray, 127, 255 , 0)
edge = cv2.Canny(threshold,100,200)
contours, hierarchy = cv2.findContours(edge,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img,contours,-1, (0,255,0), 3)

cv2.imshow("IMAGE", img)
cv2.waitKey()
cv2.destroyWindow()