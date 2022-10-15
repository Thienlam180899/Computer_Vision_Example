import cv2

# Capture image
cap = cv2.VideoCapture(0)

# When everything done, release the capture
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    img = cv2.cvtColor(frame, 1)

    # Display the resulting frame
    cv2.imshow('frame', img)

    # Type character s to save image
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite('Image.png', img)
    
    # Type character q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()