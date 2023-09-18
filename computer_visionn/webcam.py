import cv2
import numpy as np

# create a videoCaptureobject
WEBCAM_IDX = 0
cam = cv2.VideoCapture(WEBCAM_IDX)
while cam.isOpened():
    # Capture image from camera
    state, image = cam.read()
    if not state: break # if state is none then break loop
    # show image
    cv2.imshow('image', image)
    # wait for key press
    key = cv2.waitKey(10)
    # if ESC ke is pressed, exit loop
    if key == 27:
        break
# Capture image from camera
state, image = cam.read()

# show image
cv2.imshow('image', image)

# wait for key press
cv2.waitKey(0)

# release camera
cam.release()
cv2.destroyAllWindows()