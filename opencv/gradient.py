import cv2 as cv
import numpy as np
#sobel梯度算子
#梯度Gradient
def sobel_demo(image):
    grad_x = cv.Sobel(image,cv.CV_32F,1,0)
    #可用Scharr增强边缘
    grad_y = cv.Sobel(image,cv.CV_32F,0,1)
    x_grad = cv.convertScaleAbs(grad_x)
    #每个像素的梯度求绝对值转换为s是三通道8位图像
    y_grad = cv.convertScaleAbs(grad_y)
    cv.imshow('gradient-x',x_grad)
    cv.imshow('gradient-y', y_grad)
    gradxy = cv.addWeighted(x_grad,0.5,y_grad,0.5,0)
    cv.imshow('gradiantxy',gradxy)


def laplacian_demo(image):  #laplacian算法
    dst = cv.Laplacian(image,cv.CV_32F)
    lpls = cv.convertScaleAbs(dst)
    cv.imshow('laplacian_demo',lpls)

def laplacian_demo1(image):  #用算子矩阵直接输入
    kernel = np.array([[0,1,0],[1,-4,1],[0,1,0]])
    dst = cv.filter2D(image,cv.CV_32F,kernel=kernel)
    lpls = cv.convertScaleAbs(dst)
    cv.imshow('laplacian_demo1',lpls)

print('hi,python!')
src = cv.imread(r"F:\picture\7.jpg")
cv.namedWindow('input image',cv.WINDOW_AUTOSIZE)
cv.imshow('input image',src)
#sobel_demo(src)
laplacian_demo(src)
laplacian_demo1(src)
cv.waitKey(0)
cv.destroyAllWindows()