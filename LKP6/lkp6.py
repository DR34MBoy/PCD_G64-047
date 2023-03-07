# Import library yang akan digunakan
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Memasukkan gambar ke program
# Membuat gambar baru dalam format HSV dan LAB
rgb_img = cv2.imread("tomato.jpeg")
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

# plt.show() 

# Dari gambar visualisasi yang didapat, akan digunakan gambar dengan format
# LAB (Lebih spesifik yaitu bagian A* nya saja) karena bagian yang ingin di 
# mask terlihat lebih jelas untuk dibedakan dengan backgroundnya

# Menentukan nilai thresholding
lower_thresh = np.array([135])
upper_thresh = np.array([202])

# Membuat mask gambar
mask = cv2.inRange(A, lower_thresh, upper_thresh)

# Menerapkan / Segmentasi mask ke gambar yang akan di masking
mask_img1 = cv2.bitwise_and(rgb_img, rgb_img, mask = mask)

# # Menampilkan gambar mask dan gambar yang telah di masking
cv2.imshow("mask1", mask)
cv2.imshow("mask_img1", mask_img1)

# Melakukan operasi noise removal dengan fungsi medianBlur
mask = cv2.medianBlur(mask, 5)

# Menerapkan / Segmentasi mask yang baru ke gambar yang akan di masking
mask_img2 = cv2.bitwise_and(rgb_img, rgb_img, mask = mask)

# # Menampilkan gambar mask dan gambar yang telah di masking dan dilakukan noise removal
cv2.imshow("mask2", mask)
cv2.imshow("mask_img2", mask_img2)

# Fungsi closing + subplot
def closing(image, i): 
    fig, ax = plt.subplots(1, 4, figsize = (20,8), squeeze = False)
    x = 0
    kernel_dilasi = np.ones((i, i), np.uint8)
    for j in range (3, 11, 2):
        kernel_erosi = np.ones((j, j), np.uint8)
        dilasi = cv2.dilate(image, kernel_dilasi, iterations=1)
        erosi = cv2.erode(dilasi, kernel_erosi, iterations=1)
        ax[0, x].imshow(erosi)
        ax[0, x].set_title(str(j) + "x" + str(j))
        x = x + 1
    plt.show()

# Mencari hasil gambar dengan kernel dilasi dan erosi yang berbeda 
closing(mask_img2, 3)        
closing(mask_img2, 5)   
closing(mask_img2, 7)   
closing(mask_img2, 9) 

# Dari hasil yang didapat, menurut saya hasil yang paling bagus adalah gambar dengan kernel erosi 3x3 dan kernel dilasi 5x5
kernel_dilasi = np.ones((3, 3), np.uint8)
kernel_erosi = np.ones((5, 5), np.uint8)
dilasi = cv2.dilate(mask_img2, kernel_dilasi, iterations=1)
erosi = cv2.erode(dilasi, kernel_erosi, iterations=1)
cv2.imshow("hasil akhir", erosi)

# # Menunggu suatu key untuk ditekan
cv2.waitKey(0)