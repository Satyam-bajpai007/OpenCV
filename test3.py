# How to crop and resize the images

import cv2

path = "Vid-Im/car.png"
img = cv2.imread(path)
print(img.shape)

width, height = 400, 400
img_resize = cv2.resize(img, (width, height))
print(img.shape)

img_cropped = img[300:878, 800:1920]
img_crop_resize = cv2.resize(img_cropped, (img.shape[1], img.shape[0]))

cv2.imshow("Yellow Car", img)
# cv2.imshow("Resize Yellow Car", img_resize)
# cv2.imshow("Cropped Yellow Car", img_cropped)
cv2.imshow("Cropped Resize Yellow Car", img_crop_resize)
cv2.waitKey(0)
