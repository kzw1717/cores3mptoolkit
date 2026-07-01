"""
CoreS3 内蔵 ディスプレイ (2.0" IPS 320x240)  ── 出力サンプル
------------------------------------------------------
画面にタイトル・文字・図形を表示し、カウンタを毎秒更新します。
Widgets（M5 ライブラリのUI部品）を使います。配線は不要です（本体内蔵）。

対象 : M5Stack CoreS3 + UIFlow2 ファームウェア（M5 ライブラリ）
接続 : 不要（本体内蔵ディスプレイ）
実行 : python -m mpremote run display_hello.py    （VSCode は Ctrl+Shift+B）
終了 : Ctrl-C（PC側ターミナルで送信）
参考 : https://uiflow-micropython.readthedocs.io/en/latest/widgets/index.html
"""

import M5  # type: ignore
from M5 import *  # type: ignore
import time  # type: ignore

# --- 設定 ---------------------------------------------------------
INTERVAL = 1.0        # カウンタ更新間隔 [秒]

lbl_count = None
count = 0


def setup():
    """起動時に一度だけ実行する初期化処理"""
    global lbl_count
    M5.begin()
    Widgets.fillScreen(0x000000)
    Widgets.Title("CoreS3 Display", 3, 0xFFFFFF, 0x0000FF, Widgets.FONTS.DejaVu18)
    # 文字（ラベル）
    Widgets.Label("Hello, M5Stack!", 10, 60, 1.0, 0xFFFF00, 0x000000, Widgets.FONTS.DejaVu24)
    # 図形（塗りつぶし円）: x, y, r, 線色, 塗り色
    Widgets.Circle(60, 170, 30, 0x00FF00, 0x00FF00)
    # 毎秒更新するカウンタ用ラベル
    lbl_count = Widgets.Label("count: 0", 120, 160, 1.0, 0xFFFFFF, 0x000000, Widgets.FONTS.DejaVu18)
    print("Displayed on screen (Ctrl-C to stop)")


def loop():
    """繰り返し実行する処理"""
    global count
    M5.update()
    count += 1
    lbl_count.setText("count: {}".format(count))   # 既存ラベルの文字を書き換え
    time.sleep(INTERVAL)


# --- エントリポイント ---------------------------------------------
setup()
try:
    while True:
        loop()
except KeyboardInterrupt:
    print("stopped")
