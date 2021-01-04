# new day,new diff
# written in: 2020/11/26 19:46

from matplotlib import pyplot as plt
import cv2 as cv

def color_transfor(src):
    dst = cv.cvtColor(src,cv.COLOR_BGR2RGB)
    return dst

scr1 = cv.imread(r'F:/picture/5.jpg')
scr2 = cv.imread(r'F:/picture/6.jpg')
scr3 = cv.imread(r'F:/picture/8.jpg')
scr4 = cv.imread(r'F:/picture/she.jpg')
title = "hero"
plt.subplot(2,2,1)
scr1 = color_transfor(scr1)
plt.title(title,fontsize=8)
plt.imshow(scr1)

plt.subplot(2,2,2)
scr2 = color_transfor(scr2)
plt.title('flower')
plt.imshow(scr2)

plt.subplot(2,2,3)
scr3 = color_transfor(scr3)
plt.title('lines')
plt.imshow(scr3)

plt.subplot(2,2,4)
scr4 = color_transfor(scr4)
plt.title('she')
plt.imshow(scr4)
plt.show()
cv.waitKey(50000)