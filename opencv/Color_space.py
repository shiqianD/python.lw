import cv2 as cv

def color_space_demo(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    cv.imshow('gray',gray)
    hsv = cv.cvtColor(image,cv.COLOR_BGR2HSV)
    cv.imshow('hsv',hsv)
    Ycrcb = cv.cvtColor(image,cv.COLOR_BGR2YCrCb)
    cv.imshow('Ycrcb',Ycrcb)
    yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)
    cv.imshow('yuv', yuv)
    cv.imwrite(r'F:\picture\yuv.ta.jpg',yuv)
    #bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
    #bgr = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
    bgr = cv.applyColorMap(gray, cv.COLORMAP_)
    cv.imshow('bgr',bgr)




yuv=255
print('hi,python!')
src = cv.imread(r"F:\picture\ta.jpg")
cv.namedWindow('input image',cv.WINDOW_AUTOSIZE)
cv.imshow('input image',src)
color_space_demo(src)


cv.waitKey(0)
cv.destroyAllWindows()