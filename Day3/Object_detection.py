# Blue Pen Detection with Webcam

# What You’ll Do:
# 1. Turn on your webcam to see yourself and stuff around you.
# 2. Use a slider to find just the right blue for your pen—no extra noise!
# 3. Draw green boxes and labels around your blue pen when it spots it!
# 4. Hold up your blue pen and slide the Hue to lock on—wave it around!
# 5. Press 'q' to stop when you’re done.

# TODO: 
# 1. Run this code, hold up your blue pen, and slide the "Hue Center" until it’s the only thing boxed!
# 2. Move it closer or farther—find the sweet spot where it’s clean!
# Tips:
# - Start around 110-120 (typical blue pen Hue).
# - Check the "Mask" window: Pen should be white, noise should be black!

import cv2  # This helps us use the webcam and draw stuff
import numpy as np  # This helps us work with numbers and colors

# Step 1: Turn on your webcam
cap = cv2.VideoCapture(0)  # 0 means your default webcam
if not cap.isOpened():  # Make sure it works
    print("Uh-oh! Webcam not working. Is it plugged in?")
    exit()

# Step 2: Make a window with a slider to tune the blue color
window_name = "Blue Pen Detection"
cv2.namedWindow(window_name)
def nothing(x):  # This helps the slider work
    pass
# Slider for Hue center (0-180), starting at 110 (typical blue)
cv2.createTrackbar("Hue Center", window_name, 110, 180, nothing)

# Keep going until you press 'q'
while True:
    ret, frame = cap.read()  # Grab a picture from the webcam
    if not ret:  # If it fails, stop
        print("Oops! Couldn’t get a picture from the webcam.")
        break

    frame = cv2.flip(frame, 1)  # Flip it like a mirror so it feels natural

    # Step 3: Change the picture to HSV (to find blue)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Step 4: Get the slider value and set a tight blue range around it
    hue_center = cv2.getTrackbarPos("Hue Center", window_name)
    hue_range = 20  # Tight range (±20 from center) to reduce noise
    lower_bound = np.array([max(0, hue_center - hue_range), 120, 100])  # Start of blue
    upper_bound = np.array([min(180, hue_center + hue_range), 255, 255])  # End of blue

    # Step 5: Make a mask (white = your blue pen, black = everything else)
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    # Step 6: Clean up the mask to cut noise
    mask = cv2.erode(mask, None, iterations=3)  # Shrink more to zap tiny specks
    mask = cv2.dilate(mask, None, iterations=3)  # Grow back to keep the pen

    # Find the shapes of blue things in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Step 7: Draw green boxes and labels around big blue objects
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 800:  # Higher threshold to ignore small noise
            x, y, w, h = cv2.boundingRect(cnt)  # Get the box around the object
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)  # Green box
            cv2.putText(frame, "Blue Pen", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)  # Green label

    # Step 8: Show the picture and mask
    cv2.imshow(window_name, frame)  # See the box on your blue pen!
    cv2.imshow("Mask", mask)  # See what’s white (just the pen, hopefully!)

    # Step 9: Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up when you’re done
cap.release()  # Turn off the webcam
cv2.destroyAllWindows()  # Close the windows