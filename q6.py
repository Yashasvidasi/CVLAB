import cv2
image_path = "../IMAGES/WEEK1_IMAGES/leaf.png"
img = cv2.imread(image_path)
angle = 180
(h, w) = img.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, angle, 1.0)
rotated_img = cv2.warpAffine(img, M, (w, h))
cv2.imshow('Original Image', img)
cv2.imshow('Rotated Image', rotated_img)
k = cv2.waitKey(0)
cv2.destroyAllWindows()
