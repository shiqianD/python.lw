# new day,new diff
# written in: 2020/10/26 21:08
import cv2 as cv
import numpy as np
def nothing(x):  # 滑动条的回调函数
    pass


def houghLine_demo(edges):
    cv.namedWindow(WindowName, cv.WINDOW_AUTOSIZE)  # 建立空窗口
    cv.createTrackbar('threshold', WindowName, 0, 100, nothing)  # 阈值滑动条，霍夫空间交点数量
    cv.createTrackbar('minLineLength', WindowName, 0, 50, nothing)  # 最短线段长度滑动条
    cv.createTrackbar('maxLineGap', WindowName, 0, 100, nothing)  # 最大线段间距滑动条
    while True:
        img=src.copy()
        threshold = cv.getTrackbarPos('threshold', WindowName)  # 获取滑动条值
        minLineLength = cv.getTrackbarPos('minLineLength', WindowName)  # 获取滑动条值
        maxLineGap = cv.getTrackbarPos('maxLineGap', WindowName)  # 获取滑动条值
        lines=cv.HoughLinesP(edges, 0.5, np.pi / 180, threshold=threshold, minLineLength=minLineLength, maxLineGap=maxLineGap)
        #返回直线端点两点坐标列表
        for line in lines:
            x1,y1,x2,y2 = line[0]
            cv.line(img, (x1, y1), (x2, y2), (0,0 ,255), 1)
        cv.imshow(WindowName, img)
        k = cv.waitKey(1) & 0xFF
        if k == 27:
            break


def houghCircle_demo(edges):
    cv.namedWindow(WindowName, cv.WINDOW_AUTOSIZE)  # 建立空窗口
    while True:
        img = src.copy()
        circles=cv.HoughCircles(edges,cv.HOUGH_GRADIENT,dp=0.5,minDist=55, param1=1, param2=21, minRadius=10, maxRadius=40)
        #image, method，dp,minDist,circles,param1参数dp累加器分辨率与图像分辨率的反比 dp=1，累加器的分辨率与输入图像相同。如果dp=2，累加器分辨率为宽度和高度的一半
        #param2:累加器阈值,多少个霍夫空间确定一个圆,越大越少
        #返回三重列表包含三个值：圆心坐标x，y，半径
        for circle in circles[0]:
            x= int(circle[0])
            y= int(circle[1])
            r = int(circle[2])
            cv.circle(img,(x,y),r,(255,0,255),2)
        cv.imshow(WindowName, img)
        k = cv.waitKey(1) & 0xFF
        if k == 27:
            break


src = cv.imread(r"F:\picture\17.jpg")
srcBlur = cv.GaussianBlur(src, (3, 3), 0)   # 高斯滤波
gray = cv.cvtColor(srcBlur, cv.COLOR_BGR2GRAY)
edge = cv.Canny(gray, 50, 150, apertureSize=3)
WindowName = 'result'  # 窗口名
cv.imshow('src', src)
print('输入l开始直线检测，输入c开始圆检测')
while True:
    k = cv.waitKey(1) & 0xFF
    if k == ord('l'):
        houghLine_demo(edge)
    elif k== ord('c'):
        houghCircle_demo(edge)
    elif k ==27:
        break
cv.destroyAllWindows()