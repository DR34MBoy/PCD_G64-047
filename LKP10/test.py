import numpy as np
import cv2

# x = np.linspace(2.0, 3.0, num=5)

img = cv2.imread('culvularia-patogen.png', cv2.IMREAD_GRAYSCALE)
x = (img.astype(float)).ravel()
# x = img.astype(float)

normalizedData = (x-np.min(x))/(np.max(x)-np.min(x))

normalizedData = normalizedData[:1000]




print(x)
print(normalizedData)
print(len(normalizedData))



