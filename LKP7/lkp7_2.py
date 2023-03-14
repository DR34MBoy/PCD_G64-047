import numpy as np
import cv2
import math

rubic_img = cv2.imread("cubes.jpeg")
# cv2.imshow("cubes", rubic_img)

output_img = rubic_img.copy()
# cv2.imshow("output", output_img)

gray_rubic = cv2.cvtColor(rubic_img, cv2.COLOR_BGR2GRAY)
# cv2.imshow("gray", gray_cubes)

# canny_rubic = Canny(rubic_img, 5, 50, 150)
# cv2.imshow("canny", canny_cubes)

edges = cv2.Canny(gray_rubic, 200, 220)
# cv2.imshow("canny", edges)

lines = cv2.HoughLines(edges, rho=10, theta=np.pi/90, threshold=75, srn=0, stn=0,
                       min_theta=0, max_theta=np.pi)

print(len(lines))

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

cv2.imshow("output", output_img)


cv2.waitKey(0)