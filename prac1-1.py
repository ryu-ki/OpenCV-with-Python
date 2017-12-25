#coding:utf-8

#練習1-1　画像を読み込み、表示する

import cv2
import os,sys

filename = input("Filename:")
if not os.path.exists(filename):
    print("Not Found!")
    sys.exit()

img = cv2.imread(filename, 1)
cv2.namedWindow(filename,cv2.WINDOW_NORMAL)
cv2.imshow(filename,img)
cv2.waitKey(0)
cv2.destroyAllWindows()
