# CoreS3 固有機能 出力サンプル解説

M5Stack CoreS3 の**本体内蔵機能（出力系）**を使うサンプルの解説です。
**配線は不要**で、UIFlow2 の **M5 ライブラリ**で書きます。各リンクから `.py` を開けます。

## 共通事項

- **接続**：不要（すべて本体内蔵）。
- **書き方**：`import M5` ＋ `from M5 import *`。`setup()` で `M5.begin()`、`loop()` で `M5.update()` を必ず呼ぶ。
- **実行**：`mpremote run ファイル名.py`（VSCode は対象を開いて `Ctrl+Shift+B`）。
- **停止**：PC 側ターミナルで `Ctrl-C`。

---

## 出力サンプル一覧

| サンプル（.py へのリンク） | 機能（内蔵デバイス） | 動作の概要 |
| --- | --- | --- |
| [display_hello.py](../m5stack_samples/display_hello.py) | ディスプレイ（2.0" IPS） | 文字・図形・更新カウンタを表示 |
| [speaker_tone.py](../m5stack_samples/speaker_tone.py) | スピーカー（AW88298 / 1W） | ドレミを再生 |

---

## それぞれの要点

### ディスプレイ（画面に表示する）

`Widgets`（UI部品）で文字や図形を描きます。一度作ったラベルは `setText()` で
中身だけ書き換えられるので、センサー値の表示更新に向きます。

```python
Widgets.fillScreen(0x000000)                       # 背景を黒で塗る
label = Widgets.Label("Hello", 10, 60, 1.0,        # 文字, x, y, 倍率,
                      0xFFFF00, 0x000000,           # 文字色, 背景色,
                      Widgets.FONTS.DejaVu24)       # フォント
Widgets.Circle(60, 170, 30, 0x00FF00, 0x00FF00)    # 円: x, y, 半径, 線色, 塗り色
label.setText("count: 5")                          # 既存ラベルの文字を更新
```

色は `0xRRGGBB` の16進数で指定します（例：赤=0xFF0000, 緑=0x00FF00, 青=0x0000FF）。

### スピーカー（音を鳴らす）

`Speaker.begin()` で開始し、`Speaker.tone(周波数Hz, 長さms)` で単音を鳴らします。
音量は `Speaker.setVolume(0-255)`。周波数を変えれば音程、配列で並べればメロディです。

```python
Speaker.begin()
Speaker.setVolume(128)        # 0-255
Speaker.tone(440, 300)        # 440Hz を 300ms 鳴らす
```

> **必須メモ**：`M5.begin()` と、ループ内の `M5.update()` を忘れないこと。
> スピーカーは `Speaker.begin()` も最初に呼びます。

---

→ 入力系は [20_CoreS3固有機能_入力サンプル.md](20_CoreS3固有機能_入力サンプル.md) を参照。

### 参考（公式 API）
- Display / Widgets：<https://uiflow-micropython.readthedocs.io/en/latest/widgets/index.html>
- Speaker：<https://uiflow-micropython.readthedocs.io/en/latest/hardware/speaker.html>
