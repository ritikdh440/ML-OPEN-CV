import numpy as np
import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('/home/ritik/Documents/xml files/haarcascade_frontalface_default.xml')

while True:
    _,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for rect in faces:
        (x, y, w, h) =rect
        frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 3)
    

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
