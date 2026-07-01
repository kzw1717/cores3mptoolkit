"""
Grove - Mini PIR Motion Sensor (SKU: 101020741)
-----------------------------------------------
焦電型赤外線で人や動物の動きを検知する小型PIRモーションセンサー。
動きを検知すると信号が HIGH になる。
※ キット付属Arduinoスケッチ（1_mini_pir_motion）を標準MicroPythonへ移植。
   公式スケッチは毎回 "Hi, people is coming"(動きあり) / "Watching"(動きなし) を表示する。
   本サンプルは状態が変化した瞬間だけ表示し、検知/解除のタイミングを分かりやすくしている。

対象   : M5Stack CoreS3 + UIFlow2 ファームウェア (MicroPython)
接続   : PORT.B  ( 黒=GND / 赤=5V / 黄=G9 / 白=G8 )  信号は 黄線 = G9
実行   : python -m mpremote run pir_motion_sensor.py
終了   : Ctrl-C (PC側ターミナルで送信)

重要   : PIRは電源投入後 約30〜60秒 は出力が不安定（HIGHに張り付く）。この間の連続検知は
         ウォームアップで正常。開始後しばらく動かず待ってから試すこと。
         また向きで感度が変わるため、センサー面は水平に置くと安定する（キットTips）。
"""

from machine import Pin  # type: ignore
import time  # type: ignore

# --- 設定 ---------------------------------------------------------
SIG_PIN = 9          # PORT.B 黄線 (G9)
INTERVAL = 0.1       # loop() の実行間隔 [秒]

pir = Pin(SIG_PIN, Pin.IN)
prev_state = 0       # 前回の状態（0=動きなし / 1=動きあり）


def setup():
    print("Grove Mini PIR Motion Sensor started (Ctrl-C to stop)")
    print("(PIR is warming up ~30-60s: keep still at first)")


def loop():
    global prev_state
    state = pir.value()
    if state == 1 and prev_state == 0:
        print("MOTION : detected")        # 立ち上がり（動きを検知した瞬間）
    elif state == 0 and prev_state == 1:
        print("-      : no motion")        # 立ち下がり（検知が解除された瞬間）
    prev_state = state
    time.sleep(INTERVAL)


setup()
try:
    while True:
        loop()
except KeyboardInterrupt:
    print("stopped")
