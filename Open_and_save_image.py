import cv2

# Capture image
img = 'Vietdynamic.png'
image = cv2.imread(img)

# When everything done, release the capture
while(True):
    # Display the image
    cv2.imshow('image', image)

    # Type character s to save image
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite('Vietdynamic_Coppy.png', image)
    
    # Type character q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
image.release()
cv2.destroyAllWindows()