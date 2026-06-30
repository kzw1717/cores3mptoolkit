"""
CoreS3 内蔵 ディスプレイ ── 文字表示のみ サンプル（出力）
------------------------------------------------------
画面に文字だけを表示します（display_hello.py の「文字」部分を独立させたもの）。
文字サイズ・色・表示位置の変え方を示します。

対象 : M5Stack CoreS3 + UIFlow2 ファームウェア（M5 ライブラリ / M5.Lcd 描画）
接続 : 不要（本体内蔵ディスプレイ）
実行 : mpremote run display_hello_text.py    （VSCode は Ctrl+Shift+B）
終了 : Ctrl-C（PC側ターミナルで送信）
参考 : https://uiflow-micropython.readthedocs.io/en/latest/widgets/index.html

メモ : 内蔵フォントは日本語非対応のため、画面は英字で表示します。
"""

import M5
import time


def setup():
    M5.begin()
    M5.Lcd.fillScreen(0x000000)

    # タイトル（大きい文字）
    M5.Lcd.setTextColor(0xFFFF00, 0x000000)   # 文字色, 背景色
    M5.Lcd.setTextSize(3)                      # 文字サイズ（倍率）
    M5.Lcd.setCursor(10, 10)                   # 表示開始位置 (x, y)
    M5.Lcd.print("Hello, M5Stack!")

    # 通常サイズの文字（色違い）
    M5.Lcd.setTextSize(2)
    M5.Lcd.setTextColor(0xFFFFFF, 0x000000)
    M5.Lcd.setCursor(10, 70)
    M5.Lcd.print("CoreS3 Display")

    M5.Lcd.setTextColor(0x00FF00, 0x000000)
    M5.Lcd.setCursor(10, 105)
    M5.Lcd.print("Text only sample")

    # 数値を文字に埋め込む例
    M5.Lcd.setTextColor(0x00E5FF, 0x000000)
    M5.Lcd.setCursor(10, 150)
    M5.Lcd.print("value = {}".format(123))

    print("文字表示サンプル (Ctrl-C で終了)")


def loop():
    M5.update()
    time.sleep(0.5)


# --- エントリポイント ---------------------------------------------
setup()
try:
    while True:
        loop()
except KeyboardInterrupt:
    print("終了しました")
