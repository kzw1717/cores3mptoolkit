"""
Grove - Touch Sensor (SKU: 101020746)
-------------------------------------
静電容量式で指のタッチ（近接）を検知するタッチセンサー。指がパッドに触れる／近づくと
信号が HIGH になる。押し込む必要がなく、触れるだけ・近づけるだけで反応する。
※ キット付属Arduinoスケッチ（Grove_Touch_Sensor）を標準MicroPythonへ移植。
   公式スケッチは digitalRead が 1 のとき LED を点灯する例。ここでは入力サンプルとして
   タッチの有無をターミナルに表示する。

対象   : M5Stack CoreS3 + UIFlow2 ファームウェア (MicroPython)
接続   : PORT.B  ( 黒=GND / 赤=5V / 黄=G9 / 白=G8 )  信号は 黄線 = G9
実行   : python -m mpremote run touch_sensor.py
終了   : Ctrl-C (PC側ターミナルで送信)
"""

from machine import Pin  # type: ignore
import time  # type: ignore

# --- 設定 ---------------------------------------------------------
SIG_PIN = 9          # PORT.B 黄線 (G9)
INTERVAL = 0.2       # loop() の実行間隔 [秒]

touch = Pin(SIG_PIN, Pin.IN)


def setup():
    print("Grove Touch Sensor started (Ctrl-C to stop)")


def loop():
    if touch.value() == 1:
        print("TOUCH : touched")        # 値=1 でタッチあり
    else:
        print("-     : no touch")        # 値=0 でタッチなし
    time.sleep(INTERVAL)


setup()
try:
    while True:
        loop()
except KeyboardInterrupt:
    print("stopped")
