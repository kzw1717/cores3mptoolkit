"""
Grove - Moisture Sensor (SKU: 101020740)
----------------------------------------
土壌中の水分量をアナログ値で測定する土壌水分センサー。湿っているほど値が大きい。
※ 生値は元々ジッタが大きく単発読みでは値が上下するため、複数回サンプリングして
   平均化（ノイズ低減）し、しきい値で Dry / Moist / Wet を判別する方式にしている。

対象   : M5Stack CoreS3 + UIFlow2 ファームウェア (MicroPython)
接続   : PORT.B  ( 黒=GND / 赤=5V / 黄=G9 / 白=G8 )  信号は 黄線 = G9 (ADC1)
実行   : python -m mpremote run moisture_sensor.py
終了   : Ctrl-C (PC側ターミナルで送信)

校正   : しきい値 DRY_MAX / MOIST_MAX は 12bit(0-4095) 基準の目安。実際の土で値を見て
         校正すること（乾いた土・湿った土・水中でそれぞれ raw を確認して調整）。
"""

from machine import Pin, ADC  # type: ignore
import time  # type: ignore

# --- 設定 ---------------------------------------------------------
SIG_PIN = 9          # PORT.B 黄線 (G9 = ADC1)
INTERVAL = 1.0       # loop() の実行間隔 [秒]
SAMPLES = 10         # 1回の測定で平均するサンプル数（ノイズ低減）
DRY_MAX = 1000       # これ未満: 乾燥（要校正）
MOIST_MAX = 2500     # これ未満: 適湿 / 以上: 湿潤（要校正）

adc = ADC(Pin(SIG_PIN))
adc.atten(ADC.ATTN_11DB)     # 0-3.3V を測れるようにする
adc.width(ADC.WIDTH_12BIT)   # 0-4095 の分解能


def read_moisture(samples=SAMPLES):
    """複数回サンプリングして平均化。raw値(0-4095)と概算電圧(V)を返す"""
    total = 0
    for _ in range(samples):
        total += adc.read()          # 0-4095
        time.sleep_ms(5)
    raw = total // samples
    voltage = raw / 4095 * 3.3
    return raw, voltage


def classify(raw):
    """raw を Dry / Moist / Wet に分類"""
    if raw < DRY_MAX:
        return "DRY"
    elif raw < MOIST_MAX:
        return "MOIST"
    else:
        return "WET"


def setup():
    print("Grove Moisture Sensor started (Ctrl-C to stop)")


def loop():
    raw, v = read_moisture()
    print("raw={:4d}  {:.2f}V  -> {}".format(raw, v, classify(raw)))
    time.sleep(INTERVAL)


setup()
try:
    while True:
        loop()
except KeyboardInterrupt:
    print("stopped")
