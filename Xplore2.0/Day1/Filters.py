import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
filter_mode = 'normal'

def sepia(frame):
  sepia_filter = np.array([[0.272, 0.534, 0.131],
                          [0.349, 0.686, 0.168],
                          [0.393, 0.769, 0.189]])
  sepia_frame = cv.transform(frame, sepia_filter)
  return np.clip(sepia_frame, 0, 255).astype(np.uint8)

def negative(frame):
  return 255-frame

while True:
  ret, frame = cap.read()
  if not ret:
    break

  if filter_mode=='gray':
    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
  elif filter_mode == 'sepia':
    frame = sepia(frame)
  elif filter_mode == 'negative':
    frame = negative(frame)

  cv.imshow(f"Live Cam filter = {filter_mode}", frame)

  key = cv.waitKey(1) & 0xFF
  if key == ord('q'):
    break
  elif key == ord('g'):
    filter_mode = 'gray'
  elif key == ord('s'):
    filter_mode = 'sepia'
  elif key == ord('n'):
    filter_mode = 'negative'
  elif key == ord('r'):
    filter_mode = 'normal'


cap.release()
cv.waitKey(0)
cv.destroyALLWindows()
