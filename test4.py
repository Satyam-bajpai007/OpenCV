# How to draw text and shape in OpenCV

import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
# print(img)

cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 256, 0), 1)
cv2.rectangle(img, (350, 100), (450, 200), (128, 128, 0), cv2.FILLED)
cv2.circle(img, (150, 400), 60, (1286, 0, 128), cv2.FILLED)
cv2.putText(img, "Hello World!", (85, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (80, 70, 80), 3)

cv2.imshow("Image", img)
cv2.waitKey(0)
