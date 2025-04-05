import cv2
import numpy as np

# blank canvas
canvas = np.zeros((500, 500, 3), np.uint8)

#--------------------------------RECTANGLE-----------------------------------------------------

top_left = (170, 270)
bottom_right = (330, 310)

for y in range(top_left[1], bottom_right[1]):
    for x in range(top_left[0], bottom_right[0]):
        canvas[y, x] = (50, 180, 200) # tweak the pixel values to change color

# Direct way:
# cv2.rectangle(canvas, (210, 90), (290, 120), (80, 80, 80), -1)

#------------------------------------LINE-----------------------------------------------------

# TODO 1: Draw a straight horizontal line using a for loop

# Example goal: from (70, 230) to (150, 230), color = green (200, 200, 200)
# Hint: Loop over x for horizontal line

# Direct way:
# cv2.line(canvas, (350, 230), (430, 230), (200, 200, 200), 1)

#---------------------------------- CIRCLE ------------------------------------------------------


# TODO 2: Draw a filled circle using nested for loops

# Example goal: center = (350, 150), radius = 50, color = Red (0, 200, 255)
# Hint: Use the circle equation: (x - cx)^2 + (y - cy)^2 <= radius^2

# for y in range(...):
#     for x in range(...):
#         if (x - cx)**2 + (y - cy)**2 <= r**2:
#             canvas[y, x] = (0, 0, 255)

# Direct way:
# cv2.circle(canvas, (310, 160), 30, (0, 200, 255), -1)

#------------------------------- ELLIPSE & TRIANGLE -------------------------------------------------------

# cv2.ellipse(canvas, (250, 220), (180, 200), 0, 0, 360, (100, 100, 200), 4)  

# triangle = np.array([[250, 210], [230, 250], [270, 250]])
# cv2.fillPoly(canvas, [triangle], color=(255, 100, 100))

#-------------------------------------- TEXT -------------------------------------------------------

# cv2.putText(canvas, "XploreBot", (170, 475), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)


cv2.imshow('Shape', canvas)

cv2.waitKey(0) 
cv2.destroyAllWindows()