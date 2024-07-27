import cv2 as cv

img = cv.imread(cv.samples.findFile("../IMAGES/WEEK1_IMAGES/leaf.png"))


cv.imshow("Display window", img)
k = cv.waitKey(0)

if k == ord("s"):
    cv.imwrite("../IMAGES/WEEK1_IMAGES/leaf_saved.png", img)