# Grove Creater Kit — Level1 サンプルスクリプト解説

M5Stack CoreS3（UIFlow2 ファームウェア / MicroPython）で、Grove Creater Kit の
**Level1 対象 11 項目**（入力8・出力3）を動かすためのサンプルスクリプト集です。
各スクリプトは PC とつないだ状態で `python -m mpremote run` を使って実行します。

各サンプルには番号を付けています（**IG＝入力Grove / OG＝出力Grove**）。
難易度・SKU・1本ごとの詳しい解説は、次の解説ページを参照してください。

- 入力モジュール：[`docs/10_Grove_入力サンプル.md`](../docs/10_Grove_入力サンプル.md)
- 出力モジュール：[`docs/11_Grove_出力サンプル.md`](../docs/11_Grove_出力サンプル.md)

---

## 1. 前提環境

| 項目 | 内容 |
| --- | --- |
| 本体 | M5Stack CoreS3 |
| ファームウェア | UIFlow2（MicroPython ベース） |
| PC ツール | `mpremote`（Python 製のコマンドラインツール。`python -m mpremote ...` で実行） |
| 接続 | USB Type-C ケーブルで CoreS3 と PC を接続 |

CoreS3 の Grove ポートは次のとおりです（本キットの Level1 サンプルが使うのは **PORT.B**）。

| ポート | 種別 | ピン |
| --- | --- | --- |
| PORT.A（赤） | I2C | SCL=G1 / SDA=G2 |
| PORT.B（黒） | GPIO / ADC | G8 / G9 |
| PORT.C（青） | UART | TX=G17 / RX=G18 |

**Level1 の 11 項目はすべて PORT.B の信号ピン G8（`SIG_PIN = 8`）を使います。**
Grove コネクタは信号線が2本あり Port.B では G8/G9 に配線されますが、本キットは全モジュール G8 側です。
（入力と出力の2モジュールを同時に使うときの接続方法は `docs/11` の「チャレンジ課題」を参照）

---

## 2. mpremote の使い方

> Microsoft Store 版 Python では `mpremote` コマンドに PATH が通らないことがあるため、
> 本サンプル集では **`python -m mpremote ...`** の形で実行します。

### 2.1 インストール

PC に Python がある状態で、ターミナル（Windows は PowerShell / コマンドプロンプト）から：

```bash
python -m pip install mpremote
```

更新したいときは：

```bash
python -m pip install -U mpremote
```

### 2.2 デバイスの接続確認

CoreS3 を USB でつなぎ、認識されているシリアルポートを一覧表示します。

```bash
python -m mpremote devs
```

`COM3`（Windows）や `/dev/tty.usbmodem...`（Mac）のように表示されれば認識OKです。
CoreS3 が 1 台だけなら、以降のコマンドは自動でそのデバイスに接続されます。

> Windows で認識されない場合は、M5Stack の USB ドライバ（CP210x / CH9102）を入れてください。

### 2.3 スクリプトを実行する（メイン）

このサンプル集の基本の使い方です。**PC 上の .py を CoreS3 に送って実行**します
（本体には保存されません）。

```bash
# このフォルダに移動してから実行
python -m mpremote run water_sensor.py
```

実行するとセンサーの値などが PC のターミナルに表示されます。

### 2.4 停止する

- **入力（センサー）系**：PC のターミナルで **`Ctrl-C`** を押すと、スクリプトの
  `KeyboardInterrupt` が発生して停止します。
- **出力（LED・モーター）系**：`Ctrl-C` だけでは止まらないことがあります。
  `python -m mpremote run` の Ctrl-C は PC 側の mpremote が終了するだけで、**デバイス上の
  ループは動き続け、GPIO も最後の状態を保持**するためです。**確実に止めるには本体のリセット
  ボタン、または別ターミナルで `python -m mpremote reset`**（USB 抜き差しでも停止）。

### 2.5 その他の便利なコマンド

```bash
python -m mpremote repl                 # REPL(対話モード)に入る。抜けるのは Ctrl-]
python -m mpremote ls                   # 本体内のファイル一覧
python -m mpremote cp water_sensor.py : # PC -> 本体へファイルをコピー
python -m mpremote cp :main.py .        # 本体 -> PC へコピー
python -m mpremote reset                # 本体をリセット（暴走した出力を止めるのにも有効）
```

参考：本体に常駐させたい場合は `main.py` という名前でコピーすると、
電源投入時に自動実行されます（その場合は PC 非接続のため Ctrl-C では止まりません）。

---

## 3. スクリプト共通の構成

すべてのサンプルは Arduino と同じ **`setup()` / `loop()`** の形にそろえています。

```python
def setup():
    # 起動時に一度だけ実行（ピンの初期化など）
    ...

def loop():
    # 繰り返し実行（センサー読み取りや出力）
    ...

setup()
try:
    while True:
        loop()
except KeyboardInterrupt:   # PC側 Ctrl-C で停止
    print("stopped")
```

> 実機では `print()` に日本語を渡すと出力が止まるため、**表示は英語**にしています。

