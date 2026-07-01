"""
CoreS3 ディスプレイ ── 図形：角丸四角形（出力）
------------------------------------------------------
角の丸い四角形を描きます。引数 r が角の半径です。

実行 : python -m mpremote run draw_roundrect.py    終了 : Ctrl-C
API  : M5.Lcd.drawRoundRect(x, y, w, h, r, color) / fillRoundRect(x, y, w, h, r, color)
"""

import M5
import time


def setup():
    M5.begin()
    M5.Lcd.fillScreen(0x000000)
    M5.Lcd.setTextColor(0xFFFFFF, 0x000000)
    M5.Lcd.setTextSize(2)
    M5.Lcd.setCursor(10, 10)
    M5.Lcd.print("Round Rectangle")

    M5.Lcd.drawRoundRect(30, 70, 110, 90, 15, 0x00FF00)    # 枠線（緑）
    M5.Lcd.fillRoundRect(180, 70, 110, 90, 20, 0xFF9800)   # 塗りつぶし（橙）
    print("Round rectangle drawn (Ctrl-C to stop)")


def loop():
    M5.update()
    time.sleep(0.5)


setup()
try:
    while True:
        loop()
except KeyboardInterrupt:
    print("stopped")
