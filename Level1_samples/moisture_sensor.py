"""
Grove - Moisture Sensor (SKU: 101020008)
----------------------------------------
土壌中の水分量をアナログ値で測定する土壌水分センサー。
土が湿っているほど値が大きくなります。

対象   : M5Stack CoreS3 + UIFlow2 ファームウェア (MicroPython)
接続   : PORT.B  ( 黒=GND / 赤=5V / 黄=G9 / 白=G8 )
         センサーの信号は 黄線 = G9 (ADC) で読み取ります
実行   : mpremote run moisture_sensor.py
終了   : Ctrl-C (PC側ターミナルで送信)
"""

from machine import Pin, ADC
import time

# --- 設定 ---------------------------------------------------------
SIG_PIN = 9          # PORT.B 黄線 (G9)
INTERVAL = 0.5       # loop() の実行間隔 [秒]
WET_LEVEL = 30000    # この値以上を「湿っている」と簡易判定 (要調整)

# グローバル変数 (setup() で初期化)
moisture = None


def setup():
    """起動時に一度だけ実行する初期化処理"""
    global moisture
    moisture = ADC(Pin(SIG_PIN))
    moisture.atten(ADC.ATTN_11DB)   # 入力レンジ 0-3.3V
    print("Grove Moisture Sensor 開始 (Ctrl-C で終了)")


def loop():
    """繰り返し実行する処理"""
    value = moisture.read_u16()      # 0-65535
    state = "WET" if value >= WET_LEVEL else "dry"
    print("moisture:", value, state)
    time.sleep(INTERVAL)


# --- エントリポイント ---------------------------------------------
setup()
try:
    while True:
        loop()
except KeyboardInterrupt:
    print("終了しました")
