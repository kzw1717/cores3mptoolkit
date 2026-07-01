"""
Grove - Water Sensor 診断用スクリプト（原因切り分け）
------------------------------------------------------
同じ G9 を「アナログ」「デジタル(プルアップ無し)」「デジタル(プルアップ有り)」の
3通りで読み、乾いた状態と水につけた状態で値を比較します。

対象   : M5Stack CoreS3 + UIFlow2 ファームウェア (MicroPython)
接続   : PORT.B  ( 黒=GND / 赤=5V / 黄=G9 / 白=G8 )  信号は 黄線 = G9
実行   : python -m mpremote run water_sensor_diag.py
終了   : Ctrl-C (PC側ターミナルで送信)

使い方 :
  1) 乾いた状態で数秒間、表示される3値を記録。
  2) 電極を水道水につけて、3値がどう変わるかを記録。
  3) 変化した読み方（analog / no-pull / pull-up）で本番方式を決める。
"""

from machine import Pin, ADC  # type: ignore
import time  # type: ignore

SIG_PIN = 9          # PORT.B 黄線 (G9)
INTERVAL = 0.3


def read_all():
    # アナログ
    adc = ADC(Pin(SIG_PIN))
    adc.atten(ADC.ATTN_11DB)          # 0-3.3V
    a = adc.read_u16()                # 0-65535
    # デジタル（プルアップ無し）
    dnp = Pin(SIG_PIN, Pin.IN).value()
    # デジタル（プルアップ有り＝現状と同じ）
    dpu = Pin(SIG_PIN, Pin.IN, Pin.PULL_UP).value()
    return a, dnp, dpu


print("Water Sensor DIAG (Ctrl-C to stop). Compare DRY vs WET.")
try:
    while True:
        a, dnp, dpu = read_all()
        print("analog:", a, " digital(no-pull):", dnp, " digital(pull-up):", dpu)
        time.sleep(INTERVAL)
except KeyboardInterrupt:
    print("stopped")
