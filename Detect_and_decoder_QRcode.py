import cv2
import numpy as np
from pyzbar.pyzbar import decode
# initalize the camera
cap = cv2.VideoCapture(0)
cap.set(3, 6400)
cap.set(4, 480)

while True:
  success, img = cap.read()
  for barcode in decode(img):
    print(barcode.data)
    myData = barcode.data.decode('utf-8')
    print(myData)
    pts = np.array([barcode.polygon],np.int32)
    pts = pts.reshape((-1,1,2))
    cv2.polylines(img, [pts], True, (255, 0, 255), 5)

    pts2 = barcode.rect
    cv2.putText(img, myData, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 0.9, (255, 0, 255))

  # display the result
  cv2.imshow("Result", img)

  # Save code into text file
  if cv2.waitKey(1) == ord("s"):
    f = open('QRcodeData.txt', "a")
    f.write(myData)
    f.write("\n")


  # Enter q to Quit
  if cv2.waitKey(1) == ord("q"):
    break

cap.release()
cv2.destroyAllWindows()