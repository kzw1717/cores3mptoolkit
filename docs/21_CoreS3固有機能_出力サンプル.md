# CoreS3 固有機能 出力サンプル解説

M5Stack CoreS3 の**本体内蔵機能（出力系）**を使うサンプルの解説です。
**配線は不要**で、UIFlow2 の **M5 ライブラリ**で書きます。各リンクから `.py` を開けます。

## 共通事項

- **接続**：不要（すべて本体内蔵。Discord 系のみ Wi-Fi を使用）。
- **書き方**：`import M5` ＋ `from M5 import *`。`setup()` で `M5.begin()`、`loop()` で `M5.update()` を必ず呼ぶ。
- **実行**：`mpremote run ファイル名.py`（VSCode は対象を開いて `Ctrl+Shift+B`）。
- **停止**：PC 側ターミナルで `Ctrl-C`。

---

## 出力サンプル一覧

難易度は **Python 初心者の大学1年生**を対象に、5段階（**1=一番簡単 〜 5=一番難しい**）で示しています。

| 難易度 | サンプル（.py へのリンク） | 機能（内蔵デバイス） | 動作の概要 |
| :---: | --- | --- | --- |
| 1 | [display_hello_text.py](../m5stack_samples/display_hello_text.py) | ディスプレイ | 文字だけを表示（サイズ・色・位置） |
| 1 | [draw_rectangle.py](../m5stack_samples/draw_rectangle.py) | ディスプレイ（図形） | 四角形（枠線/塗り） |
| 1 | [draw_roundrect.py](../m5stack_samples/draw_roundrect.py) | ディスプレイ（図形） | 角丸四角形（枠線/塗り） |
| 1 | [draw_circle.py](../m5stack_samples/draw_circle.py) | ディスプレイ（図形） | 円（枠線/塗り） |
| 1 | [draw_ellipse.py](../m5stack_samples/draw_ellipse.py) | ディスプレイ（図形） | 楕円（枠線/塗り） |
| 1 | [draw_line.py](../m5stack_samples/draw_line.py) | ディスプレイ（図形） | 直線 |
| 2 | [draw_triangle.py](../m5stack_samples/draw_triangle.py) | ディスプレイ（図形） | 三角形（枠線/塗り） |
| 2 | [draw_arc.py](../m5stack_samples/draw_arc.py) | ディスプレイ（図形） | 円弧・扇形 |
| 2 | [display_hello_draw.py](../m5stack_samples/display_hello_draw.py) | ディスプレイ | いろいろな図形をまとめて表示 |
| 2 | [speaker_tone.py](../m5stack_samples/speaker_tone.py) | スピーカー（AW88298 / 1W） | ドレミを再生 |
| 2 | [display_image.py](../m5stack_samples/display_image.py) | ディスプレイ | 用意した PNG 画像を表示（要・画像転送） |
| 2 | [play_wav.py](../m5stack_samples/play_wav.py) | スピーカー | 用意した WAV を再生（要・音声転送） |
| 3 | [display_hello.py](../m5stack_samples/display_hello.py) | ディスプレイ | 文字・図形・更新カウンタをまとめて表示 |
| 4 | [discord_text.py](../m5stack_samples/discord_text.py) | Wi-Fi / HTTP | Discord Webhook にテキスト送信 |
| 5 | [discord_camera.py](../m5stack_samples/discord_camera.py) | カメラ + Wi-Fi | 撮影画像を Discord Webhook に送信 |

---

## 各サンプルの解説

難易度の低い順に並べています。各見出しのリンクから `.py` を開けます。
座標は左上が `(0, 0)`、画面は **320 × 240 px**、色は `0xRRGGBB`（例：赤=0xFF0000）。

### 1. [display_hello_text.py](../m5stack_samples/display_hello_text.py) ── 文字表示のみ（難易度1）

画面に文字だけを表示します。色・サイズ・位置の変え方の基本です。

```python
M5.Lcd.setTextColor(0xFFFF00, 0x000000)   # 文字色, 背景色
M5.Lcd.setTextSize(3)                      # 文字サイズ（倍率）
M5.Lcd.setCursor(10, 10)                   # 表示開始位置 (x, y)
M5.Lcd.print("Hello, M5Stack!")
```

ポイント：`setTextColor → setTextSize → setCursor → print` の順で書きます。

### 1. [draw_rectangle.py](../m5stack_samples/draw_rectangle.py) ── 四角形（難易度1）

```python
M5.Lcd.drawRect(30, 70, 110, 90, 0x00FF00)    # 枠線だけ
M5.Lcd.fillRect(180, 70, 110, 90, 0x0000FF)   # 塗りつぶし
```

ポイント：図形には「枠線だけ（**draw**〜）」と「塗りつぶし（**fill**〜）」の2種類があります。

