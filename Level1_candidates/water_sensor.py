"""
Grove - Water Sensor (SKU: 101020733)
-------------------------------------
基板上の導電パターンで水の有無・水滴を検知するセンサー。
※ 本センサは 5V 動作前提で、乾燥時の信号が約5Vになる。CoreS3(3.3V)では信号がADC上限に
   張り付き、デジタル判定では常に HIGH のままになる。そのためアナログ値のわずかな低下を
   しきい値で拾う方式にしている。

対象   : M5Stack CoreS3 + UIFlow2 ファームウェア (MicroPython)
接続   : PORT.B  ( 黒=GND / 赤=5V / 黄=G9 / 白=G8 )  信号は 黄線 = G9 (ADC)
実行   : python -m mpremote run water_sensor.py
終了   : Ctrl-C (PC側ターミナルで送信)

校正   : 実測例 → 乾燥 ≒ 65535 / 十分な水 ≒ 60000（少量の水では約65157とわずかしか下がらない）。
         WET_THRESHOLD を乾燥値と「水あり値」の間に設定する（例では 64000）。個体・水質で変わるため実機で校正すること。
         ※ 5V動作センサのため変化幅が小さく、明確な水接触は検知できるが軽い湿りは拾いにくい。
"""

from machine import Pin, ADC  # type: ignore
import time  # type: ignore

# --- 設定 ---------------------------------------------------------
SIG_PIN = 9              # PORT.B 黄線 (G9)
INTERVAL = 0.5          # loop() の実行間隔 [秒]
WET_THRESHOLD = 64000   # この値より小さければ「水あり」と判定（要実機校正）

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
