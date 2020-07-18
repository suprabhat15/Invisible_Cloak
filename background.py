import cv2
cap = cv2.VideoCapture(0) # this is the webcam

while cap.isOpened():
    ret, back = cap.read() #simply reading from the webcam
    #back is what the camera is reading
    if ret:
        cv2.imshow("image",back)
        if cv2.waitKey(5) == ord('q'):
            #save the image
            cv2.imwrite('image.jpg',back)
            break
cap.release()
cv2.destroyAllWindows()