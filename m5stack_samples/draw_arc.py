"""
CoreS3 ディスプレイ ── 図形：円弧／扇形（出力）
------------------------------------------------------
中心 (x, y)、内半径 r0・外半径 r1、開始角 angle0〜終了角 angle1[度] の
円弧（リング状）／扇形を描きます。角度は時計回り、右方向が 0 度。

実行 : python -m mpremote run draw_arc.py    終了 : Ctrl-C
API  : M5.Lcd.drawArc(x, y, r0, r1, angle0, angle1, color) / fillArc(...)
"""

import M5  # type: ignore
import time  # type: ignore


def setup():
    M5.begin()
    M5.Lcd.fillScreen(0x000000)
    M5.Lcd.setTextColor(0xFFFFFF, 0x000000)
    M5.Lcd.setTextSize(2)
    M5.Lcd.setCursor(10, 10)
    M5.Lcd.print("Arc")

    M5.Lcd.drawArc(90, 140, 35, 55, 0, 270, 0xFFFF00)    # 円弧（黄, 0-270度）
    M5.Lcd.fillArc(230, 140, 0, 55, 0, 120, 0x9C27B0)    # 扇形（紫, 0-120度）
    print("Arc drawn (Ctrl-C to stop)")


def loop():
    M5.update()
    time.sleep(0.5)


setup()
try:
    while True:
        loop()
except KeyboardInterrupt:
    print("stopped")
