import cv2 as cv
import numpy as np
#pixels像素filter滤波
def access_pixels(image):
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    print('width : %s,height : %s,channel : %s' %(width,height,channels))
    for row in range(height):
        for col in range(width):
            for c in range(channels):
                pv = image[row,col,c]
                image[row,col,c] = 255 - pv
    cv.imshow('pixels_demo',image)

def inverse(image1):
    dst = cv.bitwise_not(image1)
    cv.imshow('pixel_demo',dst)

def create_image():
    img = np.zeros([400,400,3],np.uint8)
    img[:,:,1] = np.ones([400,400])*255
    cv.imshow('new image',img)

print('hi,python!')
src = cv.imread(r"F:\picture\she.jpg")#biue,greet,red
cv.namedWindow('input image',cv.WINDOW_AUTOSIZE)
cv.imshow('input image',src)
t1 = cv.getTickCount()
#access_pixels(src)#rgb像素取反
#inverse(src)#像素转换
create_image()
t2 = cv.getTickCount()
time = (t2-t1)/cv.getTickFrequency()
print('time : %s ms'% (time*1000))
cv.waitKey(0)
cv.destroyAllWindows()