import cv2 as cv
import numpy as np


def blur_demo(image):#均值模糊#算数平均值#对随机噪声
    dst = cv.blur(image,(5,5))#行列上的模糊像素
    cv.imshow('blur_demo',dst)

def median_blur_demo(image):#中值模糊#排序中间值#椒盐噪声
    dst = cv.medianBlur(image,5)#必须是奇数
    cv.imshow('median_blur_demo',dst)

def custom_blur_demo(image):#自定义中值模糊
    #kernel = np.ones([5,5],np.float32)/25#二维
    #kernel = np.array([[1,1,1],[1,1,1],[1,1,1]],np.float32)/9
    kernel = np.array([[0, -1, 0], [-1, 5.2, -1], [0, -1, 0]], np.float32) #Laplace锐化算子
    dst = cv.filter2D(image,-1,kernel=kernel)
    cv.imshow('custom_blur_demo',dst)


print('hi,python!')
src = cv.imread(r"F:\picture\she.jpg")
cv.namedWindow('input image',cv.WINDOW_AUTOSIZE)
cv.imshow('input image',src)
blur_demo(src)
median_blur_demo(src)
custom_blur_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
