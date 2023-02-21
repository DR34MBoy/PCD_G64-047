import cv2
import numpy as np
import matplotlib.pyplot as plt

# Latihan 1: Konversi Warna
img = cv2.imread("dori.jpg")
img_gray = cv2.imread("dori.jpg", 0)

hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hue, sat, val = cv2.split(hsv_img)
cv2.imshow("HSV Image", hsv_img)
cv2.imshow("Hue Image", hue)
cv2.imshow("Saturation Image", sat)
cv2.imshow("Value Image", val) 

# Latihan 2: Segementasi
img2 = cv2.imread("nemo.jpg")





cv2.waitKey(0)

