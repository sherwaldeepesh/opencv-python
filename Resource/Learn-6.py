import cv2
import numpy as np

img = cv2.imread("Resource/lena.png")

imghor = np.hstack((img,img))
imgver = np.vstack((img,img))

cv2.imshow("Horizontal", imghor)
cv2.imshow("Vetical",imgver)

cv2.waitKey(0)