### 1. [draw_roundrect.py](../m5stack_samples/draw_roundrect.py) ── 角丸四角形（難易度1）

```python
M5.Lcd.fillRoundRect(30, 70, 110, 90, 20, 0xFF9800)   # x, y, w, h, r(角の半径), color
```

ポイント：四角形に角の半径 `r` が増えただけです。

### 1. [draw_circle.py](../m5stack_samples/draw_circle.py) ── 円（難易度1）

```python
M5.Lcd.drawCircle(90, 130, 50, 0x33CCFF)     # 中心(x, y), 半径 r, 色
M5.Lcd.fillCircle(230, 130, 50, 0x00FFFF)
```

ポイント：`(x, y)` は円の**中心**です。

### 1. [draw_ellipse.py](../m5stack_samples/draw_ellipse.py) ── 楕円（難易度1）

```python
M5.Lcd.fillEllipse(230, 130, 55, 35, 0x00FF00)   # 中心(x, y), 横半径 rx, 縦半径 ry, 色
```

ポイント：横半径 `rx` と縦半径 `ry` を別々に指定します（円の応用）。

### 1. [draw_line.py](../m5stack_samples/draw_line.py) ── 直線（難易度1）

```python
M5.Lcd.drawLine(20, 60, 300, 60, 0xFF0000)    # 点(x0,y0)〜点(x1,y1) を結ぶ
```

ポイント：始点と終点の2点を指定するだけです。

### 2. [draw_triangle.py](../m5stack_samples/draw_triangle.py) ── 三角形（難易度2）

```python
M5.Lcd.fillTriangle(240, 60, 190, 170, 290, 170, 0xFF00FF)   # 3点 (x0,y0)(x1,y1)(x2,y2)
```

ポイント：頂点が3つ（座標6個）になるので、少し数が多くなります。

### 2. [draw_arc.py](../m5stack_samples/draw_arc.py) ── 円弧・扇形（難易度2）

```python
M5.Lcd.drawArc(90, 140, 35, 55, 0, 270, 0xFFFF00)   # 中心, 内半径 r0, 外半径 r1, 開始角, 終了角, 色
M5.Lcd.fillArc(230, 140, 0, 55, 0, 120, 0x9C27B0)   # r0=0 で扇形
```

ポイント：内半径 `r0`・外半径 `r1` でリングの太さ、開始角〜終了角（**度**）で描く範囲を決めます。
`r0=0` にすると塗りつぶしの扇形になります。

### 2. [display_hello_draw.py](../m5stack_samples/display_hello_draw.py) ── 図形まとめ（難易度2）

四角・円・線・三角・楕円・円弧など、いろいろな図形を1画面にまとめて描きます。
上の図形サンプルの寄せ集めです。どの図形がどう描かれるか一度に確認できます。

### 2. [speaker_tone.py](../m5stack_samples/speaker_tone.py) ── スピーカーでドレミ（難易度2）

内蔵スピーカーで「ドレミファソラシド」を鳴らします。

```python
Speaker.begin()
Speaker.setVolume(128)              # 音量 0-255
for freq in [262, 294, 330, 349, 392, 440, 494, 523]:
    Speaker.tone(freq, 300)        # 周波数Hz を 300ms 鳴らす
```

ポイント：周波数のリストを `for` で順に鳴らすとメロディになります（リストと繰り返しの練習）。

### 2. [display_image.py](../m5stack_samples/display_image.py) ── PNG 画像を表示（難易度2）

あらかじめ本体に転送した画像（**PNG / JPG / BMP** 対応）を表示します。

```python
Widgets.Image("sample.png", 0, 0)   # (0,0) から画像を描画
```

**画像サイズの条件**

- 画面は **320 × 240 px**。全画面に出すなら **320×240 以内**で用意します。
- 画像は等倍で左上 `(x, y)` から描画されます（自動拡大縮小なし）。画面より大きいとはみ出した分は表示されません。
- 横位置を中央にしたいなら `x = (320 - 画像幅) // 2` のように計算します。

**画像の転送方法（PC → 本体）**

```bat
python -m mpremote cp sample.png :        REM 本体のルートへコピー
python -m mpremote ls                     REM 転送先を確認
```

スクリプトの `IMAGE_PATH` を転送したファイル名に合わせます（既定は `"sample.png"`）。
表示されない場合は `"/flash/sample.png"` のような絶対パスを試します。

### 2. [play_wav.py](../m5stack_samples/play_wav.py) ── WAV 音声を再生（難易度2）

あらかじめ本体に転送した WAV を再生します。

```python
Speaker.begin()
Speaker.setVolume(128)
Speaker.playWavFile("sound.wav")
```

**WAV ファイルの条件（推奨）**：WAV / PCM 16bit / モノラル / 16000 Hz 前後 / 数秒程度。

**WAV ファイルの作り方（代表例）**

