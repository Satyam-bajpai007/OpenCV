# Read image and video using OpenCV

import cv2

# img = cv2.imread("cutie.png")
#
# cv2.imshow("Cutie", img)
# cv2.waitKey(0)

framewidth = 620
frameheight = 500

vid = cv2.VideoCapture(0)
# vid.set(3, framewidth)
# vid.set(4, frameheight)

while True:
    sucess, img = vid.read()
    img = cv2.resize(img, (framewidth, frameheight))
    cv2.imshow("Bleach", img)
    print(sucess)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

