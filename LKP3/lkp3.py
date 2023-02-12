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

    plt.hist(flat, bins = 256)
    plt.show()

def norm_hist(image):
    flat = image.flatten()

    histogram, _ = np.histogram(flat, bins=256, range=(0, 255), density=True)

    normalized_histogram = histogram / histogram.sum()

    plt.bar(np.arange(256), normalized_histogram)
    plt.xlim([0, 256])
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.show()

def cmltv_histogram(image):
    flat = image.flatten()
    
    histogram, _ = np.histogram(flat, bins=256, range=(0, 255), density=True)
    
    cumulative_histogram = np.zeros(256)
    cumulative_histogram[0] = histogram[0]

    for i in range(1, 256):
        cumulative_histogram[i] = cumulative_histogram[i-1] + histogram[i]
    
    plt.bar(np.arange(256), cumulative_histogram)
    plt.xlim([0, 256])
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.show()

# Masih salah
def equal_hist(image):
    flat_image = image.flatten()
    histogram, bins = np.histogram(flat_image, bins=256, range=(0, 255))

    cumulative_histogram = np.cumsum(histogram)
    cumulative_histogram = cumulative_histogram / cumulative_histogram[-1]
    
    equalized = np.interp(flat_image, bins[:-1], cumulative_histogram)
    eqlz = equalized.reshape(image.shape)

    plt.hist(eqlz.flatten(), bins=256, range=(0, 255))
    plt.xlim([0, 256])
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.show()

# Jangan pakai fungsi di bawah ini
def equ(image):
    # masih pake fungsi dl
    img_equ = cv2.equalizeHist(image)
    return img_equ

def cmltv_histogram2(image):
    img = np.asarray(image)
    flat = img.flatten()
    plt.hist(flat, bins = 256, cumulative = True)
    plt.show()







# Main Driver

melon = cv2.imread("melon.jpeg")

gray_melon = convert_gray(melon)

stretch = contrastStretch(gray_melon)

equ_stretch = equ(stretch)



# cv2.imshow("melon", melon)
# cv2.imshow("gray", gray_melon) 
# cv2.imshow("stretch", stretch) 

# histogram(gray_melon) 
# norm_hist(gray_melon) 
# cmltv_histogram2(stretch)
equal_hist(gray_melon)




cv2.waitKey(0)