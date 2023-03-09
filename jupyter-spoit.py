import ipywidgets as widgets
from IPython.display import display
from PIL import Image

# 画像を読み込む
img = Image.open("sample_image.jpg")

# 画像を表示する
display(img)

# スポイト用のウィジェットを作成する
color_picker = widgets.ColorPicker(
    concise=False,
    description='Pick a color',
    value='black',
    disabled=False
)

# スポイトをクリックした際の処理
def on_color_picked(change):
    r, g, b = img.getpixel((change['new'][0], change['new'][1]))
    print(f"R:{r} G:{g} B:{b}")

color_picker.observe(on_color_picked, names='value')

# ウィジェットを表示する
display(color_picker)
