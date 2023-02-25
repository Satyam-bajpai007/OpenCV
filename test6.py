# Wrap Perspective and bird view in OpenCV

import cv2
import numpy as np

path = "Vid-Im/card.png"
img = cv2.imread(path)
width, height = 250, 350

pts1 = np.float32([[310, 38], [483, 123], [190, 293], [362, 378]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
img_out = cv2.warpPerspective(img, matrix, (width, height))

# print(pts1[0][0], pts1[0][1])

for i in range(4):
    cv2.circle(img, (int(pts1[i][0]), int(pts1[i][1])), 5, (255, 0, 0), cv2.FILLED)

cv2.imshow("Original Image", img)
cv2.imshow("Extracted Image", img_out)

cv2.waitKey(0)
