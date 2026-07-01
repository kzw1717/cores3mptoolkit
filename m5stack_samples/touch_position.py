"""
CoreS3 内蔵 タッチパネル (FT6336U)  ── 入力サンプル
------------------------------------------------------
静電容量式タッチパネルに触れた座標 (x, y) を読み取り、
画面と PC のターミナルに表示します。配線は不要です（本体内蔵）。

対象 : M5Stack CoreS3 + UIFlow2 ファームウェア（M5 ライブラリ）
接続 : 不要（本体内蔵タッチパネル）
実行 : python -m mpremote run touch_position.py    （VSCode は Ctrl+Shift+B）
終了 : Ctrl-C（PC側ターミナルで送信）
参考 : https://uiflow-micropython.readthedocs.io/en/latest/hardware/touch.html
"""

import M5
from M5 import *
import time

# --- 設定 ---------------------------------------------------------
INTERVAL = 0.05       # loop() の実行間隔 [秒]

lbl = None


def setup():
    """起動時に一度だけ実行する初期化処理"""
    global lbl
    M5.begin()
    Widgets.fillScreen(0x222222)
    Widgets.Title("CoreS3 Touch", 3, 0xFFFFFF, 0x0000FF, Widgets.FONTS.DejaVu18)
    lbl = Widgets.Label("Touch the screen", 6, 60, 1.0, 0xFFFFFF, 0x222222, Widgets.FONTS.DejaVu18)
    print("Touch position started (Ctrl-C to stop)")


def loop():
    """繰り返し実行する処理"""
    M5.update()
    if M5.Touch.getCount():                  # タッチ点の数（0=触れていない）
        x = M5.Touch.getX()                  # X 座標 [px]
        y = M5.Touch.getY()                  # Y 座標 [px]
        lbl.setText("x: {}   y: {}".format(x, y))
        print("touch x={} y={}".format(x, y))
    time.sleep(INTERVAL)


# --- エントリポイント ---------------------------------------------
setup()
try:
    while True:
        loop()
except KeyboardInterrupt:
    print("stopped")
