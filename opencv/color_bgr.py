import cv2 as cv
import numpy as np
def extract_object_demo():
    capture = cv.VideoCapture(r'F:\video\video1.mp4')
    while 1:
        ret,frame = capture.read()
        if ret == False:
            break
        hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
        lower_hsv = np.array([100,43,46])#颜色
        upper_hsv = np.array([124,255,255])
        mask = cv.inRange(hsv,lowerb=lower_hsv,upperb=upper_hsv)
        cv.imshow('video',frame)
        cv.imshow('mask',mask)
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
#cv.imshow('input image',src)
#color_space_demo(src)
#b,g,r= cv.split(src)    #cv.imshow('blue',b)  cv.imshow('green',g)    cv.imshow('red',r)
# src[:,:,0]= 0#红＋绿=黄(011)黄青交换
# cv.imshow('change src',src)
# cv.waitKey(500)
# src[:,:,2]= 0#绿＋蓝=青110
# cv.imshow('change src',src)
# cv.waitKey(0)
#src = cv.merge([b,g,r])#合并三个通道
extract_object_demo()
cv.waitKey(0)
cv.destroyAllWindows()