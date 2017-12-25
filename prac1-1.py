#coding:utf-8

#練習1-1　画像を読み込み、表示する

import cv2 #OpenCV
import os,sys　

#画像ファイル名
filename = input("Filename:")
#ファイルが存在するかの確認
if not os.path.exists(filename):
    print("Not Found!")
    sys.exit()

#画像ファイルの読み込み   
img = cv2.imread(filename, 1)
#ウィンドウのサイズを自由に変更可
cv2.namedWindow(filename,cv2.WINDOW_NORMAL)
#画像を表示
cv2.imshow(filename,img)
#終了処理
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
画像の読み込むための関数:cv2.imread()
・第一引数は画像ファイル名、第二引数は1,0,-1の3通りの読み込みモード。1はカラー画像、0はグレースケール画像,-1はアルファチャンネルを含めた画像
画像を表示するための関数:cv2.imshow()
・第一引数はウィンドウ名、第二引数は表示する画像
キーボード入力を処理する関数:cv2.waitKey()
・引数に0を指定すれば、何かのキーが入力されるまで無期限で待つ。
終了処理:cv2.destroyAllWindows()
・現在までに作られたウィンドウをすべて閉じる。
"""
