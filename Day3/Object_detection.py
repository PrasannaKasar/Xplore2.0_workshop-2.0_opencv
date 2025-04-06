# Pen Detection with Webcam

# What You’ll Do:
# 1. Use a slider to find just the right blue for your pen
# 2. Draw green boxes and labels around your blue pen when it spots it
# 3. Hold up your pen and slide the Hue to lock it around
# 4.  Check the "Mask" window: Pen should be white, noise should be black

import cv2  
import numpy as np  

# Step 1: Turn on your webcam
cap = cv2.VideoCapture(0) 
if not cap.isOpened():  
    print("Uh-oh! Webcam not working. Is it plugged in?")
    exit()

# Making a slider to tune the color
window_name = "Pen Detection"
cv2.namedWindow(window_name)
def nothing(x):  
    pass
cv2.createTrackbar("Hue Center", window_name, 110, 180, nothing)

while True:
    ret, frame = cap.read()  
    frame = cv2.flip(frame, 1) 

    # Step 3: Change the picture to HSV 
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Step4: Setting a color range
    hue_center = cv2.getTrackbarPos("Hue Center", window_name)
    hue_range = 20
    lower_bound = np.array([max(0, hue_center - hue_range), 120, 100]) 
    upper_bound = np.array([min(180, hue_center + hue_range), 255, 255]) 

    # Step 5: Make and clean the mask 
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    mask = cv2.erode(mask, None, iterations=3)  
    mask = cv2.dilate(mask, None, iterations=3) 


    # Step 6: Draw green boxes and labels around big blue objects
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 800:  
            x, y, w, h = cv2.boundingRect(cnt)  
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)  # Green box
            cv2.putText(frame, "Blue Pen", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)  

    cv2.imshow(window_name, frame)  
    cv2.imshow("Mask", mask) 

    # Step 9: Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()  
cv2.destroyAllWindows()  