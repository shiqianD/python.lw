import cv2 as cv
import numpy as np
# contours外形轮廓

def measure_object(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    ret,binary = cv.threshold(gray,143,255,cv.THRESH_BINARY|cv.THRESH_OTSU)
    print('threshold value:%s'%ret)
    print('-'*8)
    cv.imshow('binary image',binary)
    dst = cv.cvtColor(binary,cv.COLOR_GRAY2BGR)
    contours,hierarchy=cv.findContours(binary,cv.RETR_CCOMP,cv.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contours):
        area = cv.contourArea(contour)
        #x,y,w,h = cv.boundingRect(contour)#轮廓的框位置
        mm = cv.moments(contour)    #计算图像中心距
        print(type(mm))
        if mm['m00']:
            cx = mm['m10']/mm['m00']
            cy = mm['m01'] / mm['m00']
            cv.circle(dst,(np.int(cx),np.int(cy)),3,(0,255,255),-1)
            #轮廓中心点
            #cv.rectangle(dst,(x,y),(x+w,y+h),(255,0,0),2)
            print('contour area %s'%area)
            approxCurve=cv.approxPolyDP(contour,4,True)
            print(approxCurve.shape)
            if approxCurve.shape[0]>5:#对图形形状逐次逼近/图形边数
                cv.drawContours(dst,contours,i,(255,0,0),2)
            if approxCurve.shape[0]==4:
                cv.drawContours(dst,contours,i,(0,0,255),2)
    cv.imshow('measure_contours',dst)

print('hi,python!')
src = cv.imread(r"F:\picture\12.jpg")
cv.namedWindow('input image',cv.WINDOW_AUTOSIZE)
cv.imshow('input image',src)
measure_object(src)
cv.waitKey(0)
cv.destroyAllWindows()