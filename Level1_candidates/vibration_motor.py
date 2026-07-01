"""
Grove - Vibration Motor (SKU: 108020121)
----------------------------------------
デジタル信号で振動する小型バイブレーションモーター（HIGHで振動 / LOWで停止）。
※ キット付属Arduinoスケッチ（digitalWrite HIGH/LOW）を標準MicroPythonへ移植。

対象   : M5Stack CoreS3 + UIFlow2 ファームウェア (MicroPython)
接続   : PORT.B  ( 黒=GND / 赤=5V / 黄=G9 / 白=G8 )  信号は 黄線 = G9
実行   : python -m mpremote run vibration_motor.py
終了   : Ctrl-C (PC側ターミナルで送信)
"""

from machine import Pin
import time

# --- 設定 ---------------------------------------------------------
SIG_PIN = 9          # PORT.B 黄線 (G9)
INTERVAL = 1.0       # 振動/停止の間隔 [秒]

motor = Pin(SIG_PIN, Pin.OUT)


def setup():
    print("Grove Vibration Motor started (Ctrl-C to stop)")


def loop():
    motor.value(1)            # 振動
    print("VIB : vibrating")
    time.sleep(INTERVAL)
    motor.value(0)            # 停止
    print("--- : stopped")
    time.sleep(INTERVAL)


setup()
try:
    while True:
        loop()
except KeyboardInterrupt:
    motor.value(0)            # 終了時は停止
    print("stopped")
