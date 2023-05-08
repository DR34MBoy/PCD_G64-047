import pywt
import numpy as np
import matplotlib.pyplot as plt
import cv2

## Aktifkan salah satu

# img = cv2.imread('culvularia-patogen.png', cv2.IMREAD_GRAYSCALE)
## atau
img = cv2.imread('fusarium-patogen.png', cv2.IMREAD_GRAYSCALE)

img_data = (img.astype(float)).ravel()
normalized_data = (img_data-np.min(img_data))/(np.max(img_data)-np.min(img_data))

chirp_signal = np.sin(np.pi * normalized_data**2)

fig, ax = plt.subplots(figsize=(6,1))
ax.set_title("Original Chirp Signal: ")
ax.plot(chirp_signal)
plt.show()

data = chirp_signal
waveletname = 'sym5'

fig, axarr = plt.subplots(nrows=5, ncols=2, figsize=(6,6))
for ii in range(5):
    (data, coeff_d) = pywt.dwt(data, waveletname)
    axarr[ii, 0].plot(data, 'r')
    axarr[ii, 1].plot(coeff_d, 'g')
    axarr[ii, 0].set_ylabel("Level {}".format(ii + 1), fontsize=14, rotation=90)
    axarr[ii, 0].set_yticklabels([])
    if ii == 0:
        axarr[ii, 0].set_title("Approximation coefficients", fontsize=14)
        axarr[ii, 1].set_title("Detail coefficients", fontsize=14)
    axarr[ii, 1].set_yticklabels([])
plt.tight_layout()
plt.show()