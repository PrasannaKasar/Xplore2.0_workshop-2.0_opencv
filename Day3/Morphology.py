import cv2
import numpy as np

img = cv2.imread('images/mona_lisa.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow("Original Image", img)
 
def nothing(x):
    pass

# Use the same window name for display and trackbars
window_name = 'Morphology Transformer'
cv2.namedWindow(window_name)
cv2.createTrackbar('Kernel Size', window_name, 3, 15, nothing)
cv2.createTrackbar('Operation', window_name, 0, 3, nothing) 
cv2.createTrackbar('Iterations', window_name, 1, 5, nothing)

while True:
    kernel_size = cv2.getTrackbarPos('Kernel Size', window_name)
    operation = cv2.getTrackbarPos('Operation', window_name)
    iterations = cv2.getTrackbarPos('Iterations', window_name)

    kernel = np.ones((kernel_size, kernel_size), np.uint8)

    if operation == 0:
        result = cv2.erode(img, kernel, iterations=iterations)
    elif operation == 1:
        result = cv2.dilate(img, kernel, iterations=iterations)
    elif operation == 2:
        result = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations=iterations)
    else:
        result = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel, iterations=iterations)

    cv2.imshow(window_name, result) 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
