"""
Grove - Water Sensor (SKU: 101020733)
-------------------------------------
基板上の導電パターンで水の有無・水滴を検知するセンサー。
※ 本センサは 5V 動作前提で、乾燥時の信号が約5Vになる。CoreS3(3.3V)では信号がADC上限に
   張り付き、デジタル判定では常に HIGH のままになる。そのためアナログ値のわずかな低下を
   しきい値で拾う方式にしている。

対象   : M5Stack CoreS3 + UIFlow2 ファームウェア (MicroPython)
接続   : PORT.B  ( 黒=GND / 赤=5V / 黄=G9 / 白=G8 )  ※G8の方が感度が良い（実機確認）
実行   : python -m mpremote run water_sensor.py
終了   : Ctrl-C (PC側ターミナルで送信)

校正   : アナログ値の低下をしきい値で拾う。乾燥で最大付近、水ありで低下する。
         G8実測 → 無水 ≒ 65535 / 水につけた時 ≒ 54000（G9より変化幅が大きく感度良好）。
         WET_THRESHOLD は無水値と有水値の中間(=60000)に設定。個体・水質・ピンで変わるため
         実機で再校正すること。
メモ   : Groveコネクタは信号線が2本（Port.BではG9とG8）あり、どちらを使うかはモジュール依存。
         本センサはG8側の方が感度が良かった（実機確認）。
"""

from machine import Pin, ADC  # type: ignore
import time  # type: ignore

# --- 設定 ---------------------------------------------------------
SIG_PIN = 8              # PORT.B 信号ピン（実機確認: G8の方が感度良好）
INTERVAL = 0.5          # loop() の実行間隔 [秒]
WET_THRESHOLD = 60000   # この値より小さければ「水あり」と判定（G8実測: 無水65535/有水54000の中間）

adc = ADC(Pin(SIG_PIN))
adc.atten(ADC.ATTN_11DB)   # 0-3.3V を測れるようにする


def setup():
    print("Grove Water Sensor started (Ctrl-C to stop)")


def loop():
    value = adc.read_u16()          # 0-65535（乾燥で最大付近、水ありで少し低下）
    if value < WET_THRESHOLD:
        print("water:", value, "(WET)")
    else:
        print("water:", value, "(dry)")
    time.sleep(INTERVAL)


setup()
try:
    while True:
        loop()
except KeyboardInterrupt:
    print("stopped")
