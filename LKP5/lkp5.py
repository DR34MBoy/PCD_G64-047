import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("melon.jpeg")

hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lab_img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

blue, green, red = cv2.split(img)
hue, sat, val = cv2.split(hsv_img)
L, A, B = cv2.split(lab_img)

# RGB color space
# fig, ax1 = plt.subplots(2, 3, figsize = (20,8), squeeze = False)
# ax1[0,0].set_title('Red')
# ax1[0,0].imshow(red, cmap='gray', vmin=0, vmax=255)
# ax1[1,0].set_title('Histogram Red')
# ax1[1,0].hist(red.ravel(), 256, [10,256])

# ax1[0,1].set_title('Green')
# ax1[0,1].imshow(green, cmap='gray', vmin=0, vmax=255)
# ax1[1,1].set_title('Histogram Green')
# ax1[1,1].hist(green.ravel(), 256, [10,256])

# ax1[0,2].set_title('Blue')
# ax1[0,2].imshow(blue, cmap='gray', vmin=0, vmax=255)
# ax1[1,2].set_title('Histogram Blue')
# ax1[1,2].hist(blue.ravel(), 256, [10,256])

# HSV color space
# fig, ax2 = plt.subplots(2, 3, figsize = (20,8), squeeze = False)
# ax2[0,0].set_title('Hue')
# ax2[0,0].imshow(hue, cmap='gray', vmin=0, vmax=255)
# ax2[1,0].set_title('Histogram Hue')
# ax2[1,0].hist(hue.ravel(), 256, [10,256])

# ax2[0,1].set_title('Saturation')
# ax2[0,1].imshow(sat, cmap='gray', vmin=0, vmax=255)
# ax2[1,1].set_title('Histogram Saturation')
# ax2[1,1].hist(sat.ravel(), 256, [10,256])

# ax2[0,2].set_title('Value')
# ax2[0,2].imshow(val, cmap='gray', vmin=0, vmax=255)
# ax2[1,2].set_title('Histogram Value')
# ax2[1,2].hist(val.ravel(), 256, [10,256])

# # # LAB color space
# fig, ax3 = plt.subplots(2, 3, figsize = (20,8), squeeze = False)
# ax3[0,0].set_title('L')
# ax3[0,0].imshow(L, cmap='gray', vmin=0, vmax=255)
# ax3[1,0].set_title('Histogram L')
# ax3[1,0].hist(L.ravel(), 256, [10,256])

# ax3[0,1].set_title('A')
# ax3[0,1].imshow(A, cmap='gray', vmin=0, vmax=255)
# ax3[1,1].set_title('Histogram A')
# ax3[1,1].hist(A.ravel(), 256, [10,256])

# ax3[0,2].set_title('B')
# ax3[0,2].imshow(B, cmap='gray', vmin=0, vmax=255)
# ax3[1,2].set_title('Histogram B')
# ax3[1,2].hist(B.ravel(), 256, [10,256])

# plt.show() 






# Red, Blue, Value yang kemungkinan dipilih

img_use = img

row, col = img_use.shape[0], img_use.shape[1]
mask = np.zeros((row, col, 1), np.uint8)
for i in range (row):
    for j in range (col):
        if red[i,j] > 240:
            mask[i,j] = 0
        else:
            mask[i,j] = 255

cv2.imshow("mask", mask)

output = img_use.copy()

for i in range(row):
  for j in range(col):
    if mask[i, j] == 255:
      output[i, j] = img_use[i, j]
    else:
      output[i, j] = 0

cv2.imshow("output", output)

cv2.waitKey(0)