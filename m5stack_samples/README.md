# m5stack_samples — CoreS3 固有機能サンプル

M5Stack CoreS3 の**本体内蔵機能**を MicroPython（UIFlow2 の M5 ライブラリ）で動かす
サンプル集です。Grove と違い、いずれも**配線不要**で動きます。

各スクリプトは PC と USB でつないだ状態で `mpremote run` で実行します
（VSCode なら対象ファイルを開いて `Ctrl+Shift+B`）。停止は PC 側ターミナルで `Ctrl-C`。

| ファイル | 機能 | 種別 | 動作の概要 |
| --- | --- | --- | --- |
| `imu_accel.py` | 内蔵IMU (BMI270) | 入力 | 加速度・ジャイロを画面と端末に表示 |
| `touch_position.py` | タッチパネル | 入力 | 触れた座標 (x, y) を表示 |
| `battery_status.py` | 電源管理 (AXP2101) | 入力 | 電池残量[%]・電圧[mV]・充電状態を表示 |
| `touch_button_single.py` | タッチパネル | 入力 | 1ボタンを押した回数を表示 |
| `touch_button_yesno.py` | タッチパネル | 入力 | YES/NO 2ボタンの押下回数を表示 |
| `touch_counter.py` | タッチパネル | 入力 | 画面タッチ回数を表示 |
| `display_hello.py` | ディスプレイ | 出力 | 文字・図形・更新カウンタをまとめて表示 |
| `display_hello_text.py` | ディスプレイ | 出力 | 文字表示のみ |
| `display_hello_draw.py` | ディスプレイ | 出力 | 図形描画のみ（円以外も含む） |
| `draw_rectangle.py` | ディスプレイ | 出力 | 図形：四角形 |
| `draw_roundrect.py` | ディスプレイ | 出力 | 図形：角丸四角形 |
| `draw_circle.py` | ディスプレイ | 出力 | 図形：円 |
| `draw_ellipse.py` | ディスプレイ | 出力 | 図形：楕円 |
| `draw_line.py` | ディスプレイ | 出力 | 図形：直線 |
| `draw_triangle.py` | ディスプレイ | 出力 | 図形：三角形 |
| `draw_arc.py` | ディスプレイ | 出力 | 図形：円弧・扇形 |
| `speaker_tone.py` | スピーカー | 出力 | ドレミを再生 |
| `display_image.py` | ディスプレイ | 出力 | 用意した PNG 画像を表示（要・画像転送） |
| `play_wav.py` | スピーカー | 出力 | 用意した WAV を再生（要・音声転送） |
| `discord_text.py` | Wi-Fi / HTTP | 出力 | Discord Webhook にテキスト送信 |
| `discord_camera.py` | カメラ + Wi-Fi | 出力 | 撮影画像を Discord Webhook に送信 |

詳しい解説は次の解説ページを参照してください。

- 入力系：[`docs/20_CoreS3固有機能_入力サンプル.md`](../docs/20_CoreS3固有機能_入力サンプル.md)
- 出力系：[`docs/21_CoreS3固有機能_出力サンプル.md`](../docs/21_CoreS3固有機能_出力サンプル.md)

## 共通の書き方（M5 ライブラリ）

```python
import M5
from M5 import *      # Widgets, Imu, Speaker, Power などが使える

def setup():
    M5.begin()        # 最初に一度だけ。必須
    ...

def loop():
    M5.update()       # ループ内で毎回呼ぶ。必須
    ...

setup()
try:
    while True:
        loop()
except KeyboardInterrupt:   # PC側 Ctrl-C で停止
    print("終了しました")
```

> メモ：`M5.begin()`（初期化）と、ループ内の `M5.update()`（状態更新）は
> M5 ライブラリを使う上で必須です。これを忘れるとセンサー値やタッチが更新されません。
