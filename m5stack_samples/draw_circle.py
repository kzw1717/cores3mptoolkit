"""
CoreS3 ディスプレイ ── 図形：円（出力）
------------------------------------------------------
円を描きます。(x, y) が中心、r が半径です。

実行 : mpremote run draw_circle.py    終了 : Ctrl-C
API  : M5.Lcd.drawCircle(x, y, r, color) / fillCircle(x, y, r, color)
"""

import M5
import time


def setup():
    M5.begin()
    M5.Lcd.fillScreen(0x000000)
    M5.Lcd.setTextColor(0xFFFFFF, 0x000000)
    M5.Lcd.setTextSize(2)
    M5.Lcd.setCursor(10, 10)
    M5.Lcd.print("Circle")

    M5.Lcd.drawCircle(90, 130, 50, 0x33CCFF)    # 枠線（水色）
    M5.Lcd.fillCircle(230, 130, 50, 0x00FFFF)   # 塗りつぶし（シアン）
    print("円を表示しました (Ctrl-C で終了)")


def loop():
    M5.update()
    time.sleep(0.5)


setup()
try:
    while True:
        loop()
except KeyboardInterrupt:
    print("終了しました")
