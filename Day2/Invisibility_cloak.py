# Invisibility Cloak with White Paper!

# What You’ll Do:
# 1. Your webcam will turn on.
# 2. You’ll capture the background without you in the frame.
# 3. Then, hold up a white paper.
# 4. Wherever the paper appears, it will be replaced with the background.
# 5. You’ll look like you're disappearing behind the white paper :)

# Step 1: Import libraries
import cv2
import numpy as np
import time

# Step 2: Turn on the webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Oops! Webcam not working.")
    exit()

# Step 3: Capture background
print("Capturing background... Please move out of the frame.")
time.sleep(2)  # Short pause to let the camera adjust

for i in range(100):
    ret, background = cap.read()
    if not ret:
        continue

# Flip the background for mirror effect
background = cv2.flip(background, 1)

print("Done! Now hold up your white paper to become invisible!")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Step 4: Flip the current frame (mirror effect)
    frame = cv2.flip(frame, 1)

    # Step 5: Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Step 6: Define the range for white color in HSV
    lower_white = np.array([0, 0, 200])     
    upper_white = np.array([180, 40, 255])  

    # Step 7: Create a mask where white regions are detected
    white_mask = cv2.inRange(hsv, lower_white, upper_white)

    # Step 8: Clean the mask using morphological operations
    kernel = np.ones((5, 5), np.uint8)
    white_mask = cv2.morphologyEx(white_mask, cv2.MORPH_OPEN, kernel, iterations=2)
    white_mask = cv2.dilate(white_mask, kernel, iterations=1)

    # Step 9: Invert the mask (white -> black, black -> white)
    mask_inv = cv2.bitwise_not(white_mask)

    # Step 10: Create two separate images:
    # (a) Keep only the non-white part of the current frame
    you_part = cv2.bitwise_and(frame, frame, mask=mask_inv)

    # (b) Keep only the white part from the background (behind the paper)
    bg_part = cv2.bitwise_and(background, background, mask=white_mask)

    # Step 11: Add both parts to get the final output
    final_output = cv2.add(you_part, bg_part)

    # Step 12: Show the results
    cv2.imshow("White Cloak Magic!", final_output)

    # Step 13: Quit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Step 14: Release resources
cap.release()
cv2.destroyAllWindows()
