import cv2 as cv
import numpy as np
from plt import pyplot as plt


def equalHist_demo(image):  #全局的均衡化
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)  #j均衡化只支持灰度图
    dst = cv.equalizeHist(gray)
    cv.imshow('equalHist_demo',dst)


def Clahe_demo(image):  #局部均衡化
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)   # j均衡化只支持灰度图
    Clahe = cv.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
    dst = Clahe.apply(gray)
    cv.imshow('equalHist_demo', dst)

def create_rgb_hist(image):
    h,w,c = image.shape  #创建rgb三通道直方图(矩阵）
    rgbHist = np.zeros([16*16*16,1],np.float32)  #创建这样的初始矩阵，三通道，每个有16个bin
    bsize = 256/16  #直方图bin降级16
    for row in range(h):  #对每个像素进行处理
        for col in range(w):
            b=image[row,col,0]
            g =image[row,col,1]
            r=image[row,col,2]
            #人为构建索引，该索引通过每一个像素点的三通道进行构建
            index = np.int(b/bsize)*16*16+np.int(g/bsize)+16+np.int(r/bsize)#哪个颜色出现哪个就加一#直方图矩阵
            rgbHist[np.int(index),0] += 1
    return rgbHist

def hist_compare(image1,image2):#直方图比较
    hist1 = create_rgb_hist(image1)
    hist2 = create_rgb_hist(image2)
    match1 = cv.compareHist(hist1, hist2, cv.HISTCMP_BHATTACHARYYA)
    match2 = cv.compareHist(hist1, hist2, cv.HISTCMP_CORREL)
    match3 = cv.compareHist(hist1, hist2, cv.HISTCMP_CHISQR)
    print('巴氏距离：%s,相关性：%s,卡方：%s'%(match1,match2,match3 ))
  #巴氏越小越相似，相关越大越相似，卡方越小越相似


print('hi,python!')
src = cv.imread(r"F:\picture\she.jpg")
cv.namedWindow('input image',cv.WINDOW_AUTOSIZE)
#cv.imshow('input image',src)
equalHist_demo(src)
#Clahe_demo(src)

image1 = cv.imread(r"F:\picture\ta.jpg")
image2 = cv.imread(r"F:\picture\yuv.ta.jpg")
cv.imshow('image1',image1)
cv.imshow('image2',image2)
#hist_compare(image1,image2)

cv.waitKey(0)
cv.destroyAllWindows()
