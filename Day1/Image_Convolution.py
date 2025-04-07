import cv2
import numpy as np

# Load the image
image = cv2.imread('bird.png')  # Replace with your image path

# Grayscale filter
def apply_gray(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

# Negative filter
def apply_negative(img):
    return 255 - img

# Blur filter
def apply_blur(img):
    kernel = (1/16) * np.array([[1, 2, 1],
                                [2, 4, 2],
                                [1, 2, 1]])
    return cv2.filter2D(img, -1, kernel)

# Sharpen filter
def apply_sharpen(img):
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
    return cv2.filter2D(img, -1, kernel)

# Sobel Edge Detection
def apply_sobel(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    sobel = cv2.magnitude(sobel_x, sobel_y)
    sobel = np.clip(sobel, 0, 255).astype(np.uint8)
    return cv2.cvtColor(sobel, cv2.COLOR_GRAY2BGR)

# Apply and display each filter
# cv2.imshow('Original', image)
# cv2.imshow('Gray', apply_gray(image))
# cv2.imshow('Negative', apply_negative(image))
# cv2.imshow('Blur', apply_blur(image))
# cv2.imshow('Sharpen', apply_sharpen(image))
cv2.imshow('Sobel', apply_sobel(image))

cv2.waitKey(0)
cv2.destroyAllWindows()
