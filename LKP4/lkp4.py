import cv2
import numpy as np

# Fungsi Utama #

def convert_gray(image):
    # Mendapatkan baris, kolom, dan channel gambar masukan
    row, col, ch = image.shape

    # Membuat variabel / array dengan nama "gray"
    gray = np.zeros((row, col, 1), np.uint8)

    # Perhitungan grayscale
    for i in range(0, row):
        for j in range(0, col):
            gray[i, j] = 0.2989 * image[i, j][2] + 0.5870 * image[i, j][1] + 0.1140 * image[i, j][0]

    # Mengembalikan hasil konversi grayscale
    return gray

def proc_kern(image, kernel):
    hasil_proc = cv2.filter2D(image,-1,kernel)
    return hasil_proc


# Main Driver #
# Baca gambar
img = cv2.imread("lenna.png")

# Konversi grayscale
gray_img = convert_gray(img)

# Buat kernel
kernel_lp = np.array([[1/9, 1/9, 1/9],
                      [1/9, 1/9, 1/9],
                      [1/9, 1/9, 1/9]])

kernel_hp = np.array([[-1, -1, -1],
                      [-1, 8, -1],
                      [-1, -1, -1]])

kernel_bd = np.array([[-1, 0, 1],
                      [-1, 0, 1],
                      [-1, 0, 1]])


