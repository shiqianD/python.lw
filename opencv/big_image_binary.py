import cv2 as cv
import numpy as np
#大图像二值化
#感兴趣区域编码roi
#threch门槛
def big_image_binary(image):  #分块二值化
    print(image.shape)
    ch = 256
    cw = 256
    h,w = image.shape[:2]
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    for row in range(0,h,ch):
        for col in range(0,w,cw):
            roi = gray[row:row+ch,col:cw+col]
            #阈值方法
            #ret,dst = cv.threshold(roi,0,255,cv.THRESH_BINARY)
            #全局阈值
            dst = cv.adaptiveThreshold(roi,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,127,20)
            #20消除的噪声范围（大于20+127的都为白色）
            gray[row:row+ch,col:cw+col] = dst
            print(np.std(dst),np.mean(dst))  #std标准差mean均值
    cv.imwrite('地址')

print('hi,python!')
src = cv.imread(r"F:\picture\ta.jpg")
cv.namedWindow('input image',cv.WINDOW_AUTOSIZE)
cv.imshow('input image',src)
cv.waitKey(0)
cv.destroyAllWindows()