import cv2
import numpy as np
import time

# Start webcam
cap = cv2.VideoCapture(0)
time.sleep(2)

# Capture the background
print("Capturing background... Please move out of the frame.")
for i in range(100):
    ret, background = cap.read()
    if not ret:
        continue
background = np.flip(background, axis=1)

print("Done! Now hold up your white paper.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame (mirror view)
    frame = np.flip(frame, axis=1)

    # Convert frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define white color range in HSV
    lower_white = np.array([0, 0, 200])
    upper_white = np.array([180, 40, 255])

    # Create mask to detect white color
    white_mask = cv2.inRange(hsv, lower_white, upper_white)

    # Remove noise from the mask
    kernel = np.ones((5, 5), np.uint8)
    white_mask = cv2.morphologyEx(white_mask, cv2.MORPH_OPEN, kernel, iterations=2)
    white_mask = cv2.dilate(white_mask, kernel, iterations=1)

    # Inverted mask to segment out non-white regions
    mask_inv = cv2.bitwise_not(white_mask)

    # Segment out non-white parts from the frame
    res1 = cv2.bitwise_and(frame, frame, mask=mask_inv)

    # Segment out the white parts from the saved background
    res2 = cv2.bitwise_and(background, background, mask=white_mask)

    # Combine both results to get final output
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)

    # Display the output
    cv2.imshow("Invisibility Cloak - White", final_output)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
