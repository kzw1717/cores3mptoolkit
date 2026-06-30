# Grove 入力モジュール サンプル解説

Grove Creator Kit の **入力（センサー／スイッチ）モジュール**を CoreS3 で読み取る
サンプルの解説です。各行のリンクから実際の `.py` を開けます。
作りたいプログラムに合わせて、必要なスクリプトをコピー＆ペーストして使ってください。

## 共通事項

- **接続ポート**：すべて **PORT.B（黒）**。信号は **黄線＝G9**（一部は白線＝G8 も使用）。
- **ケーブル色**：黒=GND / 赤=5V / 黄=信号(主) / 白=信号(副)。
- **実行**：PC と USB 接続し、`mpremote run ファイル名.py`（VSCode は対象を開いて `Ctrl+Shift+B`）。
- **停止**：PC 側ターミナルで `Ctrl-C`。
- アナログ系はしきい値を実機で校正してください（環境で値が変わります）。

---

## 入力サンプル一覧

難易度は **Python 初心者の大学1年生**を対象に、5段階（**1=一番簡単 〜 5=一番難しい**）で示しています。

| 番号 | 難易度 | サンプル（.py へのリンク） | SKU | Product Name | 信号 | 動作の概要 |
| :---: | :---: | --- | --- | --- | --- | --- |
| IG1 | 1 | [magnetic_switch.py](../Level1_samples/magnetic_switch.py) | 101020038 | Grove - Magnetic Switch | デジタル | 磁石の接近を検知 |
| IG2 | 2 | [water_sensor.py](../Level1_samples/water_sensor.py) | 101020018 | Grove - Water Sensor | デジタル | 水検知で `WET`、乾燥で `dry` |
| IG3 | 2 | [pir_motion_sensor.py](../Level1_samples/pir_motion_sensor.py) | 101020353 | Grove - Mini PIR Motion Sensor | デジタル | 動きを検知すると `MOTION` |
| IG4 | 2 | [light_sensor.py](../Level1_samples/light_sensor.py) | 101020132 | Grove - Light Sensor v1.2 | アナログ(ADC) | 明るさを 0–65535 で表示 |
| IG5 | 2 | [loudness_sensor.py](../Level1_samples/loudness_sensor.py) | 101020063 | Grove - Loudness Sensor | アナログ(ADC) | 音量を 0–65535 で表示 |
| IG6 | 3 | [moisture_sensor.py](../Level1_samples/moisture_sensor.py) | 101020008 | Grove - Moisture Sensor | アナログ(ADC) | 土壌水分値と WET/dry |
| IG7 | 3 | [dht11.py](../Level1_samples/dht11.py) | 101020011 | Grove - Temperature & Humidity Sensor (DHT11) | デジタル(1線) | 温度[℃]・湿度[%]を表示 |
| IG8 | 5 | [ultrasonic_ranger.py](../Level1_samples/ultrasonic_ranger.py) | 101020010 | Grove - Ultrasonic Ranger | デジタル(単線) | 距離[cm]を表示 |

---

## 各サンプルの解説

難易度の低い順に並べています。各見出しのリンクから `.py` を開けます。

### 1. [magnetic_switch.py](../Level1_samples/magnetic_switch.py) ── 磁気スイッチ（難易度1）

磁石が近づくとスイッチが入る部品です。デジタル入力（ON/OFF）の一番やさしい例です。

```python
magnet = Pin(9, Pin.IN, Pin.PULL_DOWN)   # 入力に設定
if magnet.value() == 1:                   # 1=検知 / 0=なし
    print("MAGNET : 磁石を検知しました")
```

ポイント：`Pin.PULL_DOWN`（内部プルダウン）を付けると、何もないときの値が 0 に安定します。

### 2. [water_sensor.py](../Level1_samples/water_sensor.py) ── 水検知センサー（難易度2）

水や水滴があると反応します。**検知すると値が 0（LOW）**になる点に注意が必要です。

```python
water = Pin(9, Pin.IN, Pin.PULL_UP)   # オープンコレクタ出力なのでプルアップ
if water.value() == 0:                 # 0=水あり / 1=乾燥
    print("WET : 水を検知しました")
```

ポイント：磁気スイッチと逆で「0 が検知」です。`Pin.PULL_UP` を使います。

### 2. [pir_motion_sensor.py](../Level1_samples/pir_motion_sensor.py) ── 人感（動き）センサー（難易度2）

人や動物の動きを検知すると 1 になります。検知したときだけメッセージを出します。

```python
pir = Pin(9, Pin.IN)
if pir.value() == 1:
    print("MOTION : 動きを検知しました")
```

