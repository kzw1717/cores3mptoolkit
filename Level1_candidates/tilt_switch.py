"""
Grove - Tilt Switch (SKU: 111020063)
------------------------------------
傾き（姿勢）でオン/オフが切り替わるデジタルスイッチ。
※ Arduinoスケッチ（キット付属マニュアル）の digitalRead 例を MicroPython へ移植。

対象   : M5Stack CoreS3 + UIFlow2 ファームウェア (MicroPython)
接続   : PORT.B  ( 黒=GND / 赤=5V / 黄=G9 / 白=G8 )  信号は 黄線 = G9
実行   : python -m mpremote run tilt_switch.py
終了   : Ctrl-C (PC側ターミナルで送信)
"""

from machine import Pin
import time

# --- 設定 ---------------------------------------------------------
SIG_PIN = 9          # PORT.B 黄線 (G9)
INTERVAL = 0.2       # loop() の実行間隔 [秒]

tilt = Pin(SIG_PIN, Pin.IN)


def setup():
    print("Grove Tilt Switch started (Ctrl-C to stop)")


def loop():
    if tilt.value() == 1:
        print("ON  : tilt detected")
    else:
        print("off : level")
    time.sleep(INTERVAL)


setup()
try:
    while True:
        loop()
except KeyboardInterrupt:
    print("stopped")
