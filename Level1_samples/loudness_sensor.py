"""
Grove - Loudness Sensor (SKU: 101020063)
----------------------------------------
マイクの音量を増幅し、周囲の騒音レベルをアナログ値で出力する音量センサー。
音が大きいほど値が大きくなります。

対象   : M5Stack CoreS3 + UIFlow2 ファームウェア (MicroPython)
接続   : PORT.B  ( 黒=GND / 赤=5V / 黄=G9 / 白=G8 )
         センサーの信号は 黄線 = G9 (ADC) で読み取ります
実行   : mpremote run loudness_sensor.py
終了   : Ctrl-C (PC側ターミナルで送信)
"""

from machine import Pin, ADC
import time

# --- 設定 ---------------------------------------------------------
SIG_PIN = 9          # PORT.B 黄線 (G9)
INTERVAL = 0.1       # loop() の実行間隔 [秒]

# グローバル変数 (setup() で初期化)
sound = None


def setup():
    """起動時に一度だけ実行する初期化処理"""
    global sound
    sound = ADC(Pin(SIG_PIN))
    sound.atten(ADC.ATTN_11DB)   # 入力レンジ 0-3.3V
    print("Grove Loudness Sensor 開始 (Ctrl-C で終了)")


def loop():
    """繰り返し実行する処理"""
    value = sound.read_u16()     # 0-65535
    print("loudness:", value)
    time.sleep(INTERVAL)


# --- エントリポイント ---------------------------------------------
setup()
try:
    while True:
        loop()
except KeyboardInterrupt:
    print("終了しました")
