import numpy as np
import cv2

# Fungsi utama
# Fungsi untuk mendapatkan matrix dari suatu gambar masukan menggunakan fungsi np.array()
def matrix_img(image):
    matrix = np.array(image)
    return matrix

# Fungsi untuk mengubah intensitas pixel gambar dengan threshold tertentu
def change_px (image):
    row, col ,ch = img_daun.shape
    for i in range(0,row):
        for j in range(0,col):
            if image[i, j] < 150:
                image[i, j] = 255
    return image

# Fungsi untuk mendapatkan transpose dari matrix menggunakan fungsi transpose()
def transp_matrix(matrix):
    tp = matrix.transpose()
    return tp




# Main Driver
# Membaca gambar daun lalu menampilkannya
img_daun = cv2.imread("daun.jpg")
cv2.imshow("daun", img_daun)

# Menggunakan fungsi matrix_img untuk mendapatkan matrix dari gambar daun, lalu menampilkannya
matrix = matrix_img(img_daun)
print(matrix)

# Memecah tiap channel menggunakan fungsi split
b, g, r = cv2.split(img_daun)
# Lalu melakukan perubahan intensitas pixel dengan fungsi change_px sesuai dengan threshold
change_b = change_px(b)
change_g = change_px(g)
change_r = change_px(r)
# Menggabungkan kembali channel yang telah dipisah dan diubah
merge = cv2.merge([change_b, change_g, change_r])
# Menampilkan gambar setelah digabung
cv2.imshow("merge", merge)

# Menggunakan fungsi transp_matrix untuk mendapatkan transpose dari matrix, lalu menampilkannya
transpose = transp_matrix(matrix)
print(transpose)

cv2.waitKey(0)