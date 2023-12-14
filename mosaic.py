video_file = 'aspa.mp4'
cap = cv2.VideoCapture(video_file)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Adjust the scaleFactor and minSize for better face recognition at a distance
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
  
        for (x, y, w, h) in faces:
            # Blur the face region to create a mosaic effect
            face_roi = frame[y:y+h, x:x+w]
            face_roi = cv2.resize(face_roi, (w // 10, h // 10))  # Resize the face region
            face_roi = cv2.resize(face_roi, (w, h), interpolation=cv2.INTER_NEAREST)  # Resize it back to original size
            frame[y:y+h, x:x+w] = face_roi  # Replace the original face region with the resized one

        cv2.imshow('Video', frame)
       
        if cv2.waitKey(50) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
