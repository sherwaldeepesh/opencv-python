import cv2
import numpy as np

kernel = np.ones((5,5),np.uint8)

img = cv2.imread("Resource/t1.jpg")

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgGray = cv2.resize(imgGray, (640, 400))

imgBlur = cv2.GaussianBlur(imgGray,(5,5),0)

imgCanny = cv2.Canny(imgGray,200,200)

imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)

imgEroded = cv2.erode(imgDialation, kernel, iterations = 1)

cv2.imshow("Gray Image",imgGray)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Dialated Image", imgDialation)
cv2.imshow("Eroded Image", imgEroded)

cv2.waitKey(0)