ファイル冒頭のコメントに「接続ポート・実行方法・終了方法」を記載しています。
ピン番号や測定間隔はファイル先頭の **設定（定数）** をいじるだけで変更できます。

---

## 4. 各スクリプトの説明

番号・難易度は解説ページ（`docs/10`・`docs/11`）と対応しています。
難易度は **Python 初心者の大学1年生**を対象にした5段階（1=易しい〜5=難しい）です。
1本ごとの詳しい解説は各解説ページを参照してください。

### 入力モジュール（→ [docs/10](../docs/10_Grove_入力サンプル.md)）

| 番号 | 難易度 | ファイル | Product Name | 信号 | 動作の概要 |
| :---: | :---: | --- | --- | --- | --- |
| IG1 | 1 | `tilt_switch.py` | Grove - Tilt Switch | デジタル | 傾きで `ON`/`off` |
| IG2 | 1 | `touch_sensor.py` | Grove - Touch Sensor | デジタル | 触れると `touched` |
| IG3 | 2 | `moisture_sensor.py` | Grove - Moisture Sensor | アナログ(ADC) | 土壌水分値を表示 |
| IG4 | 2 | `light_sensor.py` | Grove - Light Sensor v1.2 | アナログ(ADC) | 明るさを 0–65535 で表示 |
| IG5 | 3 | `water_sensor.py` | Grove - Water Sensor | アナログ(ADC) | しきい値で `WET`/`dry` |
| IG6 | 3 | `sound_sensor.py` | Grove - Sound Sensor | アナログ(ADC) | 音量（振幅）を表示 |
| IG7 | 4 | `temperature_sensor.py` | Grove - Temperature Sensor | アナログ(ADC) | 温度[℃]を表示 |
| IG8 | 5 | `ultrasonic_ranger.py` | Grove - Ultrasonic Ranger | デジタル(単線SIG) | 距離[cm]を表示（範囲外は通知） |

### 出力モジュール（→ [docs/11](../docs/11_Grove_出力サンプル.md)）

| 番号 | 難易度 | ファイル | Product Name | 信号 | 動作の概要 |
| :---: | :---: | --- | --- | --- | --- |
| OG1 | 1 | `red_led.py` | Grove - Red LED | デジタル | 赤LEDを 0.5 秒ごとに点滅 |
| OG2 | 1 | `blue_led.py` | Grove - Blue LED | デジタル | 青LEDを 0.5 秒ごとに点滅 |
| OG3 | 2 | `vibration_motor.py` | Grove - Vibration Motor | デジタル | 1 秒ごとに振動/停止 |

### 補足メモ

- **デジタル入力**（tilt / touch）は `Pin(8, Pin.IN)` の `value()` が 0/1 を返します。
  検知時 HIGH（=1）を想定しています。配線や個体で論理が逆の場合は判定を入れ替えてください。
- **アナログ系**（moisture / light / water / sound）は `ADC.ATTN_11DB` を指定して
  0–3.3V を 0–65535 の `read_u16()` で読みます。値は環境で変わるので、しきい値
  （例：`water_sensor.py` の `WET_THRESHOLD`）は実機で校正してください。
  `sound_sensor.py` は交流波形を高速サンプリングして **最大−最小（振幅）** を音量の目安にします。
- **temperature_sensor.py** はアナログ値を電圧に直し、サーミスタの式（`math.log`）で温度に
  換算します。5V 動作×ADC 基準 3.3V のズレを補正するため、`VREF` を実機で微調整します。
- **ultrasonic_ranger.py** は 1 本の信号線でトリガ送信とエコー受信を行うため、
  ピンの入出力を切り替えて `time_pulse_us()` でパルス幅を測っています。
- **出力（LED・モーター）** は `Pin(8, Pin.OUT)` の `value(1)/value(0)` で ON/OFF。
  停止は本体リセット or `python -m mpremote reset`（Ctrl-C で止まらないことがあるため）。

---

## 5. かんたんトラブルシュート

| 症状 | 対処 |
| --- | --- |
| `python -m mpremote devs` に出てこない | USB ケーブル（データ通信対応か）/ ドライバ / 別ポートを確認 |
| `could not enter raw repl` | 他アプリ（UIFlow, シリアルモニタ等）がポート占有していないか確認 |
| 値が常に 0 / 65535・反応しない | 信号ピンが **G8**（`SIG_PIN = 8`）か、PORT.B に挿しているか確認 |
| LED・モーターが動かない | モジュールの向き・極性、PORT.B 接続、`SIG_PIN = 8` を確認 |
| 出力が止まらない | 本体リセットボタン、または `python -m mpremote reset` |
| 距離が常に「範囲外」 | センサー前方に対象があるか、`TIMEOUT_US` を確認 |

---

### 対象部品（Level1：11項目）

Tilt Switch / Touch Sensor / Moisture Sensor / Light Sensor v1.2 / Water Sensor /
Sound Sensor / Temperature Sensor / Ultrasonic Ranger /
Red LED / Blue LED / Vibration Motor
