"""
Grove - Sound Sensor (SKU: 101020735)
-------------------------------------
周囲の音の大きさを検出する音量センサー（マイク＋アンプ）。
出力は音の波形（交流）なので、短時間に高速サンプリングして「最大値−最小値（振幅）」を
音量の目安として求める。
※ 平均だけでは交流波形の平均＝ほぼ一定値になり音量を反映しないため、振幅方式に変更している
   （キット付属Arduinoスケッチの平均法を CoreS3 向けに改良）。

対象   : M5Stack CoreS3 + UIFlow2 ファームウェア (MicroPython)
接続   : PORT.B  ( 黒=GND / 赤=5V / 黄=G9 / 白=G8 )  信号は 黄線 = G9 (ADC)
実行   : python -m mpremote run sound_sensor.py
終了   : Ctrl-C (PC側ターミナルで送信)

見方   : 無音では小さい値、声や拍手で大きい値になる。閾値で「音あり」を判定してもよい。
"""

from machine import Pin, ADC  # type: ignore
import time  # type: ignore

# --- 設定 ---------------------------------------------------------
SIG_PIN = 9          # PORT.B 黄線 (G9)
INTERVAL = 0.1       # loop() の実行間隔 [秒]
WINDOW = 500         # 1回の測定で高速サンプリングする回数（音の波形をとらえる窓）

adc = ADC(Pin(SIG_PIN))
adc.atten(ADC.ATTN_11DB)   # 0-3.3V を測れるようにする


def setup():
    print("Grove Sound Sensor started (Ctrl-C to stop)")


def loop():
    lo = 65535
    hi = 0
    for i in range(WINDOW):        # 窓の中を高速に読み、最小と最大を記録
        v = adc.read_u16()
        if v < lo:
            lo = v
        if v > hi:
            hi = v
    level = hi - lo                # 振幅（最大−最小）＝音量の目安
    print("sound:", level)
    time.sleep(INTERVAL)


setup()
try:
    while True:
        loop()
except KeyboardInterrupt:
    print("stopped")
