import cv2
import numpy as np

img = cv2.imread('images/mona_lisa.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Mona Lisa', img)

def nothing(x):
    pass

cv2.namedWindow('Morphology Transformer')
cv2.createTrackbar('Kernel Size', 'Morphology Transformer', 3, 15, nothing)
cv2.createTrackbar('Operation', 'Morphology Transformer', 0, 3, nothing) 
cv2.createTrackbar('Iterations', 'Morphology Transformer', 1, 5, nothing)

while True:
    kernel_size = cv2.getTrackbarPos('Kernel Size', 'Morphology Transformer')
    operation = cv2.getTrackbarPos('Operation', 'Morphology Transformer')
    iterations = cv2.getTrackbarPos('Iterations', 'Morphology Transformer')
    
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    
    if operation == 0:
        result = cv2.erode(img, kernel, iterations=iterations)
    elif operation == 1:
        result = cv2.dilate(img, kernel, iterations=iterations)
    elif operation == 2:
        result = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations=iterations)
    else:
        result = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel, iterations=iterations)
    
    cv2.imshow('Morphology', result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()