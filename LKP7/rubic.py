import numpy as np
import cv2
import math

# Membaca gambar rubik
rubic_img = cv2.imread("cubes.jpeg")

# Membuat salinan gambar rubik
output_img = rubic_img.copy()

# Merubah format gambar rubik menjadi grayscale
gray_rubic = cv2.cvtColor(rubic_img, cv2.COLOR_BGR2GRAY)

# Mencari edge dengan fungsi Canny
edges = cv2.Canny(gray_rubic, 200, 220)

# Mendapatkan garis menggunakan fungsi HoughLines
lines = cv2.HoughLines(edges, rho=1, theta=np.pi/180, threshold=85, srn=100, stn=100, min_theta=0, max_theta=np.pi)

# Mendapatkan banyak garis
print(len(lines))

# Menggambar garis pada output_image
for i in range(0, len(lines)):
    rho = lines[i][0][0]
    theta = lines[i][0][1]
    a = math.cos(theta)
    b = math.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    cv2.line(output_img,(x1,y1),(x2,y2),(0,200,255))

# Menampilkan gambar dengan garis
cv2.imshow("output", output_img)

# Menunggu suatu key untuk ditekan agar dapat menutup gambar keluaran
cv2.waitKey(0)