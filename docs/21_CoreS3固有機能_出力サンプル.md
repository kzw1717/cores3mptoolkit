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
| [display_hello.py](../m5stack_samples/display_hello.py) | ディスプレイ（2.0" IPS） | 文字・図形・更新カウンタをまとめて表示 |
| [display_hello_text.py](../m5stack_samples/display_hello_text.py) | ディスプレイ | 文字表示のみ（サイズ・色・位置） |
| [display_hello_draw.py](../m5stack_samples/display_hello_draw.py) | ディスプレイ | 図形描画のみ（円以外も含むまとめ） |
| [speaker_tone.py](../m5stack_samples/speaker_tone.py) | スピーカー（AW88298 / 1W） | ドレミを再生 |
| [display_image.py](../m5stack_samples/display_image.py) | ディスプレイ | 用意した PNG 画像を表示 |
| [play_wav.py](../m5stack_samples/play_wav.py) | スピーカー | 用意した WAV 音声を再生 |
| [discord_text.py](../m5stack_samples/discord_text.py) | Wi-Fi / HTTP | Discord Webhook にテキスト送信 |
| [discord_camera.py](../m5stack_samples/discord_camera.py) | カメラ + Wi-Fi | 撮影画像を Discord Webhook に送信 |

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

#### 文字だけ / 図形だけに分けたサンプル

`display_hello.py` を用途別に分けたものです。必要な方をコピーして使ってください。

- 文字のみ：[display_hello_text.py](../m5stack_samples/display_hello_text.py)
- 図形のみ（まとめ）：[display_hello_draw.py](../m5stack_samples/display_hello_draw.py)

### 図形を描く（`M5.Lcd` の描画API）

図形は `M5.Lcd` で描きます。各図形には「枠線だけ（draw〜）」と「塗りつぶし（fill〜）」が
あります。座標は左上が `(0, 0)`、画面は **320 × 240 px**、色は `0xRRGGBB`。

**図形ごとの個別サンプル**

| サンプル | 図形 | 主なAPI |
| --- | --- | --- |
| [draw_rectangle.py](../m5stack_samples/draw_rectangle.py) | 四角形 | `drawRect(x,y,w,h,color)` / `fillRect(...)` |
| [draw_roundrect.py](../m5stack_samples/draw_roundrect.py) | 角丸四角形 | `drawRoundRect(x,y,w,h,r,color)` / `fillRoundRect(...)` |
| [draw_circle.py](../m5stack_samples/draw_circle.py) | 円 | `drawCircle(x,y,r,color)` / `fillCircle(...)` |
| [draw_ellipse.py](../m5stack_samples/draw_ellipse.py) | 楕円 | `drawEllipse(x,y,rx,ry,color)` / `fillEllipse(...)` |
| [draw_line.py](../m5stack_samples/draw_line.py) | 直線 | `drawLine(x0,y0,x1,y1,color)` |
| [draw_triangle.py](../m5stack_samples/draw_triangle.py) | 三角形 | `drawTriangle(x0,y0,x1,y1,x2,y2,color)` / `fillTriangle(...)` |
| [draw_arc.py](../m5stack_samples/draw_arc.py) | 円弧・扇形 | `drawArc(x,y,r0,r1,a0,a1,color)` / `fillArc(...)` |

```python
M5.Lcd.fillRect(10, 10, 80, 50, 0x0000FF)            # 四角（塗り）
M5.Lcd.fillCircle(160, 120, 30, 0x00FFFF)            # 円（塗り）
M5.Lcd.drawLine(0, 0, 319, 239, 0xFF0000)            # 直線
M5.Lcd.fillTriangle(10, 10, 50, 80, 90, 10, 0x00FF00)# 三角（塗り）
M5.Lcd.drawArc(160, 120, 30, 50, 0, 270, 0xFFFF00)   # 円弧（角度は度）
```

> 円弧 `Arc` は内半径 `r0`・外半径 `r1` でリングの太さを決め、開始角 `a0`〜終了角 `a1`（度）で
> 描く範囲を決めます。`r0=0` にすると塗りつぶしの扇形になります。

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

## ファイルを使う出力（画像・音声）

### 1. PNG 画像を画面に表示する — [display_image.py](../m5stack_samples/display_image.py)

`Widgets.Image(パス, x, y)` で、本体に保存した画像（**PNG / JPG / BMP** 対応）を表示します。

```python
Widgets.Image("sample.png", 0, 0)   # (0,0) から画像を描画
```

**画像サイズの条件**

- 画面は **320 × 240 px**。全画面に出すなら **320×240 以内**で用意します。
- 画像は等倍で左上 `(x, y)` から描画されます（自動拡大縮小はされません）。画面より大きいと
  はみ出した部分は表示されません。小さい画像は指定位置にそのまま表示されます。
