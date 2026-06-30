"""
CoreS3 ディスプレイ ── 図形：直線（出力）
------------------------------------------------------
2点 (x0, y0)-(x1, y1) を結ぶ直線を描きます。

実行 : mpremote run draw_line.py    終了 : Ctrl-C
API  : M5.Lcd.drawLine(x0, y0, x1, y1, color)
"""

import M5
import time


def setup():
    M5.begin()
    M5.Lcd.fillScreen(0x000000)
    M5.Lcd.setTextColor(0xFFFFFF, 0x000000)
    M5.Lcd.setTextSize(2)
    M5.Lcd.setCursor(10, 10)
    M5.Lcd.print("Line")

    M5.Lcd.drawLine(20, 60, 300, 60, 0xFF0000)     # 横線（赤）
    M5.Lcd.drawLine(20, 90, 300, 220, 0x00FF00)    # 斜め線（緑）
    M5.Lcd.drawLine(160, 80, 160, 230, 0x33CCFF)   # 縦線（水色）
    print("直線を表示しました (Ctrl-C で終了)")


def loop():
    M5.update()
    time.sleep(0.5)


setup()
try:
    while True:
        loop()
except KeyboardInterrupt:
    print("終了しました")
