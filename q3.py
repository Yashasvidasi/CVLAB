import cv2
import numpy as np

image_path = "../IMAGES/WEEK1_IMAGES/leaf.png"

img = cv2.imread(image_path)
x, y = 100, 100
b, g, r = img[y, x]
print("RGB  ({}, {}): ({}, {}, {})".format(x, y, r, g, b))