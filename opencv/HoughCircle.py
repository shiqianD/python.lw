import cv2 as cv

# 载入并显示图片
img = cv.imread(r"F:\picture\10.jpg")
cv.imshow('img', img)
# 灰度化
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# 输出图像大小，方便根据图像大小调节minRadius和maxRadius
print('img.shape:',img.shape)
# 霍夫变换圆检测
circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1,
                           70, param1=100, param2=30, minRadius=5, maxRadius=300)
# 输出返回值，方便查看类型
print(circles)
print('------------------------------')
print(circles[0])#包含检测出来的圆的信息的数组
print('------------------------------')
# 输出检测到圆的个数
print(len(circles[0]))
print('------------------------------')
# 根据检测到圆的信息，画出每一个圆
for circle in circles[0]:
    # 圆的基本信息
    print(circle[2])
    print(circle)#circle三维数组0，1，2分别为坐标行列半径
    # 坐标行列
    x = int(circle[0])
    y = int(circle[1])
    # 半径
    r = int(circle[2])
    # 在原图用指定颜色标记出圆的位置
    img = cv.circle(img, (x, y), r, (0, 0, 255), 3)
    img = cv.circle(img, (x, y), 10, (255, 0, 0), -1)
# 显示新图像
cv.imshow('res', img)

# 按任意键退出
cv.waitKey(0)
cv.destroyAllWindows()