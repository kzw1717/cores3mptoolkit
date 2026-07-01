"""
PIR 診断用スクリプト v2（Level1確定後に削除する一時ファイル）
------------------------------------------------------
G9・G8 を「両方とも素の入力（プルなし）」で読み、どちらが動きに反応するかを切り分ける。
※ v1 はピン9にプルダウンを重ねて設定してしまい G9 の読みを汚していたので修正版。

実行 : python -m mpremote run pir_diag.py    終了 : Ctrl-C
テスト手順（値と動きを対応づけるために決まったパターンで動く）:
  1. 起動後90秒は動かず待つ（PIRウォームアップ）
  2. センサー前で手を3秒振る → 5秒じっとする、を数回くり返す
  3. 手を振っているときに 0→1 に変わるピンが本物の信号
"""

from machine import Pin  # type: ignore
import time  # type: ignore

g9 = Pin(9, Pin.IN)      # PORT.B 黄線
g8 = Pin(8, Pin.IN)      # PORT.B 白線


def setup():
    print("PIR diag v2 started (Ctrl-C to stop)")


def loop():
    print("G9={}  G8={}".format(g9.value(), g8.value()))
    time.sleep(0.5)


setup()
try:
    while True:
        loop()
except KeyboardInterrupt:
    print("stopped")
