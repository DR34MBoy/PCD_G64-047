import numpy as np
import cv2
import matplotlib.pyplot as plt

# Fungsi utama konversi dan proses gambar
# Konversi gambar menjadi grayscale
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

# Melakukan contrast stretching
def contrastStretch(image):
    # Mendapatkan baris, kolom, dan channel gambar masukan
    row, col, ch = image.shape

    # Membuat variabel / array dengan nama "ctrStretch"
    ctrStretch = np.zeros((row, col, ch), np.uint8)
    
    # Mencari nilai maksimum, minimum, dan selisih antara dua nilai tersebut
    px_max = max(image.ravel())
    px_min = min(image.ravel())
    diff = px_max - px_min

    # Perhitungan contrast stretching
    for i in range(row):
        for j in range(col):
            ctrStretch[i, j] = ((image[i, j] - px_min)/diff) * 255

    # Mengembalikan hasil contrast stretching
    return ctrStretch




# Membuat Histogram
# Fungsi histogram normal
def histogram(image):
    img = np.asarray(image)
    flat = img.flatten()

    # Mengembalikan histogram
    return flat

# Fungsi normalisasi
def normalize(image):
    flat = image.flatten()

    histogram, _ = np.histogram(flat, bins=256, range=(0, 255), density=True)

    normalized_histogram = histogram / histogram.sum()

    # Mengembalikan hasil normalisasi
    return normalized_histogram

# Fungsi kumulatif
def cumulative(image):
    # Perhitungan untuk membuat histogram dengan format sedikit berbeda
    histogram = np.zeros(256, dtype=int)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            histogram[image[i, j]] += 1
    
    # Perhitungan untuk membuat hasil kumulatif
    cumul = np.zeros(256, dtype=int)
    cumul[0] = histogram[0]
    for i in range(1, 256):
        cumul[i] = cumul[i - 1] + histogram[i]
    
    # Mengembalikan hasil kumulatif
    return cumul

# Fungsi ekualisasi
def equalize(image):
    # Menerima fungsi kumulatif yang telah dibuat
    cumul = cumulative(image)
    
    # Melakukan normalisasi variabel "cumul" (dari fungsi kumulatif)
    cumul_min = np.min(cumul)
    cumul_max = np.max(cumul)
    cumul_normalized = (cumul - cumul_min) / (cumul_max - cumul_min) * 255
    
    equalized_image = np.zeros(image.shape, dtype=np.uint8)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            equalized_image[i, j] = cumul_normalized[image[i, j]].astype(np.uint8)

    # Mengembalikan hasil ekualisasi
    return equalized_image




# Menampilkan Histogram
def draw_hist(image, name):
    # Pilihan untuk membuat histogram
    if name == "Histogram" or name == "Equalize" :
        plt.hist(image.flatten(), bins=256, range=(0, 255))
        plt.xlim([0, 256])
        plt.xlabel("Intensitas Pixel")
        plt.ylabel("Frekuensi")
        if name == "Histogram" :
            plt.title("Histogram")
        else:
            plt.title("Histogram Ekualisasi")
        plt.show()
    elif name == "Normalize" or name == "Cumulative" :
        plt.bar(np.arange(256), image)
        plt.xlim([0, 256])
        plt.xlabel("Intensitas Pixel")
        plt.ylabel("Frekuensi")
        if name == "Normalize" :
            plt.title("Histogram Normalisasi")
        else:
            plt.title("Histogram Kumulatif")
        plt.show()




# Main Driver
# Membaca gambar melon dan melakukan proses grayscale, contrast stretching, dan ekualisasi
melon = cv2.imread("melon.jpeg")
gray_melon = convert_gray(melon)
stretch = contrastStretch(gray_melon)
equal = equalize(gray_melon)

# Menampilan gambar melon asli, grayscale, contrast stretching, dan ekualisasi
cv2.imshow("original", melon)
cv2.imshow("gray", gray_melon)
cv2.imshow("ekualisasi", equal) 
cv2.imshow("stretch", stretch) 

# Menapilkan histogram
# gray_melon = histogram, normalisasi, kumulatif, dan ekualisasi
# contrast stretching = histogram
draw_hist(histogram(gray_melon),"Histogram")
draw_hist(histogram(stretch),"Histogram")
draw_hist(normalize(gray_melon),"Normalize")
draw_hist(cumulative(gray_melon),"Cumulative")
draw_hist(equalize(gray_melon),"Equalize")

cv2.waitKey(0)