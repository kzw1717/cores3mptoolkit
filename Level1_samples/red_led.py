"""
Grove - Red LED (SKU: 104030005)
--------------------------------
赤色LEDモジュール。デジタル信号で点灯/消灯を制御します。
このサンプルでは 0.5 秒ごとに点滅させます。

対象   : M5Stack CoreS3 + UIFlow2 ファームウェア (MicroPython)
接続   : PORT.B  ( 黒=GND / 赤=5V / 黄=G9 / 白=G8 )
         LEDの制御信号は 黄線 = G9 です
実行   : mpremote run red_led.py
終了   : Ctrl-C (PC側ターミナルで送信)
"""

from machine import Pin
import time

# --- 設定 ---------------------------------------------------------
SIG_PIN = 9          # PORT.B 黄線 (G9)
INTERVAL = 0.5       # 点灯/消灯の間隔 [秒]

# グローバル変数 (setup() で初期化)
led = None
state = 0


def setup():
    """起動時に一度だけ実行する初期化処理"""
    global led
    led = Pin(SIG_PIN, Pin.OUT)
    print("Grove Red LED 開始 (Ctrl-C で終了)")


def loop():
    """繰り返し実行する処理"""
    global state
    state = 1 - state            # 0/1 を反転
    led.value(state)
    print("LED:", "ON" if state else "off")
    time.sleep(INTERVAL)


# --- エントリポイント ---------------------------------------------
setup()
try:
    while True:
        loop()
except KeyboardInterrupt:
    led.value(0)                 # 終了時は消灯
    print("終了しました")
