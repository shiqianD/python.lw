import cv2 as cv
import numpy as np

def fill_binary():
    image = np.zeros([400,400,3],np.uint8)
    image[100:300,100:300,:]=200
    cv.imshow('fill',image)

    mask= np.ones([402, 402, 1], np.uint8)
    mask[101:301, 101:301] = 0
    cv.floodFill(image,mask,(200,200),(100,2,255),cv.FLOODFILL_MASK_ONLY)#使用floodfill时mask定义为0
    cv.imshow('filled', image)


print('hi,python!')
src = cv.imread(r"F:\picture\ta.jpg")
cv.namedWindow('input image',cv.WINDOW_AUTOSIZE)
cv.imshow('input image',src)
fill_binary()
cv.waitKey(0)
cv.destroyAllWindows()
