"""
Grove - Button (SKU: 111020068)
-------------------------------
押している間だけオンになるモーメンタリ型プッシュボタン。
押すと HIGH(1)、離すと LOW(0)。
※ Arduinoスケッチ（キット付属マニュアル）の digitalRead 例を MicroPython へ移植。

対象   : M5Stack CoreS3 + UIFlow2 ファームウェア (MicroPython)
接続   : PORT.B  ( 黒=GND / 赤=5V / 黄=G9 / 白=G8 )  信号は 黄線 = G9
実行   : python -m mpremote run button.py
終了   : Ctrl-C (PC側ターミナルで送信)
"""

from machine import Pin  # type: ignore
import time  # type: ignore

# --- 設定 ---------------------------------------------------------
SIG_PIN = 9          # PORT.B 黄線 (G9)
INTERVAL = 0.1       # loop() の実行間隔 [秒]

button = Pin(SIG_PIN, Pin.IN)


def setup():
    print("Grove Button started (Ctrl-C to stop)")


def loop():
    if button.value() == 1:
        print("PRESSED : pressed")
    else:
        print("----    : released")
    time.sleep(INTERVAL)


setup()
try:
    while True:
        loop()
except KeyboardInterrupt:
    print("stopped")
