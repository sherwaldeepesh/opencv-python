#Import Opencv Package
import cv2

#read Image and display
# img = cv2.imread('Resource/t1.jpg')

# cv2.imshow("output",img)

# cv2.waitKey(0)

#read video and display
# cap = cv2.VideoCapture("Resource/Marshmello - Alone (Official Music Video).mp4")

# while True:
#     success,img = cap.read()
#     cv2.imshow("Video",img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

#Read Video from Webcam and Display
cap = cv2.VideoCapture(0) #insert id of webcam
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)      #for brightness

while True:
    success,img = cap.read()
    cv2.imshow("Video",cv2.flip(img,1))     #By default it will send mirror image but can correct it using cv2.flip
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
