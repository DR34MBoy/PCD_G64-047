import numpy as np
import cv2

def Canny(image, k, t1,t2):
    img = cv2.GaussianBlur(image, (k, k), 0)
    canny = cv2.Canny(img, t1, t2)
    return canny

citrus_img = cv2.imread("citrus_1.jpeg")
# cv2.imshow("citrus", citrus_img)

output_img = citrus_img.copy()
cv2.imshow("citrus", output_img)

gray_citrus = cv2.cvtColor(citrus_img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray_citrus)

canny_citrus = Canny(citrus_img, 5, 50, 150)
# cv2.imshow("canny", canny_citrus)

edges = cv2.Canny(gray_citrus, 200, 220)


cv2.waitKey(0)