"""
Grove - Water Sensor (SKU: 101020733)
-------------------------------------
基板上の導電パターンで水の有無・水滴を検知するセンサー。水検知で信号線が LOW(0)。
※ キット付属Arduinoスケッチ（digitalRead の値をそのまま表示）を標準MicroPythonへ移植。

対象   : M5Stack CoreS3 + UIFlow2 ファームウェア (MicroPython)
接続   : PORT.B  ( 黒=GND / 赤=5V / 黄=G9 / 白=G8 )  信号は 黄線 = G9
実行   : mpremote run water_sensor.py
終了   : Ctrl-C (PC側ターミナルで送信)
"""

from machine import Pin
import time

# --- 設定 ---------------------------------------------------------
SIG_PIN = 9          # PORT.B 黄線 (G9)
INTERVAL = 0.5       # loop() の実行間隔 [秒]

# 水検知で LOW(0)。CoreS3 では値を安定させるため内部プルアップを使う。
water = Pin(SIG_PIN, Pin.IN, Pin.PULL_UP)


def setup():
    print("Grove Water Sensor 開始 (Ctrl-C で終了)")


def loop():
    value = water.value()        # 0 か 1（Arduino の digitalRead に相当）
    if value == 0:
        print("water:", value, "(WET 水あり)")
    else:
        print("water:", value, "(dry 乾燥)")
    time.sleep(INTERVAL)


setup()
try:
    while True:
        loop()
except KeyboardInterrupt:
    print("終了しました")
