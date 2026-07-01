"""
CoreS3 タッチUI ── タッチ回数カウンタ サンプル（入力）
------------------------------------------------------
画面のどこでもタッチすると、タッチした回数を画面（英字）と
ターミナル（日本語）に表示します。

対象 : M5Stack CoreS3 + UIFlow2 ファームウェア（M5 ライブラリ / M5.Lcd 描画）
接続 : 不要（本体内蔵ディスプレイ＋タッチパネル）
実行 : python -m mpremote run touch_counter.py    （VSCode は Ctrl+Shift+B）
終了 : Ctrl-C（PC側ターミナルで送信）
参考 : Touch   https://uiflow-micropython.readthedocs.io/en/latest/hardware/touch.html

メモ : 内蔵フォントは日本語非対応のため画面は英字。日本語はターミナルに出します。
"""

import M5
import time

# --- 設定 ---------------------------------------------------------
touch_count = 0
prev_touching = False


def show_count():
    """カウント表示を描き直す"""
    M5.Lcd.fillRect(0, 90, 320, 60, 0x000000)
    M5.Lcd.setTextColor(0x00E5FF, 0x000000)
    M5.Lcd.setTextSize(3)
    M5.Lcd.setCursor(20, 100)
    M5.Lcd.print("Touched: {}".format(touch_count))


def on_touch():
    """画面がタッチされたときに実行する所定の関数"""
    global touch_count
    touch_count += 1
    show_count()
    print("Touched {} times".format(touch_count))


def setup():
    M5.begin()
    M5.Lcd.fillScreen(0x000000)
    M5.Lcd.setTextColor(0xFFFFFF, 0x000000)
    M5.Lcd.setTextSize(2)
    M5.Lcd.setCursor(10, 10)
    M5.Lcd.print("Tap anywhere on screen")
    show_count()
    print("Touch counter sample started (Ctrl-C to stop)")


def loop():
    global prev_touching
    M5.update()
    touching = M5.Touch.getCount() > 0
    if touching and not prev_touching:        # 触れた瞬間だけ1回カウント
        on_touch()
    prev_touching = touching
    time.sleep(0.02)


# --- エントリポイント ---------------------------------------------
setup()
try:
    while True:
        loop()
except KeyboardInterrupt:
    print("stopped")
