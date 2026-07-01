"""
Grove - Moisture Sensor (SKU: 101020740)
----------------------------------------
土壌中の水分量をアナログ値で測定する土壌水分センサー。湿っているほど値が大きい。
※ キット付属Arduinoスケッチ（1_moisture_serial）を標準MicroPythonへ忠実移植。
   Arduino版は analogRead(A0) を 1 秒ごとに 1 回読み、"Moisture = 値" を表示するだけ。

対象   : M5Stack CoreS3 + UIFlow2 ファームウェア (MicroPython)
接続   : PORT.B  ( 黒=GND / 赤=5V / 黄=G9 / 白=G8 )  ※このモジュールは信号が G8 に出る
実行   : python -m mpremote run moisture_sensor.py
終了   : Ctrl-C (PC側ターミナルで送信)

メモ   : Arduino の analogRead は 0-1023（10bit）。MicroPython の read_u16() は 0-65535。
         値のスケールは異なるが、読み方・表示・周期はキットのスケッチと同一。
         Groveコネクタは信号線が2本（Port.BではG9とG8）あり、本センサはG8側で安定（実機確認）。
"""

from machine import Pin, ADC  # type: ignore
import time  # type: ignore

# --- 設定 ---------------------------------------------------------
SIG_PIN = 8          # PORT.B 信号ピン（実機確認: このモジュールは G8 側で安定）
INTERVAL = 1.0       # loop() の実行間隔 [秒]（Arduino の delay(1000) に相当）

moisture = ADC(Pin(SIG_PIN))
moisture.atten(ADC.ATTN_11DB)   # 0-3.3V を測れるようにする


def setup():
    print("Grove Moisture Sensor started (Ctrl-C to stop)")


def loop():
    sensor_value = moisture.read_u16()      # 生値を1回読む（analogRead 相当）
    print("Moisture =", sensor_value)
    time.sleep(INTERVAL)


setup()
try:
    while True:
        loop()
except KeyboardInterrupt:
    print("stopped")
