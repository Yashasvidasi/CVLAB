import cv2
import numpy as np
img = np.zeros((400, 400, 3), np.uint8)
x, y, w, h = 100, 100, 200, 150
color = (0, 255, 0)
thickness = 2
cv2.rectangle(img, (x, y), (x+w, y+h), color, thickness)
cv2.imshow('Rectangle', img)
cv2.waitKey(0)
cv2.destroyAllWindows()