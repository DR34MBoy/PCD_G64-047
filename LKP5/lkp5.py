# Import library yang akan digunakan
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Memasukkan gambar ke program
# Membuat gambar baru dalam format HSV dan LAB
rgb_img = cv2.imread("melon.jpeg")
hsv_img = cv2.cvtColor(rgb_img, cv2.COLOR_BGR2HSV)
lab_img = cv2.cvtColor(rgb_img, cv2.COLOR_BGR2LAB)

# Memecah channel tiap format gambar
blue, green, red = cv2.split(rgb_img)
hue, sat, val = cv2.split(hsv_img)
L, A, B = cv2.split(lab_img)

# Visualisasi gambar dan jumlah pixel dalam bentuk plot
# RGB color space
fig, ax1 = plt.subplots(2, 3, figsize = (20,8), squeeze = False)
ax1[0,0].set_title('Red')
ax1[0,0].imshow(red, cmap='gray', vmin=0, vmax=255)
ax1[1,0].set_title('Histogram Red')
ax1[1,0].hist(red.ravel(), 256, [10,256])

ax1[0,1].set_title('Green')
ax1[0,1].imshow(green, cmap='gray', vmin=0, vmax=255)
ax1[1,1].set_title('Histogram Green')
ax1[1,1].hist(green.ravel(), 256, [10,256])

ax1[0,2].set_title('Blue')
ax1[0,2].imshow(blue, cmap='gray', vmin=0, vmax=255)
ax1[1,2].set_title('Histogram Blue')
ax1[1,2].hist(blue.ravel(), 256, [10,256])

# HSV color space
fig, ax2 = plt.subplots(2, 3, figsize = (20,8), squeeze = False)
ax2[0,0].set_title('Hue')
ax2[0,0].imshow(hue, cmap='gray', vmin=0, vmax=255)
ax2[1,0].set_title('Histogram Hue')
ax2[1,0].hist(hue.ravel(), 256, [10,256])

ax2[0,1].set_title('Saturation')
ax2[0,1].imshow(sat, cmap='gray', vmin=0, vmax=255)
ax2[1,1].set_title('Histogram Saturation')
ax2[1,1].hist(sat.ravel(), 256, [10,256])

ax2[0,2].set_title('Value')
ax2[0,2].imshow(val, cmap='gray', vmin=0, vmax=255)
ax2[1,2].set_title('Histogram Value')
ax2[1,2].hist(val.ravel(), 256, [10,256])

# LAB color space
fig, ax3 = plt.subplots(2, 3, figsize = (20,8), squeeze = False)
ax3[0,0].set_title('L')
ax3[0,0].imshow(L, cmap='gray', vmin=0, vmax=255)
ax3[1,0].set_title('Histogram L')
ax3[1,0].hist(L.ravel(), 256, [10,256])

ax3[0,1].set_title('A')
ax3[0,1].imshow(A, cmap='gray', vmin=0, vmax=255)
ax3[1,1].set_title('Histogram A')
ax3[1,1].hist(A.ravel(), 256, [10,256])

ax3[0,2].set_title('B')
ax3[0,2].imshow(B, cmap='gray', vmin=0, vmax=255)
ax3[1,2].set_title('Histogram B')
ax3[1,2].hist(B.ravel(), 256, [10,256])

plt.show() 

# Dari gambar visualisasi yang didapat, akan digunakan gambar dengan format
# HSV karena bagian yang ingin di mask terlihat lebih jelas untuk dibedakan
# dengan backgroundnya

# Menentukan nilai thresholding
lower_thresh = np.array([15, 125, 130])
upper_thresh = np.array([25,255,255])

# Membuat mask gambar
mask = cv2.inRange(hsv_img, lower_thresh, upper_thresh)

# Menerapkan / Segmentasi mask ke gambar yang akan di masking
mask_img1 = cv2.bitwise_and(rgb_img, rgb_img, mask = mask)

# Menampilkan gambar mask dan gambar yang telah di masking
cv2.imshow("mask1", mask)
cv2.imshow("mask_img1", mask_img1)

# Melakukan operasi noise removal dengan fungsi medianBlur
mask = cv2.medianBlur(mask, 121)

# Menerapkan / Segmentasi mask yang baru ke gambar yang akan di masking
mask_img2 = cv2.bitwise_and(rgb_img, rgb_img, mask = mask)

# Menampilkan gambar mask dan gambar yang telah di masking dan dilakukan noise removal
cv2.imshow("mask2", mask)
cv2.imshow("mask_img2", mask_img2)

# Menunggu suatu key untuk ditekan
cv2.waitKey(0)