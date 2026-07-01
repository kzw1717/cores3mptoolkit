"""
CoreS3 タッチUI ── YES / NO 2ボタン サンプル（入力）
------------------------------------------------------
画面に [YES] [NO] の2つのボタンを表示し、それぞれ所定の関数 on_yes() / on_no() を実行します。
押した回数を画面（英字）とターミナル（日本語）に表示します。

対象 : M5Stack CoreS3 + UIFlow2 ファームウェア（M5 ライブラリ / M5.Lcd 描画）
接続 : 不要（本体内蔵ディスプレイ＋タッチパネル）
実行 : python -m mpremote run touch_button_yesno.py    （VSCode は Ctrl+Shift+B）
終了 : Ctrl-C（PC側ターミナルで送信）
参考 : Touch   https://uiflow-micropython.readthedocs.io/en/latest/hardware/touch.html

メモ : 内蔵フォントは日本語非対応のため画面は英字。日本語はターミナルに出します。
"""

import M5
import time

# --- 設定 ---------------------------------------------------------
YES_BTN = (30, 80, 110, 80)    # (x, y, w, h)
NO_BTN = (180, 80, 110, 80)

yes_count = 0
no_count = 0
prev_touching = False


def in_rect(px, py, rect):
    x, y, w, h = rect
    return x <= px <= x + w and y <= py <= y + h


def draw_button(rect, label, fill):
    x, y, w, h = rect
    M5.Lcd.fillRect(x, y, w, h, fill)
    M5.Lcd.drawRect(x, y, w, h, 0xFFFFFF)
    M5.Lcd.setTextColor(0xFFFFFF, fill)
    M5.Lcd.setTextSize(3)
    M5.Lcd.setCursor(x + 24, y + 26)
    M5.Lcd.print(label)


def show_status():
    M5.Lcd.fillRect(0, 185, 320, 40, 0x000000)
    M5.Lcd.setTextColor(0xFFFFFF, 0x000000)
    M5.Lcd.setTextSize(2)
    M5.Lcd.setCursor(10, 195)
    M5.Lcd.print("YES: {}   NO: {}".format(yes_count, no_count))


def on_yes():
    """YES を押したときに実行する所定の関数"""
    global yes_count
    yes_count += 1
    show_status()
    print("yes -> {} times".format(yes_count))


def on_no():
    """NO を押したときに実行する所定の関数"""
    global no_count
    no_count += 1
    show_status()
    print("no -> {} times".format(no_count))


def setup():
    M5.begin()
    M5.Lcd.fillScreen(0x000000)
    M5.Lcd.setTextColor(0xFFFFFF, 0x000000)
    M5.Lcd.setTextSize(2)
    M5.Lcd.setCursor(10, 10)
    M5.Lcd.print("Choose YES or NO")
    draw_button(YES_BTN, "YES", 0x2E7D32)    # 緑
    draw_button(NO_BTN, "NO", 0xC62828)      # 赤
    show_status()
    print("YES/NO sample started (Ctrl-C to stop)")


def loop():
    global prev_touching
    M5.update()
    touching = M5.Touch.getCount() > 0
    if touching and not prev_touching:
        x = M5.Touch.getX()
        y = M5.Touch.getY()
        if in_rect(x, y, YES_BTN):
            on_yes()
        elif in_rect(x, y, NO_BTN):
            on_no()
    prev_touching = touching
    time.sleep(0.02)


# --- エントリポイント ---------------------------------------------
setup()
try:
    while True:
        loop()
except KeyboardInterrupt:
    print("stopped")
