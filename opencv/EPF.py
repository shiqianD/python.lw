import cv2 as cv
import numpy as np

#EPF#高斯双边#均值偏移
def bi_demo(image):
    dst = cv.bilateralFilter(image,0,80,25)#100，15
    cv.imshow('bi_demo',dst)

def shift_demo(image):
    dst = cv.pyrMeanShiftFiltering(image,5,20)#10,50
    cv.imshow('shift_demo',dst)


print('hi,python!')
src = cv.imread(r"F:\picture\7.jpg")
cv.namedWindow('input image',cv.WINDOW_AUTOSIZE)
cv.imshow('input image',src)
bi_demo(src)
shift_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
