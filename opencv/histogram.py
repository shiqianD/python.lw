import cv2 as cv
import numpy as np
from plt import pyplot as plt


def plot_demo(image):#统计直方图
    plt.hist(image.ravel(),256,[0,256])
    plt.show()
def image_hist(image):#三通道直方图
    color = ('blue','green','red')
    for i,color in enumerate(color):
        hist = cv.calcHist([image],[i],None,[256],[0,256])
        plt.plot(hist,color=color)
        plt.xlim([0,256])
    plt.show()#x轴大的代表白色


print('hi,python!')
src = cv.imread(r"./rice.png")
cv.namedWindow('input image',cv.WINDOW_AUTOSIZE)
# cv.imshow('input image',src)
plot_demo(src)
# image_hist(src)
cv.waitKey(0)
cv.destroyAllWindows()