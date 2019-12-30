from glob import glob
import cv2
import numpy as np

img = cv2.imread('gt2/Tp_D_CND_M_N_art00076_art00077_10289_gt.png')
#img = cv2.imread(imgs)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 使用Otsu自动阈值，注意用的是cv2.THRESH_BINARY_INV
ret, thresh = cv2.threshold(img_gray, 0, 255, 0)
cv2.imwrite('gray.png', img_gray)
# 寻找轮廓
image, contours, hierarchy = cv2.findContours(thresh, 3, 2)

c = len(contours)
print(c)

img_color1 = np.copy(img)
img_color2 = np.copy(img)

for cc in range(c):
    cnt = contours[cc]
    cv2.drawContours(img_color1, contours[cc], 1, (0,0,255), 3)
    x, y, w, h = cv2.boundingRect(cnt)  # 外接矩形
    cv2.rectangle(img_color2, (x,y), (x+w, y+h), (0, 255, 0), 2)

cv2.imwrite('bound.png', img_color1)
cv2.imwrite('box.png', img_color2)
