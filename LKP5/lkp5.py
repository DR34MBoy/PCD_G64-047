import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("melon.jpeg")
# cv2.imshow("melon", img)

hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lab_img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
# cv2.imshow("hsv", hsv_img)
# cv2.imshow("lab", lab_img)

blue, green, red = cv2.split(img)
hue, sat, val = cv2.split(hsv_img)
L, A, B = cv2.split(lab_img)

# RGB color space
cv2.imshow("Red", red)
cv2.imshow("Green", green)
cv2.imshow("Blue", blue)

# HSV color space
cv2.imshow("Hue", hue)
cv2.imshow("Saturation", sat)
cv2.imshow("Value", val)

# LAB color space
cv2.imshow("L", L)
cv2.imshow("A", A)
cv2.imshow("B", B)

# Red, Blue, Value yang kemungkinan dipilih

cv2.waitKey(0)