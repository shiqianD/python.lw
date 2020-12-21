import cv2 as cv
import numpy as np


def clamp(pv):
    if pv>255:
        return 255
    if pv<0:
        return 0
    else:
        return pv

def gaussian_noise(image):#高斯噪声
    h,w,c = image.shape
    for row in range(h):
        for col in range(w):
            s = np.random.normal(0,26,3)  #概率分步的均值，标准差，矩阵维
            b = image[row,col,0]  #blue
            g = image[row,col,1]  #green
            r = image[row,col,2]  #red
            image[row, col, 0] = clamp(b + s[0])
            image[row, col, 1] = clamp(g + s[1])
            image[row, col, 2] = clamp(r + s[2])
    cv.imshow('noise image',image)


print('hi,python!')
src = cv.imread(r"F:\picture\she.jpg")
cv.namedWindow('input image',cv.WINDOW_AUTOSIZE)
cv.imshow('input image',src)
t1 = cv.getTickCount()
gaussian_noise(src)
t2 = cv.getTickCount()
time = (t2-t1)/cv.getTickFrequency()
print('time consume : %s ms'% (time*1000))
dst = cv.GaussianBlur(src,(5,5),0)
cv.imshow('gaussian blur',dst)#高斯模糊对高斯噪声有抑制作用
cv.waitKey(0)
cv.destroyAllWindows()