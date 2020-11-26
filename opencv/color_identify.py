import cv2 as cv
import numpy as np

def extract_object_demo():
    capture = cv.VideoCapture(r'F:\video\video1.mp4')
    while 1:
        ret,frame = capture.read()
        if ret == False:
            break
        hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
        lower_hsv = np.array([100,43,46])#蓝色
        upper_hsv = np.array([124,255,255])
        mask = cv.inRange(hsv,lowerb=lower_hsv,upperb=upper_hsv)
        dst=cv.bitwise_and(frame,frame,mask=mask)
        cv.imshow('video',frame)
        #cv.imshow('mask',mask)#黑白图
        cv.imshow('dst', dst)#只有蓝色
        c = cv.waitKey(40)
        if c == 27:
            break


def color_space_demo(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    cv.imshow('gray',gray)
    hsv = cv.cvtColor(image,cv.COLOR_BGR2HSV)
    cv.imshow('hsv',hsv)
    Ycrcb = cv.cvtColor(image,cv.COLOR_BGR2YCrCb)
    cv.imshow('Ycrcb',Ycrcb)
    yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)
    cv.imshow('yuv', yuv)


print('hi,python!')
src = cv.imread(r"F:\picture\ta.jpg")
cv.namedWindow('input image',cv.WINDOW_AUTOSIZE)
cv.imshow('input image',src)
#color_space_demo(src)
extract_object_demo()
cv.waitKey(0)
cv.destroyAllWindows()