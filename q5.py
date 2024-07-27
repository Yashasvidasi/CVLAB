import cv2
image_path = "../IMAGES/WEEK1_IMAGES/leaf.png"
img = cv2.imread(image_path)
width, height = 640, 480
resized_img = cv2.resize(img, (width, height))
cv2.imshow('Original Image', img)
cv2.imshow('Resized Image', resized_img)
k = cv2.waitKey(0)
if(k == ord("q")):
    cv2.destroyAllWindows()