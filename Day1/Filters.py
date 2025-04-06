import cv2
import numpy as np

def sepia(frame):
    sepia_filter = np.array([[0.272, 0.534, 0.131],
                             [0.349, 0.686, 0.168],
                             [0.393, 0.769, 0.189]])
    
    #explain what is transform and clip function

    sepia_frame = cv2.transform(frame, sepia_filter)
    return np.clip(sepia_frame, 0, 255).astype(np.uint8)

def gaussian_blur(frame):
    kernel_3x3 = (1/16) * np.array([
        [1, 2, 1],
        [2, 4, 2],
        [1, 2, 1]
    ])
    #explain what is filter2d 
    return cv2.filter2D(frame, -1, kernel_3x3)

def sharpen(frame):
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
    return cv2.filter2D(frame, -1, kernel)

def negative(frame):
    return 255 - frame

# def sobel(frame):
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
#     sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
#     sobel_combined = cv2.magnitude(sobel_x, sobel_y)
#     sobel_combined = np.clip(sobel_combined, 0, 255).astype(np.uint8)
#     return cv2.cvtColor(sobel_combined, cv2.COLOR_GRAY2BGR)

cap = cv2.VideoCapture(0)
filter_mode = 'normal'

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if filter_mode == 'gray':
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
    elif filter_mode == 'sepia':
        frame = sepia(frame)
    elif filter_mode == 'negative':
        frame = negative(frame)
    elif filter_mode == 'blur':
        frame = gaussian_blur(frame)
    elif filter_mode == 'sharpen':
        frame = sharpen(frame)
    # elif filter_mode == 'sobel':
    #     frame = sobel(frame)

    cv2.imshow("Live Video", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('g'):
        filter_mode = 'gray'
    elif key == ord('s'):
        filter_mode = 'sepia'
    elif key == ord('n'):
        filter_mode = 'negative'
    elif key == ord('b'):
        filter_mode = 'blur'
    elif key == ord('h'):
        filter_mode = 'sharpen'
    elif key == ord('e'):
        filter_mode = 'sobel'
    elif key == ord('r'):
        filter_mode = 'normal'

cap.release()
cv2.destroyAllWindows()