import cv2

img = cv2.imread('Experimental/bottlenme.jpg', cv2.COLOR_BGR2GRAY)
resimg = cv2.resize(img, (100, 100))
bottle_cascade = cv2.CascadeClassifier('Cascades/haarcascade_water_bottle.xml')
bottles = bottle_cascade.detectMultiScale(resimg, 1.3, 5)

for (x, y, w, h) in bottles:
    cv2.putText(resimg, 'Bottle', (x, y), cv2.FONT_HERSHEY_COMPLEX, .5, (255, 255, 0))

cv2.imshow('hi', resimg)

height, width, depth = img.shape
print bottles.size
cv2.imshow('res', cv2.resize(resimg, (width, height)))

cv2.waitKey(0)
