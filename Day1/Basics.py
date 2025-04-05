import cv2
import numpy as np

# load image (use any image file in the same folder)
image = cv2.imread('images/car.jpg')  
cv2.imshow('Original Image', image)

# -------------------- IMAGE BASICS --------------------

# # shape of the image
# print("Image shape:", image.shape)

# height, width, channels = image.shape
# print("Height:", height)
# print("Width:", width)
# print("Channels (BGR):", channels)

# # accessing pixel value
# pix = image[100, 100]
# print("Pixel value at (100,100):", pix)


# ------------------- SPLITTING CHANNELS --------------------

# # split image into blue, green, red channels
# blue, green, red = cv2.split(image)

# zeros = np.zeros_like(blue)

# only_blue = cv2.merge([blue, zeros, zeros])
# cv2.imshow("Blue", only_blue)

# only_green = cv2.merge([zeros, green, zeros])
# cv2.imshow("Green", only_green)

# only_red = cv2.merge([zeros, zeros, red])
# cv2.imshow("Red", only_red)

# ------------------- BASIC OPERATIONS -------------------

# # resize
# resized = cv2.resize(image, (300, 300))
# cv2.imshow('Resized Image', resized)

# # crop
# cropped = image[50:200, 100:300]
# cv2.imshow('Cropped Image', cropped)

# # flip (0: vertical, 1: horizontal, -1: both)
# flipped = cv2.flip(image, 1)
# cv2.imshow('Flipped Image', flipped)

# # saving image
# cv2.imwrite('flipped_image.jpg', flipped)


# Cleanup
cv2.waitKey(0)
cv2.destroyAllWindows()
