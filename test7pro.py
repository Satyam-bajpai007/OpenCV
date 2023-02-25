# In this we learn about to extract the image in the given image
# with the help of mouseclick.

import cv2
import numpy as np

circle = np.zeros((4, 2), np.int32)
counter = 0

def mouse_click(event,x,y,flags,params):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        circle[counter] = x, y
        counter = counter + 1
        print(circle)

path = "iv/image/card.png"
img = cv2.imread(path)

while True:
    if counter == 4:
        width, height = 250, 350
        pts1 = np.float32([circle[0], circle[1], circle[2], circle[3]])
        pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        img_out = cv2.warpPerspective(img, matrix, (width, height))
        cv2.imshow("Extracted Image", img_out)
        # print(pts1[0][0], pts1[0][1])

    for i in range(4):
        cv2.circle(img, (circle[i][0], circle[i][1]), 5, (255, 0, 0), cv2.FILLED)

    cv2.imshow("Original Image", img)
    cv2.setMouseCallback("Original Image", mouse_click)
    cv2.waitKey(1)
