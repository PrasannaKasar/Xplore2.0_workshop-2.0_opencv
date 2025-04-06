# Background Removal

# What You’ll Do:
# 1. Use your webcam to see yourself.
# 2. Replace your real background with a cool background picture.
# 3. Use sliders to pick a  hsv color to keep you in the picture.
# 4. Watch the "Mask" window: make yourself white there by moving sliders :)
# 5. Have fun seeing yourself with a new background!

 # TODO: Move sliders until you are white in mask window!


import cv2 
import numpy as np  

# Step 1: Load the picture we’ll use as the new background
bg_image = cv2.imread("images/mountain.jpg")  
bg_image = cv2.resize(bg_image, (640, 480))  

# Step 2: Turn on your webcam
cap = cv2.VideoCapture(0)  # 0 means your default webcam
if not cap.isOpened():  
    print("Uh-oh! Webcam not working. Is it plugged in?")
    exit()

# Making a slidebar
cv2.namedWindow("Background Removal")

def nothing(x): 
    pass

cv2.createTrackbar("Lower Hue", "Background Removal", 0, 180, nothing)  
cv2.createTrackbar("Upper Hue", "Background Removal", 30, 180, nothing) 
cv2.createTrackbar("Lower Sat", "Background Removal", 50, 255, nothing) 
cv2.createTrackbar("Upper Sat", "Background Removal", 255, 255, nothing)
cv2.createTrackbar("Lower Val", "Background Removal", 50, 255, nothing) 
cv2.createTrackbar("Upper Val", "Background Removal", 255, 255, nothing)

while cap.isOpened():
    ret, frame = cap.read()  

    frame = cv2.resize(frame, (640, 480))  
    frame = cv2.flip(frame, 1)  

    # Step 3: Change the picture to HSV (a fun way to pick colors)
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  

    # For choosing slider value
    lower_hue = cv2.getTrackbarPos("Lower Hue", "Background Removal")
    upper_hue = cv2.getTrackbarPos("Upper Hue", "Background Removal")
    lower_sat = cv2.getTrackbarPos("Lower Sat", "Background Removal")
    upper_sat = cv2.getTrackbarPos("Upper Sat", "Background Removal")
    lower_val = cv2.getTrackbarPos("Lower Val", "Background Removal")
    upper_val = cv2.getTrackbarPos("Upper Val", "Background Removal")

    # Setting the color range dynamically using sliders
    lower_color = np.array([lower_hue, lower_sat, lower_val])
    upper_color = np.array([upper_hue, upper_sat, upper_val])

    # Step 4: Make a mask (white = you, black = background)
    mask = cv2.inRange(hsv_frame, lower_color, upper_color)  
    mask = cv2.GaussianBlur(mask, (5, 5), 0)  # Blurring it a little
    cv2.imshow("Mask (White = You)", mask)


    # Step 5: Split the picture into you and the mountain
    foreground = cv2.bitwise_and(frame, frame, mask=mask)  # Keep you where the mask is white
    inverse_mask = cv2.bitwise_not(mask)  # flips the mask (black becomes white, white becomes black)
    background = cv2.bitwise_and(bg_image, bg_image, mask=inverse_mask)  # Keep mountain where mask is black

    # Step 6: Put you and the mountain together
    final_image = cv2.add(foreground, background)  
    cv2.imshow("Virtual Background Fun", final_image)

    # Step 7: Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()  
cv2.destroyAllWindows()  