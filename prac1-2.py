#coding:utf-8

#練習1-2　画像の保存（今回はある画像を読み込み、そのグレースケール画像を保存）

import cv2
import os,sys

#画像ファイル名
filename = input("Filename:")
#保存ファイル名

if not os.path.exists(filename):
    print("Not Found!")
    sys.exit()

img = cv2.imread(filename, 0)
cv2.namedWindow(filename,cv2.WINDOW_NORMAL)
cv2.imshow(filename,img)
cv2.imwrite("grayscale.png",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
