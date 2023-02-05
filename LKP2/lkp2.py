import numpy as np
import cv2

def RGB_to_HSV(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = df/mx
    v = mx
    return h, s, v

def convert_image(image_path):
    image = cv2.imread(image_path)
    row, col, ch = image.shape
    for x in range(col):
        for y in range(row):
            b, g, r = image[y, x]
            h, s, v = RGB_to_HSV(r, g, b)
            image[y, x] = (int(h/2), int(s*255), int(v*255))
    return image


test = convert_image("lenna.png")
cv2.imshow(test)
cv2.waitKey(0)
