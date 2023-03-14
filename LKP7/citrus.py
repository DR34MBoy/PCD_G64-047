import numpy as np
import cv2

# Membaca gambar citrus
citrus_img = cv2.imread("citrus_1.jpeg")

# Membuat salinan gambar citrus
output_img = citrus_img.copy()

# Merubah format gambar rubik menjadi grayscale
gray_citrus = cv2.cvtColor(citrus_img, cv2.COLOR_BGR2GRAY)

# Menerapakan medianBlur ke gambar gray_citrus
gray_citrus = cv2.medianBlur(gray_citrus,11)

# Mendapatkan lingkaran menggunakan fungsi HoughCircles
circles = cv2.HoughCircles(gray_citrus, cv2.HOUGH_GRADIENT,dp=1,minDist=35,param1=40,param2=55,minRadius=39,maxRadius=220)
circles = np.uint16(np.around(circles))

# Menggambar lingkaran pada output_image
for i in circles[0,:]:
    cv2.circle(output_img,(i[0],i[1]),i[2],(0,255,0))
    cv2.circle(output_img,(i[0],i[1]),2,(0,0,255))
    # print("cx: {}, cy: {}, radius: {}".format(i[0],i[1], i[2]))

# Menampilkan gambar dengan lingkaran
cv2.imshow("output", output_img)

# Menunggu suatu key untuk ditekan agar dapat menutup gambar keluaran
cv2.waitKey(0)