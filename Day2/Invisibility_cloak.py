import cv2
import numpy as np
import time

# Start webcam
cap = cv2.VideoCapture(0)
time.sleep(2)

# Capture the background
print("Capturing background... Please move out of the frame.")
for i in range(30):
    ret, background = cap.read()
background = np.flip(background, axis=1)

print("Done! Now hold up your red handkerchief.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame (mirror view)
    frame = np.flip(frame, axis=1)

    # Convert frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define red color ranges (two ranges for HSV wrap-around)
    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])

    # Create masks for both red ranges
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

    # Combine masks
    red_mask = mask1 + mask2

    # Clean up the mask
    kernel = np.ones((5, 5), np.uint8)
    red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_OPEN, kernel, iterations=2)
    red_mask = cv2.dilate(red_mask, kernel, iterations=1)

    # Inverted mask for everything except red
    mask_inv = cv2.bitwise_not(red_mask)

    # Segment out non-red parts of the frame
    res1 = cv2.bitwise_and(frame, frame, mask=mask_inv)

    # Replace red parts with background
    res2 = cv2.bitwise_and(background, background, mask=red_mask)

    # Combine both results
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)

    # Display
    cv2.imshow("Invisibility Cloak - Red", final_output)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release and destroy
cap.release()
cv2.destroyAllWindows()
