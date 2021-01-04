import cv2 as cv
import numpy as np
# 去除小的干扰快
#填充闭合区域，水平或垂直线提取

def open_demo(image):#先膨胀在腐蚀
    print(image.shape)
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    ret,binary =cv.threshold(gray,0,255,cv.THRESH_BINARY_INV |cv.THRESH_OTSU)
    cv.imshow('binary',binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT,())#要保留的形状
    binary = cv.morphologyEx(binary,cv.MORPH_OPEN,kernel)


print('hi,python!')
src = cv.imread(r"F:\picture\12.jpg")
cv.namedWindow('input image',cv.WINDOW_AUTOSIZE)
cv.imshow('input image',src)
open_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()