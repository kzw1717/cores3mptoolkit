# m5stack_samples — CoreS3 固有機能サンプル

M5Stack CoreS3 の**本体内蔵機能**を MicroPython（UIFlow2 の M5 ライブラリ）で動かす
サンプル集です。Grove と違い、いずれも**配線不要**で動きます。

各スクリプトは PC と USB でつないだ状態で `mpremote run` で実行します
（VSCode なら対象ファイルを開いて `Ctrl+Shift+B`）。停止は PC 側ターミナルで `Ctrl-C`。

各サンプルには番号を付けています（**IM＝入力M5Stack / OM＝出力M5Stack**）。
番号・難易度は解説ページと対応しています。難易度は **Python 初心者の大学1年生**を
対象にした5段階（1=易しい〜5=難しい）です。1本ごとの詳しい解説は解説ページを参照してください。

- 入力系：[`docs/20_CoreS3固有機能_入力サンプル.md`](../docs/20_CoreS3固有機能_入力サンプル.md)
- 出力系：[`docs/21_CoreS3固有機能_出力サンプル.md`](../docs/21_CoreS3固有機能_出力サンプル.md)

### 入力サンプル（→ [docs/20](../docs/20_CoreS3固有機能_入力サンプル.md)）

| 番号 | 難易度 | ファイル | 機能（内蔵デバイス） | 動作の概要 |
| :---: | :---: | --- | --- | --- |
| IM1 | 2 | `touch_position.py` | タッチパネル | 触れた座標 (x, y) を表示 |
| IM2 | 2 | `battery_status.py` | 電源管理 (AXP2101) | 電池残量[%]・電圧[mV]・充電状態を表示 |
| IM3 | 3 | `imu_accel.py` | 内蔵IMU (BMI270) | 加速度・ジャイロを画面と端末に表示 |
| IM4 | 3 | `touch_counter.py` | タッチパネル | 画面タッチ回数を表示 |
| IM5 | 4 | `touch_button_single.py` | タッチパネル | 1ボタンを押した回数を表示 |
| IM6 | 4 | `touch_button_yesno.py` | タッチパネル | YES/NO 2ボタンの押下回数を表示 |

### 出力サンプル（→ [docs/21](../docs/21_CoreS3固有機能_出力サンプル.md)）

| 番号 | 難易度 | ファイル | 機能（内蔵デバイス） | 動作の概要 |
| :---: | :---: | --- | --- | --- |
| OM1 | 1 | `display_hello_text.py` | ディスプレイ | 文字だけを表示 |
| OM2 | 1 | `draw_rectangle.py` | ディスプレイ（図形） | 四角形（枠線/塗り） |
| OM3 | 1 | `draw_roundrect.py` | ディスプレイ（図形） | 角丸四角形（枠線/塗り） |
| OM4 | 1 | `draw_circle.py` | ディスプレイ（図形） | 円（枠線/塗り） |
| OM5 | 1 | `draw_ellipse.py` | ディスプレイ（図形） | 楕円（枠線/塗り） |
| OM6 | 1 | `draw_line.py` | ディスプレイ（図形） | 直線 |
| OM7 | 2 | `draw_triangle.py` | ディスプレイ（図形） | 三角形（枠線/塗り） |
| OM8 | 2 | `draw_arc.py` | ディスプレイ（図形） | 円弧・扇形 |
| OM9 | 2 | `display_hello_draw.py` | ディスプレイ | いろいろな図形をまとめて表示 |
| OM10 | 2 | `speaker_tone.py` | スピーカー (AW88298) | ドレミを再生 |
| OM11 | 2 | `display_image.py` | ディスプレイ | 用意した PNG 画像を表示（要・画像転送） |
| OM12 | 2 | `play_wav.py` | スピーカー | 用意した WAV を再生（要・音声転送） |
| OM13 | 3 | `display_hello.py` | ディスプレイ | 文字・図形・更新カウンタをまとめて表示 |
| OM14 | 4 | `discord_text.py` | Wi-Fi / HTTP | Discord Webhook にテキスト送信 |
| OM15 | 5 | `discord_camera.py` | カメラ + Wi-Fi | 撮影画像を Discord Webhook に送信 |

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
