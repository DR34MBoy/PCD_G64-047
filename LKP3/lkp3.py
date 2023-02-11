import numpy as np
import cv2
import matplotlib.pyplot as plt
import PyQt5
from numpy import *

def convert_gray(image):
    row, col, ch = image.shape
    gray = np.zeros((row, col, 1), np.uint8)

    for i in range(0, row):
        for j in range(0, col):
            gray[i, j] = 0.2989 * image[i, j][2] + 0.5870 * image[i, j][1] + 0.1140 * image[i, j][0]

    return gray

def contrastStretch(image):
    row, col, ch = image.shape
    ctrStretch = np.zeros((row, col, ch), np.uint8)
    # fungsi max min harus 1 dimensi, pake .ravel()
    px_max = max(image.ravel())
    px_min = min(image.ravel())
    diff = px_max - px_min

    for i in range(row):
        for j in range(col):
            ctrStretch[i, j] = ((image[i, j] - px_min)/diff)*255

    return ctrStretch

def histogram(image):
    img = np.asarray(image)
    flat = img.flatten()
    plt.hist(flat, bins = 255)
    plt.show()

## Masih Belum Bener
def norm_hist(image):
    img = np.asarray(image)
    flat = img.flatten()
    plt.hist(flat, bins=255, density=True, color='blue', alpha=0.7, rwidth=0.85)
    plt.show()

def cmltv_histogram(image):
    img = np.asarray(image)
    flat = img.flatten()
    plt.hist(flat, bins = 255, cumulative = True)
    plt.show()

# Jangan pakai fungsi ini
def equ(image):
    # masih pake fungsi dl
    img_equ = cv2.equalizeHist(image)
    return img_equ







# Main Driver

melon = cv2.imread("melon.jpeg")

gray_melon = convert_gray(melon)

stretch = contrastStretch(gray_melon)

equ_stretch = equ(stretch)



# cv2.imshow("melon", melon)
# cv2.imshow("gray", gray_melon) 
# cv2.imshow("stretch", stretch) 

histogram(gray_melon) 
norm_hist(stretch) 


# norm_hist(gray_melon)


cv2.waitKey(0)