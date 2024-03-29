# Import library yang akan digunakan
import numpy as np
import cv2

# Fungsi Konvolusi
def customConvolution(img, mask):
    # Mendapatkan baris, kolom, dan channel gambar masukan
    row, col, ch= img.shape

    # Mendapatkan baris dan kolom dari mask / filter
    rowMask, colMask = len(mask), len(mask)

    # Mendapatkan matriks gambar bernama canvas
    canvas = np.zeros((row, col, 1), dtype="uint8")

    # Proses konvolusi
    for i in range(0,row-1):
        for j in range(0,col-1):
            imgSum = 0; maskSum = 0
            for a in range(-int(rowMask/2) , rowMask - int(rowMask/2)):
                for b in range(-int(colMask/2), colMask - int(colMask/2)):
                    if (i + a >= 0) and (j + b >= 0):
                        imgSum = imgSum + img[i+a, j+b][0] * mask[a + int(rowMask/2)][b + int(colMask/2)]
                        maskSum = maskSum + mask[a + int(rowMask/2)][b + int(colMask/2)]
            intensity = imgSum / maskSum
            if intensity > 255:
                intensity = 255
            elif intensity < 0:
                intensity = 0
            canvas[i, j] = intensity

    # Mengembalikan matriks gambar "canvas"
    return canvas

# Fungsi mengubah gambar menjadi grayscale
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

# Main Driver #
# Membaca gambar
img = cv2.imread("lenna.png")

# Membuat filter mask kernel
lowPassFilter = np.array([[1/9, 1/9, 1/9],
                          [1/9, 1/9, 1/9],
                          [1/9, 1/9, 1/9]])
highPassFilter = np.array([[0, -1, 0],
                           [-1, 4, -1],
                           [0, -1, 0]])
directPassFilter = np.array([[-1, 0, 1],
                             [-1, 0, 1],
                             [-1, 0, 1]])

# Mengubah gambar menjadi grayscale
canvas = convert_gray(img)

# Mendapatkan gambar dengan metode konvolusi
result_lpf = customConvolution(canvas, lowPassFilter)
result_hpf = customConvolution(canvas, highPassFilter)
result_dpf = customConvolution(canvas, directPassFilter)

# Menampilkan gambar hasil proses konvolusi
cv2.imshow("Low pass filter image", result_lpf)
cv2.imshow("High pass filter image", result_hpf)
cv2.imshow("Direct pass filter image", result_dpf)

cv2.waitKey(0)
cv2.destroyAllWindows()