import numpy as np
import cv2
import pyttsx as tts

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

# https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')
# https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
eye_cascade = cv2.CascadeClassifier('Cascades/haarcascade_eye.xml')

# bottle_cascade = cv2.CascadeClassifier('Cascades/haarcascade_water_bottle_trail.xml')

cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    resgray = cv2.resize(gray, (500, 500))
    # bottles = bottle_cascade.detectMultiScale(resgray, 1.3, 5)
    # print 'hi'
    k = 0
    height, width, channels = img.shape
    regions = [(0, 0, width / 3, height / 3), (width / 3, 0, 2 * width / 3, height / 3),
               (2 * width / 3, 0, width, height / 3), (0, height / 3, width / 3, 2 * height / 3),
               (width / 3, height / 3, 2 * width / 3, 2 * height / 3),
               (2 * width / 3, height / 3, width, 2 * height / 3), (0, 2 * height / 3, width / 3, height),
               (width / 3, 2 * height / 3, 2 * width / 3, height),
               (2 * width / 3, 2 * height / 3, width, height)]

    for (s, e, ss, ee) in regions:
        cv2.rectangle(img, (s, e), (ss, ee), (255, 255, 0), 2)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        if 0 < x < width / 3 and 0 < y < height / 3:
            print 'Top left\n'
        elif width / 3 < x < 2 * width / 3 and 0 < y < height / 3:
            print 'Top\n'
        elif 2 * width / 3 < x < width and 0 < y < height / 3:
            print 'Top Right\n'
        elif 0 < x < width / 3 and height / 3 < y < 2 * height / 3:
            print 'Left\n'
        elif width / 3 < x < 2 * width / 3 and height / 3 < y < 2 * height / 3:
            print 'Center\n'
        elif 2 * width / 3 < x < width and height / 3 < y < 2 * height / 3:
            print 'Right\n'
        elif 0 < x < width / 3 and 2 * height / 3 < y < height:
            print 'Bottom Left\n'
        elif width / 3 < x < 2 * width / 3 and 2 * height / 3 < y < height:
            print 'Bottom\n'
        elif 2 * width / 3 < x < width and 2 * height / 3 < y < height:
            print 'Bottom Right\n'
        k += 1
    l = 0
    # for (x, y, w, h) in bottles:
    #    cv2.rectangle(resgray, (x, y), (x + w, y + h), (255, 0, 0), 2)
    #    l += 1

    dispString = "There are " + str(k) + " face(s)"
    cv2.putText(img, dispString, (0, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0))
    cv2.imshow('img', img)
    resgray = cv2.resize(resgray, (width, height))
    # bdispString = "There are " + str(l) + "Bottle(s)"
    # cv2.putText(gray, bdispString, (0, 20), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0))
    cv2.imshow('resgray', resgray)
    p = cv2.waitKey(30) & 0xff
    if p == 27:
        break

cap.release()
cv2.destroyAllWindows()
