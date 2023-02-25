# Detecting clicks on images
import cv2

path = "Vid-Im/card.png"

def mouse_click(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)

img = cv2.imread(path)
cv2.imshow("Original Image", img)
cv2.setMouseCallback("Original Image", mouse_click)
cv2.waitKey(0)
