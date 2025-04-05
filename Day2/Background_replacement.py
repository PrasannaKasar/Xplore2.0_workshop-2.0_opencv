import cv2
import mediapipe as mp
import numpy as np

# Load background image
bg_image = cv2.imread("images/mountain.jpg")
bg_image = cv2.resize(bg_image, (640, 480))

# Initialize MediaPipe Selfie Segmentation
mp_selfie_segmentation = mp.solutions.selfie_segmentation
segmentor = mp_selfie_segmentation.SelfieSegmentation(model_selection=1)

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, flipCode=1)

    frame = cv2.resize(frame, (640, 480))
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Get segmentation mask
    results = segmentor.process(frame_rgb)
    mask = results.segmentation_mask

    # Threshold to create binary mask
    condition = mask > 0.5
    condition = np.stack((condition,) * 3, axis=-1)  # Make 3-channel

    # Combine foreground with background image
    output_image = np.where(condition, frame, bg_image)

    cv2.imshow("Virtual Background (No Green Screen)", output_image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
