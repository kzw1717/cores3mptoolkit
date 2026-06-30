"""
CoreS3 ディスプレイ ── 図形：三角形（出力）
------------------------------------------------------
3点 (x0,y0)(x1,y1)(x2,y2) を結ぶ三角形を描きます。

実行 : mpremote run draw_triangle.py    終了 : Ctrl-C
API  : M5.Lcd.drawTriangle(x0,y0,x1,y1,x2,y2,color) / fillTriangle(...)
"""

import M5
import time


def setup():
    M5.begin()
    M5.Lcd.fillScreen(0x000000)
    M5.Lcd.setTextColor(0xFFFFFF, 0x000000)
    M5.Lcd.setTextSize(2)
    M5.Lcd.setCursor(10, 10)
    M5.Lcd.print("Triangle")

    M5.Lcd.drawTriangle(80, 60, 30, 170, 130, 170, 0xFFFF00)    # 枠線（黄）
    M5.Lcd.fillTriangle(240, 60, 190, 170, 290, 170, 0xFF00FF)  # 塗りつぶし（マゼンタ）
    print("三角形を表示しました (Ctrl-C で終了)")


def loop():
    M5.update()
    time.sleep(0.5)


setup()
try:
    while True:
        loop()
except KeyboardInterrupt:
    print("終了しました")
