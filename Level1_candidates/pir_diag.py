"""
PIR 診断用スクリプト（Level1確定後に削除する一時ファイル）
------------------------------------------------------
Grove Mini PIR Motion Sensor の信号が G9 / G8 のどちらに、どんな値で来ているかを
0.5秒ごとに生表示して切り分ける。3パターンを同時に確認する:
  - G9(IN)           : プルなしで読んだ値
  - G8(IN)           : 配線が逆だった場合の確認
  - G9(PULL_DOWN)    : 出力がオープン系で浮いている場合の確認

実行 : python -m mpremote run pir_diag.py    終了 : Ctrl-C
使い方: 起動後30〜60秒は動かず待つ→その後センサー前で手を振り、値が 1 に変わるか観察する。
"""

from machine import Pin  # type: ignore
import time  # type: ignore

g9 = Pin(9, Pin.IN)
g8 = Pin(8, Pin.IN)
g9pd = Pin(9, Pin.IN, Pin.PULL_DOWN)


def setup():
    print("PIR diag started (Ctrl-C to stop)")


def loop():
    print("G9={} G8={} G9pd={}".format(g9.value(), g8.value(), g9pd.value()))
    time.sleep(0.5)


setup()
try:
    while True:
        loop()
except KeyboardInterrupt:
    print("stopped")
