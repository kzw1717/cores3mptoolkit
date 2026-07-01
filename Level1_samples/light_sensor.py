"""
Grove - Light Sensor v1.2 (SKU: 101020736)
------------------------------------------
フォトトランジスタで周囲の明るさをアナログ値で測定する照度センサー。
明るいほど値が大きくなります。

対象   : M5Stack CoreS3 + UIFlow2 ファームウェア (MicroPython)
接続   : PORT.B  ( 黒=GND / 赤=5V / 黄=G9 / 白=G8 )  ※このモジュールは信号が G8 に出る
実行   : python -m mpremote run light_sensor.py
終了   : Ctrl-C (PC側ターミナルで送信)

メモ   : Groveコネクタは信号線が2本（Port.BではG9とG8）あり、どちらを使うかはモジュール依存。
         本センサはG8側に信号が出た（実機確認）。G9では明暗に反応しない。
"""

from machine import Pin, ADC  # type: ignore
import time  # type: ignore

# --- 設定 ---------------------------------------------------------
SIG_PIN = 8          # PORT.B 信号ピン（実機確認: このモジュールは G8 側）
INTERVAL = 0.2       # loop() の実行間隔 [秒]

# グローバル変数 (setup() で初期化)
light = None


def setup():
    """起動時に一度だけ実行する初期化処理"""
    global light
    light = ADC(Pin(SIG_PIN))
    light.atten(ADC.ATTN_11DB)   # 入力レンジ 0-3.3V
    print("Grove Light Sensor started (Ctrl-C to stop)")


def loop():
    """繰り返し実行する処理"""
    value = light.read_u16()     # 0-65535
    print("light:", value)
    time.sleep(INTERVAL)


# --- エントリポイント ---------------------------------------------
setup()
try:
    while True:
        loop()
except KeyboardInterrupt:
    print("stopped")
