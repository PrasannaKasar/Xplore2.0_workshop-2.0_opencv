# Morphology

# What You’ll Do:
# 1. Load a picture we made with shapes and dots.
# 2. Use sliders to change operation you perform:
#    - Shrink stuff (Erosion, slider at 0): makes white things smaller.
#    - Grow stuff (Dilation, slider at 1): makes white things bigger.
#    - Clean up dots (Opening, slider at 2): memoves tiny white spots.
#    - Fill holes (Closing, slider at 3): fills black gaps in white shapes.
# 3. Move the sliders to change kernel size and no. of iteration


import cv2  
import numpy as np  


# Step 1: Load our picture in black and white
img = cv2.imread('images/morphology.jpg', cv2.IMREAD_GRAYSCALE) 
if img is None:  # If it doesn’t load, tell us
    print("Oops! Couldn’t find image. Did you run the first script?")
    exit()
cv2.imshow("Original Image", img) 

# Making a fun window with sliders
window_name = 'Morphology Transformer'  
cv2.namedWindow(window_name)
def nothing(x):  
    pass
cv2.createTrackbar('Kernel Size', window_name, 3, 15, nothing) 
cv2.createTrackbar('Operation', window_name, 0, 3, nothing)    
cv2.createTrackbar('Iterations', window_name, 1, 5, nothing)   


while True:
    # Gettinig the slider values
    kernel_size = cv2.getTrackbarPos('Kernel Size', window_name)  
    operation = cv2.getTrackbarPos('Operation', window_name)      
    iterations = cv2.getTrackbarPos('Iterations', window_name)    

    # Step 2: Define a dyanamic kernel 
    kernel = np.ones((kernel_size, kernel_size), np.uint8)  

    # Step 3: Define conditions to perform operations
    
    if operation == 0:  # Shrink (Erosion)
        result = cv2.erode(img, kernel, iterations=iterations)  
    elif operation == 1:  # Grow (Dilation)
        result = cv2.dilate(img, kernel, iterations=iterations) 
    elif operation == 2:  # Clean up (Opening)
        result = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations=iterations)  
    else:  # Fill holes (Closing)
        result = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel, iterations=iterations) 

    cv2.imshow(window_name, result)

    # Step 4: Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()  