ポイント：電源投入直後はセンサーが安定するまで数十秒かかることがあります。

### 2. [light_sensor.py](../Level1_samples/light_sensor.py) ── 明るさセンサー（難易度2）

明るさを **数値（0〜65535）** で読みます。アナログ入力（ADC）の基本形です。

```python
light = ADC(Pin(9))
light.atten(ADC.ATTN_11DB)     # 0〜3.3V を測れるようにする
value = light.read_u16()       # 0〜65535
```

ポイント：`atten(ADC.ATTN_11DB)` と `read_u16()` の組み合わせがアナログ読み取りの定番です。

### 2. [loudness_sensor.py](../Level1_samples/loudness_sensor.py) ── 音量センサー（難易度2）

周囲の音の大きさを数値で読みます。コードは明るさセンサーとほぼ同じです。

```python
sound = ADC(Pin(9))
sound.atten(ADC.ATTN_11DB)
value = sound.read_u16()       # 0〜65535
```

ポイント：瞬間的な音を捉えたいときは `INTERVAL`（読み取り間隔）をさらに短くします。

### 3. [moisture_sensor.py](../Level1_samples/moisture_sensor.py) ── 土壌水分センサー（難易度3）

土の水分量をアナログで読み、**しきい値**と比べて WET / dry を判定します。

```python
WET_LEVEL = 30000              # この値以上で「湿っている」と判定（要調整）
value = moisture.read_u16()
state = "WET" if value >= WET_LEVEL else "dry"
```

ポイント：アナログ値＋しきい値判定の練習になります。`WET_LEVEL` は実機で校正してください。

### 3. [dht11.py](../Level1_samples/dht11.py) ── 温湿度センサー DHT11（難易度3）

温度と湿度を**専用ライブラリ**でまとめて読みます。

```python
import dht
sensor = dht.DHT11(Pin(9))
sensor.measure()                       # 計測を実行
print(sensor.temperature(), sensor.humidity())
```

ポイント：`dht` は MicroPython 標準搭載で追加導入不要。読み取りは **2秒以上の間隔**が必要で、
失敗に備えて `try / except OSError` で囲んでいます。

### 5. [ultrasonic_ranger.py](../Level1_samples/ultrasonic_ranger.py) ── 超音波距離センサー（難易度5）

1本の信号線で「トリガ送信」と「エコー受信」の両方を行うため、**ピンの入出力を
切り替え**ながらパルス幅を測り、距離[cm]に換算します。最も応用的なサンプルです。

```python
p = Pin(9, Pin.OUT)            # 送信時は出力
# ... 10us のトリガを出す ...
p = Pin(9, Pin.IN)            # 受信時は入力に切替
dur = time_pulse_us(p, 1, 30000)  # エコーのパルス幅[us]を測る
distance_cm = dur / 58.0          # 距離に換算
```

ポイント：ピンの向き切替・`time_pulse_us()`・タイムアウト・単位換算と要素が多く、
まとめて理解できると応用力がつきます。

---

## 入力モジュールの使い方のポイント

### デジタル入力（ON/OFF を読む）

`water_sensor` / `magnetic_switch` / `pir_motion_sensor` は基本形が同じで、
`Pin(9, Pin.IN)` の `value()` が 0/1 を返すだけです。判定したい論理に合わせて
`== 1` / `== 0` を入れ替えれば、多くの「検知系」センサーに流用できます。

```python
from machine import Pin
import time
p = Pin(9, Pin.IN)        # PORT.B 黄=G9
while True:
    print(p.value())      # 0 か 1
    time.sleep(0.2)
```

### アナログ入力（強さを数値で読む）

`light_sensor` / `loudness_sensor` / `moisture_sensor` は ADC で 0–65535 の数値を読みます。
**部品を変えてもコードはほぼ同じ**なので、明るさ・音量・水分量はこの型を使い回せます。

```python
from machine import Pin, ADC
adc = ADC(Pin(9))             # PORT.B 黄=G9
adc.atten(ADC.ATTN_11DB)      # 0-3.3V を測れるようにする
print(adc.read_u16())         # 0-65535
```

### 専用処理が要るもの

- **dht11.py**：温度と湿度を同時に読む 1線式。MicroPython 標準の `dht` モジュールを使用（追加導入不要）。読み取りは 1 秒以上の間隔が必要。
- **ultrasonic_ranger.py**：1本の信号線でトリガ送信とエコー受信を行うため、ピンの入出力を切り替えて `time_pulse_us()` でパルス幅を測ります。

---

→ 出力モジュールは [11_Grove_出力サンプル.md](11_Grove_出力サンプル.md) を参照。
