import numpy as np
import cv2

img = cv2.imread('/home/ritik/Documents/input images/crossword.jpg',0)

_,th_1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
th_2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 12);
th_3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 12);

cv2.imshow("Simple_threshold", th_1)
cv2.imshow("Adaptive_mean_c", th_2)
cv2.imshow("Adaptive_gaussian_c",th_3)
cv2.waitKey()
cv2.destroyWindow()