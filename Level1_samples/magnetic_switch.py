"""
Grove - Magnetic Switch (SKU: 101020038)
----------------------------------------
磁石の接近をリードスイッチで検知するデジタル磁気近接スイッチ。
磁石が近づくと信号が変化します。

対象   : M5Stack CoreS3 + UIFlow2 ファームウェア (MicroPython)
接続   : PORT.B  ( 黒=GND / 赤=5V / 黄=G9 / 白=G8 )
         センサーの信号は 黄線 = G9 で読み取ります
実行   : mpremote run magnetic_switch.py
終了   : Ctrl-C (PC側ターミナルで送信)
"""

from machine import Pin
import time

# --- 設定 ---------------------------------------------------------
SIG_PIN = 9          # PORT.B 黄線 (G9)
INTERVAL = 0.2       # loop() の実行間隔 [秒]

# グローバル変数 (setup() で初期化)
magnet = None


def setup():
    """起動時に一度だけ実行する初期化処理"""
    global magnet
    magnet = Pin(SIG_PIN, Pin.IN, Pin.PULL_DOWN)
    print("Grove Magnetic Switch 開始 (Ctrl-C で終了)")


def loop():
    """繰り返し実行する処理"""
    if magnet.value() == 1:
        print("MAGNET : 磁石を検知しました")
    else:
        print("----   : 検知なし")
    time.sleep(INTERVAL)


# --- エントリポイント ---------------------------------------------
setup()
try:
    while True:
        loop()
except KeyboardInterrupt:
    print("終了しました")
