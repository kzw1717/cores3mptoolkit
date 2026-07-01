"""
PIR 診断用スクリプト v3（Level1確定後に削除する一時ファイル）
------------------------------------------------------
プル抵抗を入れて「浮きノイズ」を消し、本物の駆動信号だけを見分ける。
このv3は G9・G8 を両方 PULL_DOWN で読む（プッシュプル出力なら静止=0/動き=1になるはず）。
※ もしこれで動きに追従しなければ、次は PULL_UP 版（下のMODEを"up"に変更）で試す。
   オープンドレイン出力なら PULL_UP で 静止=1 / 動き=0 になる。

実行 : python -m mpremote run pir_diag.py    終了 : Ctrl-C
テスト: 起動後60秒静止 → 15秒じっと静止（理想は値が一定）→ 1〜2m離れて正面を横切って歩く
        → 歩いたときだけ値が変わるピンが本物の信号。
"""

from machine import Pin  # type: ignore
import time  # type: ignore

MODE = "down"    # "down"=PULL_DOWN / "up"=PULL_UP  （まず down、駄目なら up に変えて再実行）

pull = Pin.PULL_DOWN if MODE == "down" else Pin.PULL_UP
g9 = Pin(9, Pin.IN, pull)     # PORT.B 黄線
g8 = Pin(8, Pin.IN, pull)     # PORT.B 白線


def setup():
    print("PIR diag v3 started  MODE={} (Ctrl-C to stop)".format(MODE))


def loop():
    print("G9={}  G8={}".format(g9.value(), g8.value()))
    time.sleep(0.5)


setup()
try:
    while True:
        loop()
except KeyboardInterrupt:
    print("stopped")
