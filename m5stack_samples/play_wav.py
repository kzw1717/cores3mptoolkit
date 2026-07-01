"""
CoreS3 内蔵 スピーカー ── WAV 音声ファイル再生サンプル（出力）
------------------------------------------------------
あらかじめ本体に転送しておいた WAV ファイルを再生します。
WAV は PC から mpremote で本体へコピーしておきます（解説ページ参照）。

対象 : M5Stack CoreS3 + UIFlow2 ファームウェア（M5 ライブラリ）
接続 : 不要（本体内蔵スピーカー）
準備 : WAV を本体へ転送 →  python -m mpremote cp sound.wav :
実行 : python -m mpremote run play_wav.py    （VSCode は Ctrl+Shift+B）
終了 : Ctrl-C（PC側ターミナルで送信）
参考 : https://uiflow-micropython.readthedocs.io/en/latest/hardware/speaker.html

WAV の条件（推奨）:
- 形式 : WAV / PCM 16bit / モノラル
- サンプルレート : 16000 Hz 前後（8000〜44100 Hz 程度）
- 長さ : 数秒程度（容量が大きいと転送・再生に時間がかかる）
"""

import M5
from M5 import *
import time

# --- 設定 ---------------------------------------------------------
WAV_PATH = "sound.wav"    # 本体へ転送した WAV のパス（見つからない場合は "/flash/sound.wav" を試す）
VOLUME = 128              # 音量 0-255
REPEAT_INTERVAL = 3.0     # 繰り返し再生の間隔 [秒]


def setup():
    """起動時に一度だけ実行する初期化処理"""
    M5.begin()
    Speaker.begin()
    Speaker.setVolume(VOLUME)
    Widgets.fillScreen(0x222222)
    Widgets.Title("CoreS3 WAV Player", 3, 0xFFFFFF, 0x0000FF, Widgets.FONTS.DejaVu18)
    Widgets.Label("Play: " + WAV_PATH, 10, 80, 1.0, 0xFFFFFF, 0x222222, Widgets.FONTS.DejaVu18)
    print("WAV play started: {} (Ctrl-C to stop)".format(WAV_PATH))


def loop():
    """繰り返し実行する処理（一定間隔で再生）"""
    M5.update()
    Speaker.playWavFile(WAV_PATH)   # WAV ファイルを再生
    time.sleep(REPEAT_INTERVAL)


# --- エントリポイント ---------------------------------------------
setup()
try:
    while True:
        loop()
except KeyboardInterrupt:
    print("stopped")
