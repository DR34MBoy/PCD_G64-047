import math
import cv2
import numpy as np

img = cv2.imread('cubes.jpeg')
output_img = img.copy()
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,200,220)
lines = cv2.HoughLines(edges, rho=0.5, theta=np.pi/90, threshold=75, srn=0, stn=0,
                       min_theta=0, max_theta=np.pi)


# oVERWRITING--> OUTPUT_img
for i in range(0, len(lines)):
  rho = lines[i][0][0]
  theta = lines[i][0][1]
  a = math.cos(theta) # sudut
  b = math.sin(theta) # sudut
  x0 = a*rho # Sumbu X
  y0 = b*rho # Sumbu Y
  # Note : angka 1000 = konstanta/pengalinya.
  x1 = int(x0 + 1000*(-b))
  y1 = int(y0 + 1000*(a))
  x2 = int(x0 - 1000*(-b))
  y2 = int(y0 - 1000*(a))
  cv2.line(output_img,(x1,y1),(x2,y2),(0,200,255))

print(lines[0])
print("\n Original Image")
cv2.imshow("image",img)
print("\n Hough Lines Transform Image")
cv2.imshow("output", output_img)

cv2.waitKey(0)