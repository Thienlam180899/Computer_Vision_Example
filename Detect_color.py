import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# define range of blue color in HSV
#lower = np.array([169, 100, 100])
#upper = np.array([189, 255, 255])

# define range of blue color in HSV
#lower = np.array([110, 50, 50])
#upper = np.array([130, 255, 255])

# define range of green color in HSV
lower = np.array([25, 52, 72])
upper = np.array([102, 255, 255])

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    
    
    k = cv2.waitKey(1)  
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
