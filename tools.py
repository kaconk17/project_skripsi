import cv2
import os
from numpy import savetxt

img = cv2.imread("models/HE6.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.resize(gray,(400,400))
print(gray)
(thresh, bw)=cv2.threshold(gray, 160,255,cv2.THRESH_BINARY)
print(bw)
cv2.imwrite("imbin.jpg",bw)
#cv2.imwrite("imgray.jpg",gray)
#cv2.imshow("ori",img)
#cv2.imshow("gray",gray)
#cv2.waitKey(0)