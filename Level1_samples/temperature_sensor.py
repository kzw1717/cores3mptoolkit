"""
Grove - Temperature Sensor (SKU: 101020732)
-------------------------------------------
サーミスタで周囲温度を測るアナログ温度センサー。
※ キット付属Arduinoスケッチ（サーミスタ換算式）を標準MicroPythonへ移植。
   temperature = 1/(log(R/R0)/B + 1/298.15) - 273.15

対象   : M5Stack CoreS3 + UIFlow2 ファームウェア (MicroPython)
接続   : PORT.B  ( 黒=GND / 赤=5V / 黄=G9 / 白=G8 )  ※信号は G8
実行   : python -m mpremote run temperature_sensor.py
終了   : Ctrl-C (PC側ターミナルで送信)

注意   : B 定数・基準抵抗はキット付属Arduino資料の値（B=3975 / R0=10kΩ）。
         信号は G8 側（実機確認。G9では不安定だった）。
校正   : 本センサは電源5V動作だが CoreS3 の ADC 基準は約3.3V。キット式の (最大-a)/a 比は
         「ADC基準=電源電圧」前提でCoreS3では崩れるため、実電圧 v を求めて電源5Vを別扱いにする。
           v = raw/ADC_MAX * VREF                （ADCで測った実電圧）
           R = R0 * (VCC - v) / v                 （サーミスタ抵抗。Arduino式と同じ関係）
           temp = 1/(ln(R/R0)/B + 1/298.15) - 273.15
         VREF(ADC実効フルスケール≈3.3V)とVCC(5V)は実機で微調整可。表示が実温とずれる場合は
         VREF を優先的に、それでも合わなければ B / R0 を校正すること。
"""

from machine import Pin, ADC  # type: ignore
import math  # type: ignore
import time  # type: ignore

# --- 設定 ---------------------------------------------------------
SIG_PIN = 8          # PORT.B 信号ピン（実機確認: このモジュールは G8 側）
INTERVAL = 1.0       # loop() の実行間隔 [秒]
B = 3975             # サーミスタ B 定数
R0 = 10000           # 基準抵抗 [Ω]（25℃でのサーミスタ公称抵抗）
ADC_MAX = 65535      # read_u16() の最大値
VREF = 3.05          # ADC ATTN_11DB の実効フルスケール電圧 [V]（実機校正値。個体差で要微調整）
VCC = 5.0            # センサー電源電圧（Port.B 赤線）[V]

adc = ADC(Pin(SIG_PIN))
adc.atten(ADC.ATTN_11DB)   # 0-3.3V を測れるようにする


def setup():
    print("Grove Temperature Sensor started (Ctrl-C to stop)")


def loop():
    a = adc.read_u16()
    v = a / ADC_MAX * VREF                       # ADCで測った実電圧 [V]
    # 電圧が範囲外だと分圧計算が破綻するのでガード
    if v <= 0.0 or v >= VCC:
        print("raw:", a, " (out of range)")
        time.sleep(INTERVAL)
        return
    resistance = R0 * (VCC - v) / v              # サーミスタ抵抗値 [Ω]
    tempC = 1.0 / (math.log(resistance / R0) / B + 1.0 / 298.15) - 273.15
    print("raw:", a, " {:.2f}V  temp: {:.1f} C".format(v, tempC))
    time.sleep(INTERVAL)


setup()
try:
    while True:
        loop()
except KeyboardInterrupt:
    print("stopped")
