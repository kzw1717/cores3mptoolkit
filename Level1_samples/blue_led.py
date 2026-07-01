"""
Grove - Blue LED (SKU: 104020196)
---------------------------------
青色LEDモジュール。デジタル信号で点灯/消灯を制御します。
このサンプルでは 0.5 秒ごとに点滅させます。

対象   : M5Stack CoreS3 + UIFlow2 ファームウェア (MicroPython)
接続   : PORT.B  ( 黒=GND / 赤=5V / 黄=G9 / 白=G8 )
         LEDの制御信号は 黄線 = G9 です
実行   : python -m mpremote run blue_led.py
終了   : Ctrl-C (PC側ターミナルで送信)
"""

from machine import Pin
import time

# --- 設定 ---------------------------------------------------------
SIG_PIN = 9          # PORT.B 黄線 (G9)
INTERVAL = 0.5       # 点灯/消灯の間隔 [秒]

# LED を出力として用意する
led = Pin(SIG_PIN, Pin.OUT)


def setup():
    """起動時に一度だけ実行する処理"""
    print("Grove Blue LED started (Ctrl-C to stop)")


def loop():
    """繰り返し実行する処理：点灯 → 待つ → 消灯 → 待つ"""
    led.value(1)              # 1 で点灯
    print("LED: ON")
    time.sleep(INTERVAL)
    led.value(0)              # 0 で消灯
    print("LED: off")
    time.sleep(INTERVAL)


# --- エントリポイント ---------------------------------------------
setup()
try:
    while True:
        loop()
except KeyboardInterrupt:
    led.value(0)             # 終了時は消灯
    print("stopped")
