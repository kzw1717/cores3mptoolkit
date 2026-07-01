"""
CoreS3 タッチUI ── 1ボタン サンプル（入力）
------------------------------------------------------
画面に1つのボタンを表示し、タッチしたら所定の関数 on_button_pressed() を実行します。
例として「押された回数」を画面（英字）とターミナル（日本語）に表示します。

対象 : M5Stack CoreS3 + UIFlow2 ファームウェア（M5 ライブラリ / M5.Lcd 描画）
接続 : 不要（本体内蔵ディスプレイ＋タッチパネル）
実行 : python -m mpremote run touch_button_single.py    （VSCode は Ctrl+Shift+B）
終了 : Ctrl-C（PC側ターミナルで送信）
参考 : Touch   https://uiflow-micropython.readthedocs.io/en/latest/hardware/touch.html
       Display https://uiflow-micropython.readthedocs.io/en/latest/widgets/index.html

メモ : 内蔵フォントは日本語を含まないため、画面表示は英字にしています。
       日本語はターミナル（print）に出します。
"""

import M5
import time

# --- 設定 ---------------------------------------------------------
BTN = (90, 90, 140, 60)    # ボタン領域 (x, y, w, h)

press_count = 0
prev_touching = False


def in_rect(px, py, rect):
    """点 (px, py) が矩形 rect 内かどうか"""
    x, y, w, h = rect
    return x <= px <= x + w and y <= py <= y + h


def draw_button():
    x, y, w, h = BTN
    M5.Lcd.fillRect(x, y, w, h, 0x1E88E5)         # ボタン本体
    M5.Lcd.drawRect(x, y, w, h, 0xFFFFFF)         # 枠線
    M5.Lcd.setTextColor(0xFFFFFF, 0x1E88E5)
    M5.Lcd.setTextSize(3)
    M5.Lcd.setCursor(x + 24, y + 16)
    M5.Lcd.print("PUSH")


def show_status():
    """ステータス表示領域をクリアしてから描き直す"""
    M5.Lcd.fillRect(0, 180, 320, 40, 0x000000)
    M5.Lcd.setTextColor(0xFFFFFF, 0x000000)
    M5.Lcd.setTextSize(2)
    M5.Lcd.setCursor(10, 190)
    M5.Lcd.print("Pushed: {} times".format(press_count))


def on_button_pressed():
    """ボタンが押されたときに実行する所定の関数"""
    global press_count
    press_count += 1
    show_status()
    print("Button pressed {} times".format(press_count))


def setup():
    M5.begin()
    M5.Lcd.fillScreen(0x000000)
    M5.Lcd.setTextColor(0xFFFFFF, 0x000000)
    M5.Lcd.setTextSize(2)
    M5.Lcd.setCursor(10, 10)
    M5.Lcd.print("Touch the button")
    draw_button()
    show_status()
    print("1-button sample started (Ctrl-C to stop)")


def loop():
    global prev_touching
    M5.update()
    touching = M5.Touch.getCount() > 0
    if touching and not prev_touching:        # 触れた瞬間だけ反応（押しっぱなし防止）
        if in_rect(M5.Touch.getX(), M5.Touch.getY(), BTN):
            on_button_pressed()
    prev_touching = touching
    time.sleep(0.02)


# --- エントリポイント ---------------------------------------------
setup()
try:
    while True:
        loop()
except KeyboardInterrupt:
    print("stopped")
