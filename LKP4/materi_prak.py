import cv2 
import numpy as np

img = cv2.imread("lenna.png")
cv2.imshow("original", img)

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("original", img_gray)

# Spasial Filter (Smoothing type CV_MEDIAN)
median = cv2.medianBlur(img_gray, 5)
cv2.imshow("median", median)

# Spasial Filter (Matriks Konvolusi)
kernel = np.array([[0, -1, 0],
 [-1, 4, -1],
 [0, -1, 0]])
dst = cv2.filter2D(img_gray,-1,kernel)
cv2.imshow("result", dst)

# Gaussian Noise
gauss = np.random.normal(0,1,img.size)
gauss = gauss.reshape(img.shape[0],img.shape[1],img.shape[2]).astype('uint8')
img_gauss = cv2.add(img, gauss)
cv2.imshow('Gaussian noise', img_gauss)









cv2.waitKey(0)