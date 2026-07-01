"""
Grove - Mini PIR Motion Sensor (SKU: 101020741)
-----------------------------------------------
焦電型赤外線で人や動物の動きを検知する小型PIRモーションセンサー。
※ キット付属Arduinoスケッチ（1_mini_pir_motion）を標準MicroPythonへ移植。

【この個体/モジュールの重要な実測ポイント】
  - 信号は「白線 = G8」に出る（黄線=G9 ではない）。
  - 内部プルアップが必須。プルアップ無し（素のIN）だと値が浮いてランダムに 0/1 する。
  - 極性：値=1(HIGH) のとき動きあり(detected)、値=0(LOW) のとき動きなし(no motion)。

対象   : M5Stack CoreS3 + UIFlow2 ファームウェア (MicroPython)
接続   : PORT.B  ( 黒=GND / 赤=5V / 黄=G9 / 白=G8 )  ※信号は 白線 = G8
実行   : python -m mpremote run pir_motion_sensor.py
終了   : Ctrl-C (PC側ターミナルで送信)

重要   : PIRは電源投入後 約30〜60秒 は出力が不安定。開始後しばらく動かず待つこと。
         向きで感度が変わるため、センサー面は動きを横切る向きに置くと安定（最適 約2m）。
"""

from machine import Pin  # type: ignore
import time  # type: ignore

# --- 設定 ---------------------------------------------------------
SIG_PIN = 8          # PORT.B 白線 (G8)  ※このモジュールは白線側に信号が出る
INTERVAL = 0.2       # loop() の実行間隔 [秒]

# 内部プルアップ付き入力（プルアップ無しだと値が浮くため必須）
pir = Pin(SIG_PIN, Pin.IN, Pin.PULL_UP)


def setup():
    print("Grove Mini PIR Motion Sensor started (Ctrl-C to stop)")
    print("(PIR is warming up ~30-60s: keep still at first)")


def loop():
    if pir.value() == 1:
        print("MOTION : detected")        # 値=1 で動きあり
    else:
        print("-      : no motion")        # 値=0 で動きなし
    time.sleep(INTERVAL)


setup()
try:
    while True:
        loop()
except KeyboardInterrupt:
    print("stopped")
