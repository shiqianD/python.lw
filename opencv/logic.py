import cv2 as cv
import numpy as np
def add_demo(m1,m2):
    dst=cv.add(m1,m2)
    cv.imshow('add.demo',dst)


def subtract_demo(m1,m2):
    dst = cv.subtract(m1,m2)
    cv.imshow('subtract',dst)


def divide_demo(m1,m2):
    dst = cv.divide(m1,m2)
    cv.imshow('divide',dst)


def multiply_demo(m1,m2):
    dst = cv.multiply(m1,m2)
    cv.imshow('multiply',dst)


def logic_demo(m1,m2):#logic逻辑
    dst = cv.bitwise_and(m1,m2)#像素与运算
    cv.imshow('logic_demo', dst)


def logic_demo1(m1,m2):
    dst = cv.bitwise_or(m1,m2)#像素与运算
    cv.imshow('logic_demo1', dst)


# def others(m1,m2):#求均值
#     M1 = cv.mean(m1)
#     M2 = cv.mean(m2)
#     print(M1)
#     print(M2)

def others(m1,m2):#求均值和标准差，标准差大代表图像差异越大。#平均方差->样本的波动，小，图片暗
    M1,dev1 = cv.meanStdDev(m1)
    M2,dev2 = cv.meanStdDev(m2)
    h,w = m1.shape[:2]
    #print(M1)
    #print(M2)
    print(dev1)
    print(dev2)
    img = np.zeros([h,w],np.uint8)
    m,dev = cv.meanStdDev(img)
    print(m)
    print(dev)


def contrast_brightness_demo(image,c,b):#调整亮度比
    h,w,ch = image.shape
    black = np.zeros([h,w,ch],image.dtype)
    dst = cv.addWeighted(image,c,black,1-c,b)
    cv.imshow('con-bri-demo',dst)

print('hi,python!')
src1 = cv.imread(r"F:\picture\windows.jpg")
src2 = cv.imread(r'F:\picture\linux.jpg')
src = cv.imread(r"F:\picture\2.jpg")
cv.namedWindow('src1',cv.WINDOW_GUI_NORMAL)
cv.imshow('src1',src1)
cv.imshow('src2',src2)
cv.imshow('src',src)
#add_demo(src1,src2)
#subtract_demo(src1,src2)
#divide_demo(src1,src2)
#logic_demo(src1,src2)
#logic_demo1(src1,src2)
#others(src1,src2)
contrast_brightness_demo(src,1.2,30)
cv.waitKey(0)
cv.destroyAllWindows()
