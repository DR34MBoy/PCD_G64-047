import numpy as np
import cv2

def convert_gray(image):
    row, col, ch = image.shape
    gray = np.zeros((row, col, 1), np.uint8)

    for i in range(0, row):
        for j in range(0, col):
            gray[i, j] = 0.2989 * image[i, j][2] + 0.5870 * image[i, j][1] + 0.1140 * image[i, j][0]

    return gray


# Main Driver

melon = cv2.imread("melon.jpeg")
# cv2.imshow("melon", melon)

gray_melon = convert_gray(melon)
# cv2.imshow("gray", gray_melon) 

cv2.waitKey(0)