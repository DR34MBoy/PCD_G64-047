import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("melon.jpeg")
array_img = img.flatten()
plt.hist(array_img, bins = 256)
plt.title("Original")
plt.show()

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
array_gray = img.flatten()
plt.hist(array_gray, bins = 256)
plt.title("Grayscale")
plt.show()

# Low Pass Kernel (Filter 2D)
kernel1 = np.array([[1/9, 1/9, 1/9],
                  [1/9, 1/9, 1/9],
                  [1/9, 1/9, 1/9]])
lpk = cv2.filter2D(img_gray,-1,kernel1)
array_lpk = lpk.flatten()

# cv2.imshow("LPK", lpk)

plt.hist(array_lpk, bins = 256)
plt.title("Low Pass Kernel")
plt.show()

# High Pass Kernel
kernel2 = np.array([[0, -1, 0],
                  [-1, 4, -1],
                  [0, -1, 0]])
hpk = cv2.filter2D(img_gray,-1,kernel2)
array_hpk = hpk.flatten()

# cv2.imshow("HPK", hpk)

plt.hist(array_hpk, bins = 256)
plt.title("High Pass Kernel")
plt.show()

# Directional Kernel
kernel3 = np.array([[-1, 0, 1],
                  [-1, 0, 1],
                  [-1, 0, 1]])
bdk = cv2.filter2D(img_gray,-1,kernel3)
array_bdk = bdk.flatten()

# cv2.imshow("BDK", bdk)

plt.hist(array_bdk, bins = 256)
plt.title("Directional Kernel")
plt.show()

cv2.waitKey(0)