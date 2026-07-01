"""
Grove - Sound Sensor (SKU: 101020735)
-------------------------------------
周囲の音の大きさをアナログ電圧で出力する音量センサー。
※ キット付属Arduinoスケッチ（32回サンプルして平均）を標準MicroPythonへ移植。

対象   : M5Stack CoreS3 + UIFlow2 ファームウェア (MicroPython)
接続   : PORT.B  ( 黒=GND / 赤=5V / 黄=G9 / 白=G8 )  信号は 黄線 = G9
実行   : mpremote run sound_sensor.py
終了   : Ctrl-C (PC側ターミナルで送信)
"""

from machine import Pin, ADC
import time

# --- 設定 ---------------------------------------------------------
SIG_PIN = 9          # PORT.B 黄線 (G9)
INTERVAL = 0.1       # loop() の実行間隔 [秒]
SAMPLES = 32         # 平均するサンプル数（値を安定させる）

adc = ADC(Pin(SIG_PIN))
adc.atten(ADC.ATTN_11DB)   # 0-3.3V を測れるようにする


def setup():
    print("Grove Sound Sensor 開始 (Ctrl-C で終了)")


def loop():
    total = 0
    for i in range(SAMPLES):        # 32回読み取って合計
        total += adc.read_u16()
    level = total // SAMPLES        # 平均
    print("sound:", level)
    time.sleep(INTERVAL)


setup()
try:
    while True:
        loop()
except KeyboardInterrupt:
    print("終了しました")
