"""
Grove - Switch(P) (SKU: 111020067)
----------------------------------
スライド式の自己保持型トグルスイッチ。オン/オフ状態をデジタル出力。
※ Arduinoスケッチ（キット付属マニュアル）の digitalRead 例を MicroPython へ移植。

対象   : M5Stack CoreS3 + UIFlow2 ファームウェア (MicroPython)
接続   : PORT.B  ( 黒=GND / 赤=5V / 黄=G9 / 白=G8 )  信号は 黄線 = G9
実行   : mpremote run switch_p.py
終了   : Ctrl-C (PC側ターミナルで送信)
"""

from machine import Pin
import time

# --- 設定 ---------------------------------------------------------
SIG_PIN = 9          # PORT.B 黄線 (G9)
INTERVAL = 0.2       # loop() の実行間隔 [秒]

switch = Pin(SIG_PIN, Pin.IN)


def setup():
    print("Grove Switch(P) 開始 (Ctrl-C で終了)")


def loop():
    if switch.value() == 1:
        print("ON  : スイッチ ON")
    else:
        print("off : スイッチ OFF")
    time.sleep(INTERVAL)


setup()
try:
    while True:
        loop()
except KeyboardInterrupt:
    print("終了しました")
