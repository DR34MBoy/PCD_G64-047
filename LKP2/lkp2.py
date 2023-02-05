import numpy as np
import cv2

def RGB2HSV(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0

    cmx = max(r, g, b)
    cmn = min(r, g, b)
    diff = cmx-cmn

    if cmx == cmn:
        h = 0
    elif cmx == r:
        h = (60 * ((g-b)/diff) + 360) % 360
    elif cmx == g:
        h = (60 * ((b-r)/diff) + 120) % 360
    elif cmx == b:
        h = (60 * ((r-g)/diff) + 240) % 360

    if cmx == 0:
        s = 0
    else:
        s = diff/cmx
        
    v = cmx
    return h, s, v

def convert_image(image_path):
    image = cv2.imread(image_path)
    row, col, ch = image.shape
    for x in range(col):
        for y in range(row):
            b, g, r = image[y, x]
            h, s, v = RGB2HSV(r, g, b)
            image[y, x] = (int(h/2), int(s*255), int(v*255))
    return image

def avg_int(image):
    total = 0
    counter = 0
    row, col = image.shape
    for x in range(col):
        for y in range(row):
            total += image[x,y]
            counter += 1
    avg = total/counter
    return avg

def change_px(image):
    avg = avg_int(image)
    row, col = image.shape
    for x in range(col):
        for y in range(row):
            if image[x,y] < avg:
                image[x,y] = 0
            else:
                image[x,y] = 255
    return image

img = convert_image("lenna.png")
cv2.imshow("test1", img)

h,s,v = cv2.split(img)

print(avg_int(h))
print(avg_int(s))
print(avg_int(v))

test_h = change_px(h)
test_s = change_px(s)
test_v = change_px(v)

cv2.imshow("h", test_h)
cv2.imshow("s", test_s)
cv2.imshow("v", test_v)

cv2.waitKey(0)
