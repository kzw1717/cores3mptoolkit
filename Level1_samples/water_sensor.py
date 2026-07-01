"""
Grove - Water Sensor (SKU: 101020733)
-------------------------------------
基板上の導電パターンで水の有無・水滴を検知するセンサー。
水を検知すると信号線が LOW になります。

対象   : M5Stack CoreS3 + UIFlow2 ファームウェア (MicroPython)
接続   : PORT.B  ( 黒=GND / 赤=5V / 黄=G9 / 白=G8 )
         水センサーの信号は 黄線 = G9 で読み取ります
実行   : mpremote run water_sensor.py
終了   : Ctrl-C
"""

from machine import Pin
import time

# --- 設定 ---------------------------------------------------------
SIG_PIN = 9          # PORT.B 黄線 (G9)
INTERVAL = 0.5       # loop() の実行間隔 [秒]

# グローバル変数 (setup() で初期化)
water = None


def setup():
    """起動時に一度だけ実行する初期化処理"""
    global water
    # Grove Water Sensor はオープンコレクタ出力のため内部プルアップを使用
    # 水検知 -> LOW(0) / 乾燥 -> HIGH(1)
    water = Pin(SIG_PIN, Pin.IN, Pin.PULL_UP)
    print("Grove Water Sensor 開始 (Ctrl-C で終了)")


def loop():
    """繰り返し実行する処理"""
    if water.value() == 0:
        print("WET : 水を検知しました")
    else:
        print("dry : 乾燥")
    time.sleep(INTERVAL)


# --- エントリポイント ---------------------------------------------
setup()
try:
    while True:
        loop()
except KeyboardInterrupt:
    print("終了しました")
