#coding:utf-8

#練習1-2　画像の保存（今回はある画像を読み込み、そのグレースケール画像を保存）

import cv2
import os,sys

#画像ファイル名
filename = input("Filename:")

if not os.path.exists(filename):
    print("Not Found!")
    sys.exit()

img = cv2.imread(filename, 0)
cv2.namedWindow(filename,cv2.WINDOW_NORMAL)
cv2.imshow(filename,img)
cv2.imwrite("grayscale.png",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
画像の保存:cv2.imwrite()
・第一引数は画像のファイル名、第二引数は保存したいファイル名
"""
