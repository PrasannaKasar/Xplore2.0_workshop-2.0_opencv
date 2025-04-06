# Face Detection with Webcam

# What You’ll Do:
# 1. Turn on your webcam to see yourself.
# 2. Use a special tool to find faces in the picture.
# 3. Draw yellow boxes around every face it spots!
# 4. Try be more precise by making a circle to frame your face
# 5. Press 'q' to stop when you’re done.

import cv2  

# Step 1: Load a face finding tool
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Step 2: Turn on your webcam
cap = cv2.VideoCapture(0)  # 0 means your default webcam
if not cap.isOpened():  
    print("Uh-oh! Webcam not working. Is it plugged in?")
    exit()

while True:
    ret, frame = cap.read() 
    frame = cv2.flip(frame, 1)   

    # Step 3: Turn the picture to black and white (helps find faces)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Step 4: Look for faces in the picture
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Step 5: Draw yellow boxes around face we find
    for (x, y, w, h) in faces:  # x, y is the top-left corner, w, h is width and height
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)  

#-----------------------------------------------------------------------------------------
        # TODO: Write your code here to draw a red circle in the middle of the face!

        # Hint: Calculate the center center_x, center_y
        # Example goal: cv2.circle(frame, (center_x, center_y), 20, (0, 0, 255), 2)
#------------------------------------------------------------------------------------------

    cv2.imshow('Face Detection (Haar Cascade)', frame)

    # Step 6: Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()  
cv2.destroyAllWindows()  