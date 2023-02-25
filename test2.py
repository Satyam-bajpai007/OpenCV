# 5 Basic function for image transition

import cv2
import numpy as np

kernel = np.ones((5, 5), np.uint8)
print(kernel)

path = "cutie.png"

img = cv2.imread(path)
img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_blur = cv2.GaussianBlur(img, (5, 5), 0)
img_canny = cv2.Canny(img, 100, 100)
img_dilation = cv2.dilate(img_canny, kernel, iterations=1)
img_eroded = cv2.erode(img_canny, kernel, iterations=2)

# cv2.imshow("Original", img)
# cv2.imshow("Grey", img_grey)
# cv2.imshow("Blur", img_blur)
cv2.imshow("Canny", img_canny)
cv2.imshow("Dilation", img_dilation)
cv2.imshow("Eroded", img_eroded)

cv2.waitKey(0)
