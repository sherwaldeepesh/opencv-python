import cv2
import numpy as np

img = cv2.imread("Resource/t1.jpg")
print(img.shape)

imgResize = cv2.resize(img, (640,480))
print(imgResize.shape)

imgCropped = imgResize[0:200,200:640]

# cv2.imshow("Image ", img)

cv2.imshow("Image Resized", imgResize)
cv2.imshow("Cropped Image", imgCropped)

cv2.waitKey(0)