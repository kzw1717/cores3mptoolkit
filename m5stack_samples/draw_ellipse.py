"""
CoreS3 ディスプレイ ── 図形：楕円（出力）
------------------------------------------------------
楕円を描きます。(x, y) が中心、rx が横半径、ry が縦半径です。

実行 : mpremote run draw_ellipse.py    終了 : Ctrl-C
API  : M5.Lcd.drawEllipse(x, y, rx, ry, color) / fillEllipse(x, y, rx, ry, color)
"""

import M5
import time


def setup():
    M5.begin()
    M5.Lcd.fillScreen(0x000000)
    M5.Lcd.setTextColor(0xFFFFFF, 0x000000)
    M5.Lcd.setTextSize(2)
    M5.Lcd.setCursor(10, 10)
    M5.Lcd.print("Ellipse")

    M5.Lcd.drawEllipse(90, 130, 60, 35, 0xFF00FF)    # 枠線（マゼンタ）
    M5.Lcd.fillEllipse(230, 130, 55, 35, 0x00FF00)   # 塗りつぶし（緑）
    print("楕円を表示しました (Ctrl-C で終了)")


def loop():
    M5.update()
    time.sleep(0.5)


setup()
try:
    while True:
        loop()
except KeyboardInterrupt:
    print("終了しました")
