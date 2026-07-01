"""
Grove - Mini PIR Motion Sensor (SKU: 101020741)
-----------------------------------------------
焦電型赤外線で人や動物の動きを検知する小型PIRモーションセンサー。
動きを検知すると信号が HIGH になります。

対象   : M5Stack CoreS3 + UIFlow2 ファームウェア (MicroPython)
接続   : PORT.B  ( 黒=GND / 赤=5V / 黄=G9 / 白=G8 )
         センサーの信号は 黄線 = G9 で読み取ります
実行   : python -m mpremote run pir_motion_sensor.py
終了   : Ctrl-C (PC側ターミナルで送信)
"""

from machine import Pin
import time

# --- 設定 ---------------------------------------------------------
SIG_PIN = 9          # PORT.B 黄線 (G9)
INTERVAL = 0.2       # loop() の実行間隔 [秒]

# グローバル変数 (setup() で初期化)
pir = None


def setup():
    """起動時に一度だけ実行する初期化処理"""
    global pir
    pir = Pin(SIG_PIN, Pin.IN)
    print("Grove Mini PIR Motion Sensor started (Ctrl-C to stop)")


def loop():
    """繰り返し実行する処理"""
    if pir.value() == 1:
        print("MOTION : motion detected")
    time.sleep(INTERVAL)


# --- エントリポイント ---------------------------------------------
setup()
try:
    while True:
        loop()
except KeyboardInterrupt:
    print("stopped")
