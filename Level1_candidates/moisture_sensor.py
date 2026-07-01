"""
Grove - Moisture Sensor (SKU: 101020740)
----------------------------------------
土壌中の水分量をアナログ値で測定する土壌水分センサー。湿っているほど値が大きい。
※ キット付属Arduinoスケッチ（analogRead の生値を表示）を標準MicroPythonへ移植。

対象   : M5Stack CoreS3 + UIFlow2 ファームウェア (MicroPython)
接続   : PORT.B  ( 黒=GND / 赤=5V / 黄=G9 / 白=G8 )  信号は 黄線 = G9 (ADC)
実行   : mpremote run moisture_sensor.py
終了   : Ctrl-C (PC側ターミナルで送信)
"""

from machine import Pin, ADC
import time

# --- 設定 ---------------------------------------------------------
SIG_PIN = 9          # PORT.B 黄線 (G9)
INTERVAL = 0.5       # loop() の実行間隔 [秒]

moisture = ADC(Pin(SIG_PIN))
moisture.atten(ADC.ATTN_11DB)   # 0-3.3V を測れるようにする


def setup():
    print("Grove Moisture Sensor 開始 (Ctrl-C で終了)")


def loop():
    value = moisture.read_u16()      # 0-65535（Arduino の analogRead に相当）
    print("moisture:", value)
    # しきい値で乾湿を判定したい場合は、例えば value >= 30000 で「湿っている」など
    # （しきい値は実機で校正してください）。
    time.sleep(INTERVAL)


setup()
try:
    while True:
        loop()
except KeyboardInterrupt:
    print("終了しました")
