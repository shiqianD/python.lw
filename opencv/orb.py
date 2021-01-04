# new day,new diff
# written in: 2020/11/28 13:12
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('F:/picture/20.jpg', 0)
orb = cv2.ORB_create(nfeatures=100)
# 使用ORB检测特征点
kp = orb.detect(img, None)
# compute the descriptors with ORB
kp, des = orb.compute(img, kp)
# 绘制特征点
img2 = cv2.drawKeypoints(img, kp, None, color=(0, 255, 0), flags=0)
plt.imshow(img2, cmap='gray'), plt.title('ORB')
plt.show()
