"""
CoreS3 内蔵 ディスプレイ ── 画像(PNG)表示サンプル（出力）
------------------------------------------------------
あらかじめ本体に転送しておいた PNG 画像を画面に表示します。
画像は PC から mpremote で本体へコピーしておきます（解説ページ参照）。

対象 : M5Stack CoreS3 + UIFlow2 ファームウェア（M5 ライブラリ）
接続 : 不要（本体内蔵ディスプレイ）
準備 : 画像を本体へ転送 →  python -m mpremote cp sample.png :
実行 : mpremote run display_image.py    （VSCode は Ctrl+Shift+B）
終了 : Ctrl-C（PC側ターミナルで送信）
参考 : https://uiflow-micropython.readthedocs.io/en/latest/widgets/image.html

画像の条件（重要）:
- 形式 : PNG（BMP / JPG も可）
- サイズ : 画面は 320 x 240 px。全画面なら 320x240 以内で用意する
- 置き場所 : 本体のルート（mpremote cp で送った先）。下の IMAGE_PATH に合わせる
"""

import M5
from M5 import *
import time

# --- 設定 ---------------------------------------------------------
IMAGE_PATH = "sample.png"   # 本体へ転送した画像のパス（見つからない場合は "/flash/sample.png" を試す）
POS_X = 0                   # 表示開始 X 座標
POS_Y = 0                   # 表示開始 Y 座標


def setup():
    """起動時に一度だけ実行する初期化処理"""
    M5.begin()
    Widgets.fillScreen(0x000000)
    # 画像を読み込んで (POS_X, POS_Y) に表示する
    Widgets.Image(IMAGE_PATH, POS_X, POS_Y)
    print("画像を表示しました: {} (Ctrl-C で終了)".format(IMAGE_PATH))


def loop():
    """繰り返し実行する処理（表示を保持するだけ）"""
    M5.update()
    time.sleep(0.5)


# --- エントリポイント ---------------------------------------------
setup()
try:
    while True:
        loop()
except KeyboardInterrupt:
    print("終了しました")
