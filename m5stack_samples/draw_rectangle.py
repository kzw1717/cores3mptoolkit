"""
CoreS3 ディスプレイ ── 図形：四角形（出力）
------------------------------------------------------
四角形を描きます。枠線のみ drawRect、塗りつぶし fillRect。

実行 : python -m mpremote run draw_rectangle.py    終了 : Ctrl-C
API  : M5.Lcd.drawRect(x, y, w, h, color) / fillRect(x, y, w, h, color)
"""

import M5  # type: ignore
import time  # type: ignore


def setup():
    M5.begin()
    M5.Lcd.fillScreen(0x000000)
    M5.Lcd.setTextColor(0xFFFFFF, 0x000000)
    M5.Lcd.setTextSize(2)
    M5.Lcd.setCursor(10, 10)
    M5.Lcd.print("Rectangle")

    M5.Lcd.drawRect(30, 70, 110, 90, 0x00FF00)    # 枠線（緑）
    M5.Lcd.fillRect(180, 70, 110, 90, 0x0000FF)   # 塗りつぶし（青）
    print("Rectangle drawn (Ctrl-C to stop)")


def loop():
    M5.update()
    time.sleep(0.5)


setup()
try:
    while True:
        loop()
except KeyboardInterrupt:
    print("stopped")