- 横位置中央に置きたいなら `x = (320 - 画像幅) // 2` のように計算します。
- 形式は PNG 推奨（透過も可）。色数が多い写真は JPG だと容量を抑えられます。

**画像の転送方法（PC → 本体）**

PC 上の画像を、`mpremote` で本体へコピーします（このフォルダで実行）。

```bat
python -m mpremote cp sample.png :        REM 本体のルートへコピー
python -m mpremote ls                     REM 転送先を確認（パスの確認に便利）
```

スクリプト側の `IMAGE_PATH` を、転送したファイル名に合わせます（既定は `"sample.png"`）。
表示されない場合は `"/flash/sample.png"` のように絶対パスを試してください。

---

### 2. WAV 音声を再生する — [play_wav.py](../m5stack_samples/play_wav.py)

`Speaker.playWavFile(パス)` で、本体に保存した WAV を再生します。

```python
Speaker.begin()
Speaker.setVolume(128)
Speaker.playWavFile("sound.wav")
```

**WAV ファイルの条件（推奨）**

- 形式：**WAV / PCM 16bit / モノラル**
- サンプルレート：**16000 Hz** 前後（8000〜44100 Hz 程度）
- 長さ：数秒程度（容量が大きいほど転送・再生に時間がかかります）

**WAV ファイルの作り方（代表的な手順）**

- **Audacity（無料・GUI）の場合**
  1. 音声を録音、または音声ファイルを開く。
  2. 必要なら「トラック → ステレオからモノラルへ」でモノラル化。
  3. 左下の「プロジェクトのサンプリング周波数」を `16000` に設定。
  4. 「ファイル → 書き出し → WAV (16bit PCM) として書き出し」で保存。

- **ffmpeg（コマンド）の場合**

  ```bat
  ffmpeg -i input.mp3 -ac 1 -ar 16000 -sample_fmt s16 sound.wav
  ```
  （`-ac 1`=モノラル / `-ar 16000`=16kHz / `-sample_fmt s16`=16bit PCM）

**WAV の転送方法（PC → 本体）**

```bat
python -m mpremote cp sound.wav :
python -m mpremote ls
```

スクリプト側の `WAV_PATH` を転送したファイル名に合わせます（既定は `"sound.wav"`）。

---

## ネットワークを使う出力（Discord Webhook）

下の 2 つは **Wi-Fi 接続**と **Discord Webhook URL** が必要です。

**事前準備：Discord Webhook URL の取得**

1. Discord で対象チャンネルのある**サーバー設定**を開く。
2. 「連携サービス（Integrations）」→「ウェブフック（Webhooks）」→「新しいウェブフック」。
3. 投稿先チャンネルを選び、「ウェブフック URL をコピー」。
4. コピーした URL をスクリプトの `WEBHOOK_URL` に貼り付ける。

**Wi-Fi について**

サンプルは `WIFI_SSID` / `WIFI_PASS` で明示的に接続します。M5Burner で Wi-Fi を
設定済みでも、`mpremote run` で動かすスクリプトでは自分で接続するのが確実です。

### 3. テキストを送る — [discord_text.py](../m5stack_samples/discord_text.py)

`requests2.post(URL, json={"content": "..."})` で送信します。成功すると応答コードは **204**。

```python
import requests2
res = requests2.post(WEBHOOK_URL, json={"content": "こんにちは"})
print(res.status_code)   # 204 で成功
res.close()
```

### 4. カメラ画像を送る — [discord_camera.py](../m5stack_samples/discord_camera.py)

カメラで撮影 → JPEG 変換 → `multipart/form-data` で画像を添付して送信します。

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
- Discord に画像添付するには `multipart/form-data` で `file` パートに JPEG を入れます
  （サンプルの `build_multipart()` が組み立てます）。送信成功時の応答コードは **204**（環境により 200）。

---

→ 入力系は [20_CoreS3固有機能_入力サンプル.md](20_CoreS3固有機能_入力サンプル.md) を参照。

### 参考（公式 API）
- Display / Widgets：<https://uiflow-micropython.readthedocs.io/en/latest/widgets/index.html>
- Image（画像表示）：<https://uiflow-micropython.readthedocs.io/en/latest/widgets/image.html>
- Speaker（WAV 再生）：<https://uiflow-micropython.readthedocs.io/en/latest/hardware/speaker.html>
- requests2（HTTP）：<https://uiflow-micropython.readthedocs.io/en/latest/software/requests2.html>
- camera / jpg（撮影）：<https://uiflow-micropython.readthedocs.io/en/latest/advanced/camera.html>
