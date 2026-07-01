"""
Grove - Temperature Sensor (SKU: 101020732)
-------------------------------------------
サーミスタで周囲温度を測るアナログ温度センサー。
※ キット付属Arduinoスケッチ（サーミスタ換算式）を標準MicroPythonへ移植。
   temperature = 1/(log(R/R0)/B + 1/298.15) - 273.15

対象   : M5Stack CoreS3 + UIFlow2 ファームウェア (MicroPython)
接続   : PORT.B  ( 黒=GND / 赤=5V / 黄=G9 / 白=G8 )  信号は 黄線 = G9
実行   : python -m mpremote run temperature_sensor.py
終了   : Ctrl-C (PC側ターミナルで送信)

注意   : B 定数・基準抵抗はキット付属Arduino資料の値（B=3975 / R0=10kΩ）。
         実機の表示がずれる場合は下の B / R0 を実測で校正してください。
"""

from machine import Pin, ADC  # type: ignore
import math  # type: ignore
import time  # type: ignore

# --- 設定 ---------------------------------------------------------
SIG_PIN = 9          # PORT.B 黄線 (G9)
INTERVAL = 1.0       # loop() の実行間隔 [秒]
B = 3975             # サーミスタ B 定数
R0 = 10000           # 基準抵抗 [Ω]
ADC_MAX = 65535      # read_u16() の最大値

adc = ADC(Pin(SIG_PIN))
adc.atten(ADC.ATTN_11DB)   # 0-3.3V を測れるようにする


def setup():
    print("Grove Temperature Sensor started (Ctrl-C to stop)")


def loop():
    a = adc.read_u16()
    # 5V動作センサのため、CoreS3(3.3V)ではADCが上限(65535付近)に張り付くことがある。
    # そのとき resistance=0 → log(0) で math domain error になるためガードする。
    if a <= 1 or a >= ADC_MAX - 1:
        print("raw:", a, " (out of range: 5V sensor saturates CoreS3 3.3V ADC)")
        time.sleep(INTERVAL)
        return
    resistance = (ADC_MAX - a) * R0 / a         # サーミスタ抵抗値
    tempC = 1.0 / (math.log(resistance / R0) / B + 1.0 / 298.15) - 273.15
    print("raw:", a, " temp: {:.1f} C".format(tempC))
    time.sleep(INTERVAL)


setup()
try:
    while True:
        loop()
except KeyboardInterrupt:
    print("stopped")
