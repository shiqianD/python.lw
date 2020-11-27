import cv2 as cv
import numpy as np
# contours外形轮廓
def contours_demo(image):
    dst = cv.GaussianBlur(image,(3,3),0)
    gray = cv.cvtColor(dst,cv.COLOR_BGR2GRAY)
    ret,binary = cv.threshold(gray,0,255,cv.THRESH_BINARY|cv.THRESH_OTSU)
    cv.imshow('binary image',binary)
    contours,hierarchy = cv.findContours(binary,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
    shape = image.shape
    new = np.ones(shape,np.uint8)
    cv.drawContours(new,contours,-1,(255,0,0),1)
    cv.imshow('detect contours',new)

print('hi,python!')
src = cv.imread(r"F:\picture\8.jpg")
cv.namedWindow('input image',cv.WINDOW_AUTOSIZE)
cv.imshow('input image',src)
contours_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()