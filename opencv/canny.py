import cv2 as cv
import numpy as np


def edge_demo(image):#canny边缘提取#对噪声比较敏感
    blurred = cv.GaussianBlur(image,(3,3),0)
    #所以先高斯滤波处理噪声
    gray = cv.cvtColor(blurred,cv.COLOR_BGR2GRAY)
    x_grad = cv.Sobel(gray,cv.CV_16SC1,1,0)
    y_grad = cv.Sobel(gray,cv.CV_16SC1,0,1)
    #edge_output = cv.Canny(x_grad,y_grad,50,150)
    #高阈值一般为低阈值的三倍#梯度
    edge_output = cv.Canny(gray, 50, 150)
    #灰度
    cv.imshow('canny edge',edge_output)
    dst = cv.bitwise_and(image,image,mask=edge_output)
    cv.imshow('color edge',dst)



print('hi,python!')
src = cv.imread(r"F:\picture\1.jpg")
cv.namedWindow('input image',cv.WINDOW_AUTOSIZE)
cv.imshow('input image',src)
edge_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()