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

    cv2.imshow("Background Removal", frame)

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


#-------------------------------------TRY IT AT HOME------------------------------------------------

#-------------------------------------USING MEDIAPIPE------------------------------------------------

# import cv2
# import mediapipe as mp
# import numpy as np

# # Step 1: Load your cool background image 
# bg_image = cv2.imread("images/mountain.jpg")
# bg_image = cv2.resize(bg_image, (640, 480)) 

# # Step 2: Turn on your webcam
# cap = cv2.VideoCapture(0)
# if not cap.isOpened():
#     print("Webcam not detected! Check if it's connected properly.")
#     exit()

# # Step 3: Initialize MediaPipe's Selfie Segmentation model
# mp_selfie_segmentation = mp.solutions.selfie_segmentation
# segmentor = mp_selfie_segmentation.SelfieSegmentation(model_selection=1)  # 0 = fast, 1 = accurate

# # Step 4: Process webcam frames in a loop
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     frame = cv2.resize(frame, (640, 480))  
#     frame = cv2.flip(frame, 1)  

#     # Step 5: Convert to RGB (MediaPipe needs this)
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#     # Step 6: Get the segmentation mask (person vs. background)
#     results = segmentor.process(rgb_frame)
#     mask = results.segmentation_mask

#     # Step 7: Create a binary condition mask — where the person is
#     condition = mask > 0.5  # You can tweak this threshold for sharper detection

#     # Step 8: Resize background to match the webcam frame
#     bg_resized = cv2.resize(bg_image, (frame.shape[1], frame.shape[0]))

#     # Step 9: Combine the person and the new background using the mask
#     output_image = np.where(condition[..., None], frame, bg_resized)

#     # Step 10: Show the final output
#     cv2.imshow("Virtual Background (MediaPipe)", output_image)

#     # Step 11: Press 'q' to quit
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Cleanup
# cap.release()
# cv2.destroyAllWindows()
