import numpy as np
import cv2

def change_px (image):
    for i in range(0,row):
        for j in range(0,col):
            if image[i, j] < 150:
                image[i, j] = 255
            else:
                image[i, j] = image[i, j]
    return image

img_daun = cv2.imread("daun.jpg")
row, col ,ch = img_daun.shape

b, g, r = cv2.split(img_daun)

cv2.imshow("daun", img_daun)

# cv2.imshow("b", b)
# cv2.imshow("g", g)
# cv2.imshow("r", r)

change_b = change_px(b)
change_g = change_px(g)
change_r = change_px(r)

# cv2.imshow("b", change_b)
# cv2.imshow("g", change_g)
# cv2.imshow("r", change_r)

merge = cv2.merge([change_b, change_g, change_r])

cv2.imshow("merge", merge)


cv2.waitKey(0)

