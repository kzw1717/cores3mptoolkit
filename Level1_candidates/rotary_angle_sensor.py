"""
Grove - Rotary Angle Sensor (SKU: 101020734)
--------------------------------------------
つまみを回すと回転角をアナログ値として出力する可変抵抗（10kΩ・可動域300度）。
※ キット付属Arduinoスケッチ（analogRead → 角度換算）を標準MicroPythonへ移植。

対象   : M5Stack CoreS3 + UIFlow2 ファームウェア (MicroPython)
接続   : PORT.B  ( 黒=GND / 赤=5V / 黄=G9 / 白=G8 )  信号は 黄線 = G9
実行   : python -m mpremote run rotary_angle_sensor.py
終了   : Ctrl-C (PC側ターミナルで送信)
"""

from machine import Pin, ADC  # type: ignore
import time  # type: ignore

# --- 設定 ---------------------------------------------------------
SIG_PIN = 9          # PORT.B 黄線 (G9)
INTERVAL = 0.2       # loop() の実行間隔 [秒]
FULL_ANGLE = 300     # 可動域 [度]
ADC_MAX = 65535      # read_u16() の最大値

adc = ADC(Pin(SIG_PIN))
adc.atten(ADC.ATTN_11DB)   # 0-3.3V を測れるようにする


def setup():
    print("Grove Rotary Angle Sensor started (Ctrl-C to stop)")


def loop():
    value = adc.read_u16()                     # 0-65535
    degrees = value * FULL_ANGLE / ADC_MAX     # 0-300度へ換算
    print("raw:", value, " angle: {:.0f} deg".format(degrees))
    time.sleep(INTERVAL)


setup()
try:
    while True:
        loop()
except KeyboardInterrupt:
    print("stopped")
