import cv2 as cv
import numpy as np

drawing=False
mode = True
ix,iy=-1,-1#鼠标初始定位

def nothing(x):
    pass

def onMouse(event,x,y,flag,param):#x,y画图时的位置
    b = cv.getTrackbarPos('b',winName)
    g = cv.getTrackbarPos('g',winName)
    r = cv.getTrackbarPos('r',winName)
    color = (b,g,r)#下面画图时的线色
    global ix,iy,drawing,mode
    if event ==cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy=x,y
    elif event== cv.EVENT_MOUSEMOVE and flag == cv.EVENT_FLAG_LBUTTON:
        if drawing:
            if mode:
                cv.rectangle(img,(ix,iy),(x,y),color,-1)
            else:
                cv.circle(img,(x,y),3,color,-1)#虽然是画圆，但是r足够小
    elif event ==cv.EVENT_RBUTTONDOWN:
        if drawing:
            if mode:
                cv.circle(img,(x,y),60,color,3)
    elif event == cv.EVENT_LBUTTONUP:  # 当鼠标松开停止绘画
        if mode is True:
            cv.rectangle(img, (ix, iy), (x, y), (255, 255, 255), 5)  # 松开鼠标后画一个白色矩形

src1 = cv.imread(r'F:\picture\A.jpg')
top = cv.resize(src1,(500,500),interpolation=cv.INTER_AREA)
src2 = cv.imread(r'F:\picture\I.jpg')
bottom = cv.resize(src2,(500,500),interpolation=cv.INTER_AREA)
winName = 'result'
img = np.ones(top.shape,np.uint8)
cv.namedWindow(winName,cv.WINDOW_AUTOSIZE)
cv.createTrackbar('transform',winName,0,100,nothing)
cv.createTrackbar('overlap',winName,0,100,nothing)
cv.createTrackbar('b',winName,0,255,nothing)
cv.createTrackbar('g',winName,0,255,nothing)
cv.createTrackbar('r',winName,0,255,nothing)
cv.setMouseCallback(winName,onMouse)
while 1:
    a = cv.getTrackbarPos('transform',winName)
    b = cv.getTrackbarPos('overlap',winName)
    overlap = cv.addWeighted(bottom,1-a/100,top,a/100,0)
    add = cv.addWeighted(overlap,1-b/100,img,b/100,0)
    cv.imshow('result',add)
    k = cv.waitKey(1)
    if k ==ord('m'):
        mode = not mode
    elif k==27:
        break
cv.destroyAllWindows()