- **Audacity（無料・GUI）**：音声を開く →「ステレオからモノラルへ」→ 左下のサンプリング周波数を `16000` →
  「ファイル → 書き出し → WAV (16bit PCM)」で保存。
- **ffmpeg（コマンド）**：
  ```bat
  ffmpeg -i input.mp3 -ac 1 -ar 16000 -sample_fmt s16 sound.wav
  ```
  （`-ac 1`=モノラル / `-ar 16000`=16kHz / `-sample_fmt s16`=16bit PCM）

**転送方法**：`python -m mpremote cp sound.wav :` でコピー。スクリプトの `WAV_PATH` を合わせます。

### 3. [display_hello.py](../m5stack_samples/display_hello.py) ── 文字＋図形＋更新（難易度3）

文字・図形・「毎秒増えるカウンタ」をまとめて表示します。`Widgets`（UI部品）を使い、
一度作ったラベルを `setText()` で書き換えて表示を更新します。

```python
label = Widgets.Label("count: 0", 120, 160, 1.0, 0xFFFFFF, 0x000000, Widgets.FONTS.DejaVu18)
count += 1
label.setText("count: {}".format(count))   # 既存ラベルの文字だけ更新
```

ポイント：`loop()` の中で値を更新して `setText()` する流れは、センサー値の表示更新にそのまま使えます。

### 4. [discord_text.py](../m5stack_samples/discord_text.py) ── Discord にテキスト送信（難易度4）

Wi-Fi に接続し、Discord の Webhook にテキストを送ります。

```python
import requests2
res = requests2.post(WEBHOOK_URL, json={"content": "こんにちは"})
print(res.status_code)   # 204 で成功
res.close()
```

**事前準備：Webhook URL の取得**

1. Discord の**サーバー設定** →「連携サービス」→「ウェブフック」→「新しいウェブフック」。
2. 投稿先チャンネルを選び「ウェブフック URL をコピー」。
3. URL をスクリプトの `WEBHOOK_URL` に貼る。`WIFI_SSID` / `WIFI_PASS` も自分の値にする。

ポイント：Wi-Fi 接続（`network`）とインターネット送信（`requests2`）が新しく出てきます。
M5Burner で Wi-Fi 設定済みでも、スクリプト側で接続するのが確実です。

### 5. [discord_camera.py](../m5stack_samples/discord_camera.py) ── カメラ画像を Discord に送信（難易度5）

カメラで撮影 → JPEG 変換 → `multipart/form-data` で画像を添付して送ります。最も応用的です。

```python
import camera, jpg, requests2
camera.init(pixformat=camera.RGB565, framesize=camera.QVGA)  # 320x240
img = camera.snapshot()              # 1枚撮影（RGB565）
img_jpg = jpg.encode(img, 80)        # JPEG に変換（品質80）
jpeg_bytes = img_jpg.bytearray()     # JPEG のバイト列
# multipart 本体を組み立てて requests2.post(... data=body, headers=...) で送信
```

ポイント：

- `camera` / `jpg` モジュールは **CoreS3 専用**です。
- 撮影直後は露出が安定しないため、サンプルでは数フレーム捨ててから撮っています。
- 画像添付は `multipart/form-data` の `file` パートに JPEG を入れます（`build_multipart()` が組み立て）。
  送信成功時の応答コードは **204**（環境により 200）。Wi-Fi・Webhook の準備は `discord_text.py` と同じです。

---

## 出力モジュールの使い方のポイント

### ディスプレイ（画面に表示する）

文字や図形は `Widgets`（UI部品）または `M5.Lcd`（描画API）で表示します。`Widgets.Label` は
一度作ったラベルを `setText()` で書き換えられるので、値の表示更新に向きます。

```python
Widgets.fillScreen(0x000000)                       # 背景を黒で塗る
label = Widgets.Label("Hello", 10, 60, 1.0,        # 文字, x, y, 倍率,
                      0xFFFF00, 0x000000,           # 文字色, 背景色,
                      Widgets.FONTS.DejaVu24)       # フォント
label.setText("count: 5")                          # 既存ラベルの文字を更新
```

図形は `M5.Lcd` で描き、各図形に「枠線だけ（**draw**〜）」と「塗りつぶし（**fill**〜）」があります
（個々の図形は上の各サンプルを参照）。色は `0xRRGGBB` の16進数です。

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
- Image（画像表示）：<https://uiflow-micropython.readthedocs.io/en/latest/widgets/image.html>
- Speaker（WAV 再生）：<https://uiflow-micropython.readthedocs.io/en/latest/hardware/speaker.html>
- requests2（HTTP）：<https://uiflow-micropython.readthedocs.io/en/latest/software/requests2.html>
- camera / jpg（撮影）：<https://uiflow-micropython.readthedocs.io/en/latest/advanced/camera.html>
