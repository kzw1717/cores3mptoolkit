"""
CoreS3 内蔵 スピーカー (AW88298 / 1W)  ── 出力サンプル
------------------------------------------------------
内蔵スピーカーで「ドレミファソラシド」を鳴らします。
Speaker.tone(周波数Hz, 長さms) で単音を鳴らせます。配線は不要です（本体内蔵）。

対象 : M5Stack CoreS3 + UIFlow2 ファームウェア（M5 ライブラリ）
接続 : 不要（本体内蔵スピーカー）
実行 : mpremote run speaker_tone.py    （VSCode は Ctrl+Shift+B）
終了 : Ctrl-C（PC側ターミナルで送信）
参考 : https://uiflow-micropython.readthedocs.io/en/latest/hardware/speaker.html
"""

import M5
from M5 import *
import time

# --- 設定 ---------------------------------------------------------
# ドレミファソラシド の周波数 [Hz]
SCALE = [262, 294, 330, 349, 392, 440, 494, 523]
NOTE_MS = 300         # 1音の長さ [ミリ秒]
VOLUME = 128          # 音量 0-255


def setup():
    """起動時に一度だけ実行する初期化処理"""
    M5.begin()
    Speaker.begin()                 # スピーカー機能を開始
    Speaker.setVolume(VOLUME)       # 音量設定 (0-255)
    Widgets.fillScreen(0x222222)
    Widgets.Title("CoreS3 Speaker", 3, 0xFFFFFF, 0x0000FF, Widgets.FONTS.DejaVu18)
    Widgets.Label("ドレミ を再生中...", 10, 80, 1.0, 0xFFFFFF, 0x222222, Widgets.FONTS.DejaVu18)
    print("スピーカー開始 (Ctrl-C で終了)")


def loop():
    """繰り返し実行する処理"""
    M5.update()
    for freq in SCALE:
        Speaker.tone(freq, NOTE_MS)         # 単音を鳴らす
        time.sleep(NOTE_MS / 1000 + 0.05)   # 鳴り終わるまで待つ
    time.sleep(1.0)                          # ひと巡りしたら少し休む


# --- エントリポイント ---------------------------------------------
setup()
try:
    while True:
        loop()
except KeyboardInterrupt:
    print("終了しました")
