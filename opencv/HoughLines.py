import cv2 as cv
import numpy as np

def line_detection(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray,50,150,3)#框架宽度
    lines = cv.HoughLines(edges,1,np.pi/180,123)
    #生成极坐标时的扫描步长rho，扫描角度步长theta，阈值的低值#返回值为rho，theta
    #'NoneType' object is not iterable阈值过高lines=none
    for line in lines:
        rho,theta = line[0]
        a= np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho  #x=pcos0
        y0 = b*rho
        x1 = int(x0+1000*(-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv.line(image,(x1,y1),(x2,y2),(0,0,255),2)
    cv.imshow('image_lines',image)


print('hi,python!')
src = cv.imread(r"F:\picture\3.jpg")
cv.namedWindow('input image',cv.WINDOW_AUTOSIZE)
cv.imshow('input image',src)
line_detection(src)
cv.waitKey(0)
cv.destroyAllWindows()