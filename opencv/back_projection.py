import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def back_projection():  #图片反向投影
    sample = cv.imread(r'F:\picture\6.1.jpg')
    target = cv.imread(r'F:\picture\6.jpg')
    sam_hsv = cv.cvtColor(sample,cv.COLOR_BGR2HSV)#转到hsv色彩空间
    tar_hsv = cv.cvtColor(target,cv.COLOR_BGR2HSV)

    cv.imshow('sample',sample)
    cv.imshow('target',target)
    # sample直方图
    samHist = cv.calcHist([sam_hsv],[0,1],None,[180,256],[0,180,0,256])
    #[180,256]bin的个数越大分的越细
    cv.normalize(samHist,samHist,0,255,cv.NORM_MINMAX)
    dst = cv.calcBackProject([tar_hsv],[0,1],samHist,[0,180,0,256],1)#1放大系数
    cv.imshow('backProjectionDemo',dst)
    x = cv.bitwise_not(dst)
    cv.imshow('pixel_demo', x)

def hist2d_demo(image):  #2D直方图#色调，饱和度
    hsv = cv.cvtColor(image,cv.COLOR_BGR2HSV)
    hist = cv.calcHist([image],[0,1],None,[180,256],[0,180,0,256])
    plt.imshow(hist,interpolation='nearest')  #临近点插值
    plt.title('2D Histogram')
    plt.show()


print('hi,python!')
src = cv.imread(r"F:\picture\ta.jpg")
cv.namedWindow('input image',cv.WINDOW_AUTOSIZE)
cv.imshow('input image',src)
#hist2d_demo(src)
back_projection()
cv.waitKey(0)
cv.destroyAllWindows()