# Grove Creater Kit — Level1 サンプルスクリプト解説

M5Stack CoreS3（UIFlow2 ファームウェア / MicroPython）で、Grove Creater Kit の
**Level1 対象 10 項目**を動かすためのサンプルスクリプト集です。
各スクリプトは PC とつないだ状態で `mpremote run` を使って実行します。

---

## 1. 前提環境

| 項目 | 内容 |
| --- | --- |
| 本体 | M5Stack CoreS3 |
| ファームウェア | UIFlow2（MicroPython ベース） |
| PC ツール | `mpremote`（Python 製のコマンドラインツール） |
| 接続 | USB Type-C ケーブルで CoreS3 と PC を接続 |

CoreS3 の Grove ポートは次のとおりです（本キットのサンプルが使うのは PORT.A と PORT.B）。

| ポート | 種別 | ピン |
| --- | --- | --- |
| PORT.A（赤） | I2C | SCL=G1 / SDA=G2 |
| PORT.B（黒） | GPIO / ADC | 黄=G9 / 白=G8 |
| PORT.C（青） | UART | TX=G17 / RX=G18 |

Grove 4極ケーブルの色と信号の対応：**黒=GND / 赤=5V / 黄=信号(主) / 白=信号(副)**。
Level1 の 10 項目はすべて **PORT.B の黄線（G9）** を信号に使います。

---

## 2. mpremote の使い方

### 2.1 インストール

PC に Python がある状態で、ターミナル（Windows はコマンドプロンプト / PowerShell）から：

```bash
pip install mpremote
```

更新したいときは：

```bash
pip install -U mpremote
```

### 2.2 デバイスの接続確認

CoreS3 を USB でつなぎ、認識されているシリアルポートを一覧表示します。

```bash
mpremote devs
```

`COM3`（Windows）や `/dev/tty.usbmodem...`（Mac）のように表示されれば認識OKです。
CoreS3 が 1 台だけなら、以降のコマンドは自動でそのデバイスに接続されます。

> Windows で認識されない場合は、M5Stack の USB ドライバ（CP210x / CH9102）を入れてください。

### 2.3 スクリプトを実行する（メイン）

このサンプル集の基本の使い方です。**PC 上の .py を CoreS3 に送って実行**します
（本体には保存されません）。

```bash
# このフォルダに移動してから実行
mpremote run water_sensor.py
```

実行するとセンサーの値などが PC のターミナルに表示されます。

### 2.4 停止する（Ctrl-C）

実行を止めるには、**PC のターミナルで `Ctrl-C` を押します**。
CoreS3 本体にキーボードはありませんが、`Ctrl-C` は USB シリアル経由で本体に送られ、
スクリプト側の `KeyboardInterrupt` が発生して「終了しました」と表示して停止します。

> このサンプル集は「PC につないで `mpremote run` で動かす」前提のため、
> 停止は PC からの `Ctrl-C` で行います。

### 2.5 その他の便利なコマンド

```bash
mpremote repl                 # REPL(対話モード)に入る。抜けるのは Ctrl-]
mpremote ls                   # 本体内のファイル一覧
mpremote cp water_sensor.py : # PC -> 本体へファイルをコピー
mpremote cp :main.py .        # 本体 -> PC へコピー
mpremote reset                # 本体をリセット
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
    print("終了しました")
```

ファイル冒頭のコメントに「接続ポート・実行方法・終了方法」を記載しています。
ピン番号や測定間隔はファイル先頭の **設定（定数）** をいじるだけで変更できます。

---

## 4. 各スクリプトの説明

| ファイル | 部品 | 種別 | 動作の概要 |
| --- | --- | --- | --- |
| `water_sensor.py` | Grove - Water Sensor | デジタル入力 | 水検知で `WET`、乾燥で `dry` を表示 |
| `light_sensor.py` | Grove - Light Sensor v1.2 | アナログ(ADC) | 明るさを 0–65535 の数値で表示 |
| `magnetic_switch.py` | Grove - Magnetic Switch | デジタル入力 | 磁石の接近で `MAGNET` を表示 |
| `dht11.py` | Grove - DHT11 | デジタル(1線) | 温度[℃]・湿度[%]を表示 |
| `red_led.py` | Grove - Red LED | デジタル出力 | 赤LEDを 0.5 秒ごとに点滅 |
| `blue_led.py` | Grove - Blue LED | デジタル出力 | 青LEDを 0.5 秒ごとに点滅 |
| `moisture_sensor.py` | Grove - Moisture Sensor | アナログ(ADC) | 土壌水分値と `WET/dry` を表示 |
| `pir_motion_sensor.py` | Grove - Mini PIR Motion | デジタル入力 | 動きを検知すると `MOTION` を表示 |
| `loudness_sensor.py` | Grove - Loudness Sensor | アナログ(ADC) | 音量を 0–65535 の数値で表示 |
| `ultrasonic_ranger.py` | Grove - Ultrasonic Ranger | デジタル(単線SIG) | 距離[cm]を表示（範囲外は通知） |

### 補足メモ

- **アナログ系**（light / moisture / loudness）は `ADC.ATTN_11DB` を指定して
  0–3.3V を 0–65535 の `read_u16()` で読みます。値は環境に応じて変わるので、
  しきい値（例：`moisture_sensor.py` の `WET_LEVEL`）は実機で校正してください。
- **DHT11** は読み取りに 1 秒以上の間隔が必要なため `INTERVAL = 2.0` にしています。
  `dht` モジュールは MicroPython 標準搭載で、追加導入は不要です。
- **Ultrasonic Ranger** は 1 本の信号線でトリガ送信とエコー受信を行うため、
  ピンの入出力を切り替えて `time_pulse_us()` でパルス幅を測っています。
- **Magnetic / PIR** は検知時 HIGH を想定しています。配線や個体で論理が逆の場合は、
  `value()` の判定（`== 1` / `== 0`）を入れ替えてください。

---

## 5. かんたんトラブルシュート

| 症状 | 対処 |
| --- | --- |
| `mpremote devs` に出てこない | USB ケーブル（データ通信対応か）/ ドライバ / 別ポートを確認 |
| `could not enter raw repl` | 他アプリ（UIFlow, シリアルモニタ等）がポート占有していないか確認 |
| 値が常に 0 / 65535 | 配線（黄=G9, 5V, GND）と挿しているポートが PORT.B か確認 |
| LED が光らない | LED モジュールの向き・極性、PORT.B 接続を確認 |
| 距離が常に「範囲外」 | センサー前方に対象があるか、`TIMEOUT_US` を確認 |

---

### 対象部品（Level1：10項目）

Water Sensor / Light Sensor v1.2 / Magnetic Switch / DHT11 /
Red LED / Blue LED / Moisture Sensor / Mini PIR Motion Sensor /
Loudness Sensor / Ultrasonic Ranger
