import numpy as np
import cv2
import matplotlib.pyplot as plt
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




# Membuat Histogram
def histogram(image):
    img = np.asarray(image)
    flat = img.flatten()

    return flat

def norm_hist(image):
    flat = image.flatten()

    histogram, _ = np.histogram(flat, bins=256, range=(0, 255), density=True)

    normalized_histogram = histogram / histogram.sum()

    return normalized_histogram

def cmltv_hist(image):
    histogram = np.zeros(256, dtype=int)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            histogram[image[i, j]] += 1
    
    cdf = np.zeros(256, dtype=int)
    cdf[0] = histogram[0]
    for i in range(1, 256):
        cdf[i] = cdf[i - 1] + histogram[i]
    
    return cdf

def equal_hist(image):
    cdf = cmltv_hist(image)
    
    cdf_min = np.min(cdf)
    cdf_max = np.max(cdf)
    cdf_normalized = (cdf - cdf_min) / (cdf_max - cdf_min) * 255
    
    equalized_image = np.zeros(image.shape, dtype=np.uint8)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            equalized_image[i, j] = cdf_normalized[image[i, j]].astype(np.uint8)

    return equalized_image




# Menamplikan Histogram
def draw_hist(image, name):
    if name == "Histogram" or name == "Equalize" :
        plt.hist(image.flatten(), bins=256, range=(0, 255))
        plt.xlim([0, 256])
        plt.xlabel("Pixel Intensity")
        plt.ylabel("Frequency")
        plt.show()
    elif name == "Normalize" or name == "Cumulative" :
        plt.bar(np.arange(256), image)
        plt.xlim([0, 256])
        plt.xlabel("Pixel Intensity")
        plt.ylabel("Frequency")
        plt.show()




# Main Driver
melon = cv2.imread("melon.jpeg")
gray_melon = convert_gray(melon)
stretch = contrastStretch(gray_melon)
equal = equal_hist(gray_melon)

cv2.imshow("ori", melon)
cv2.imshow("gray", gray_melon)
cv2.imshow("ekualisasi", equal) 
cv2.imshow("stretch", stretch) 

draw_hist(histogram(gray_melon),"Histogram")
draw_hist(histogram(stretch),"Histogram")
draw_hist(norm_hist(gray_melon),"Normalize")
draw_hist(cmltv_hist(gray_melon),"Cumulative")
draw_hist(equal_hist(gray_melon),"Equalize")

cv2.waitKey(0)