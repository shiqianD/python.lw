import cv2 as cv
from plt import pyplot as plt


def adjust(src):
    gray = cv.cvtColor(src,cv.COLOR_BGR2GRAY)
    cv.imshow("gray",gray)
    a = cv.imadjust

print('hi,python!')
src = cv.imread(r"F:\picture\ta.jpg")
cv.namedWindow('input image',cv.WINDOW_AUTOSIZE)
cv.imshow('input image',src)
adjust(src)
cv.waitKey(0)
cv.destroyAllWindows()




