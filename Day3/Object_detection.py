# Object Detection using Color

# What You’ll Do:
# 1. Open your webcam and click on any colored object 
# 2. The program remembers the color and tracks anything matching that color.
# 3. It draws a green box around the object in real time.
# 4. You can also view the mask (black & white) showing only the selected color.
# 5. Press 'q' to quit the program.

import cv2
import numpy as np

# Step 1: Turn on the webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Webcam not found. Please check the connection.")
    exit()

# Create a display window
window_name = "Object Detector"
cv2.namedWindow(window_name)

# This variable will store the hue value when a color is selected
selected_hue = None
hue_range = 20  # +/- value for hue range

# Step 2: Define a function to select color from the webcam frame
def pick_color(event, x, y, flags, param):
    global selected_hue
    if event == cv2.EVENT_LBUTTONDOWN:
        frame = param
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        clicked_pixel = hsv[y, x]
        selected_hue = int(clicked_pixel[0])
        print("Selected Hue:", selected_hue)

# Step 3: Continuously read from the webcam
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame horizontally for a mirror effect
    frame = cv2.flip(frame, 1)
    display_frame = frame.copy()

    # Set the mouse click callback
    cv2.setMouseCallback(window_name, pick_color, frame)

    # Step 4: If a hue has been selected, detect objects of that color
    if selected_hue is not None:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Define color boundaries for the mask
        lower_bound = np.array([max(0, selected_hue - hue_range), 120, 100])
        upper_bound = np.array([min(180, selected_hue + hue_range), 255, 255])

        # Create a binary mask where the selected color is white
        mask = cv2.inRange(hsv, lower_bound, upper_bound)

        # Clean up the mask using erosion and dilation
        mask = cv2.erode(mask, None, iterations=3)
        mask = cv2.dilate(mask, None, iterations=3)

        # Step 5: Find contours in the mask
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 800:
                x, y, w, h = cv2.boundingRect(cnt)
                # Draw a rectangle around the detected object
                cv2.rectangle(display_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(display_frame, "Detected Object", (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        # Show the mask window
        cv2.imshow("Mask", mask)

    # Show the main webcam window
    cv2.imshow(window_name, display_frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Step 6: Release resources
cap.release()
cv2.destroyAllWindows()
