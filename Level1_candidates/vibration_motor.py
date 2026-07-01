"""
Grove - Vibration Motor (SKU: 108020121)
----------------------------------------
デジタル信号で振動する小型バイブレーションモーター（HIGHで振動 / LOWで停止）。
※ キット付属Arduinoスケッチ（digitalWrite HIGH/LOW）を標準MicroPythonへ移植。

対象   : M5Stack CoreS3 + UIFlow2 ファームウェア (MicroPython)
接続   : PORT.B  ( 黒=GND / 赤=5V / 黄=G9 / 白=G8 )  ※このモジュールは制御信号が G8 に出る
実行   : python -m mpremote run vibration_motor.py
終了   : Ctrl-C (PC側ターミナルで送信)

停止   : ★出力（アクチュエータ）系の注意★ Ctrl-Cだけでは止まらないことがある。
         `mpremote run` のCtrl-CはPC側mpremoteが終了するだけで、デバイス上のloop()は動き続け、
         GPIOも最後の状態を保持するため、モーターが振動し続けることがある。
         確実に止めるには CoreS3 本体のリセットボタン、または別ターミナルで
         `python -m mpremote reset`（ソフトリセット）を実行する。USB抜き差しでも停止。

メモ   : Groveコネクタは信号線が2本（Port.BではG9とG8）あり、どちらを使うかはモジュール依存。
         本モジュールはG8側で制御（実機確認前提。G9で動かない場合はここが原因）。
"""

from machine import Pin  # type: ignore
import time  # type: ignore

# --- 設定 ---------------------------------------------------------
SIG_PIN = 8          # PORT.B 信号ピン（G8）
INTERVAL = 1.0       # 振動/停止の間隔 [秒]

motor = Pin(SIG_PIN, Pin.OUT)


def setup():
    print("Grove Vibration Motor started (Ctrl-C to stop)")


def loop():
    motor.value(1)            # 振動
    print("VIB : vibrating")
    time.sleep(INTERVAL)
    motor.value(0)            # 停止
    print("--- : stopped")
    time.sleep(INTERVAL)


setup()
try:
    while True:
        loop()
except KeyboardInterrupt:
    motor.value(0)            # 終了時は停止
    print("stopped")
