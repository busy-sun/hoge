from tkinter import *
from PIL import Image, ImageTk

# 画像ファイルのパス
IMAGE_PATH = "example.jpg"

# 画像を開く
image = Image.open(IMAGE_PATH)

# Jupyter Notebookで画像を表示するための設定
%matplotlib inline
import matplotlib.pyplot as plt
plt.imshow(image)

# 画像を表示するためのキャンバスを作成する
canvas = Canvas(width=image.width, height=image.height)
canvas.pack()

# 画像をキャンバスに描画する
img_tk = ImageTk.PhotoImage(image)
canvas.create_image(0, 0, image=img_tk, anchor="nw")

# クリックされたときに呼び出される関数
def click(event):
    # クリックされた座標を取得する
    x, y = event.x, event.y
    
    # 座標の色を取得する
    color = image.getpixel((x, y))
    print(color)

# クリックされたときにclick関数を呼び出すように設定する
canvas.bind("<Button-1>", click)
