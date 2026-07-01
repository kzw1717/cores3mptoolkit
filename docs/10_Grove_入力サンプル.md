# Grove 入力モジュール サンプル解説

Grove Creator Kit の **入力（センサー／スイッチ）モジュール**を CoreS3 で読み取る
サンプルの解説です。各行のリンクから実際の `.py` を開けます。
作りたいプログラムに合わせて、必要なスクリプトをコピー＆ペーストして使ってください。

## 共通事項

- **接続ポート**：すべて **PORT.B（黒）**。
- **信号ピンは G8**：本キットの Level1 モジュールは、Port.B の **G8**（`SIG_PIN = 8`）に信号が出ます。
  （Grove コネクタは信号線が2本あり Port.B では G8/G9 に配線されますが、本キットは全モジュール G8 側です。）
- **ケーブル色**：黒=GND / 赤=5V（信号ピンはコード上 `Pin(8)` を使用）。
- **実行**：PC と USB 接続し、`python -m mpremote run ファイル名.py`（VSCode は対象を開いて `Ctrl+Shift+B`）。
- **停止**：PC 側ターミナルで `Ctrl-C`。
- **画面/ターミナルの文字は英語**：実機では `print()` に日本語を渡すと出力が止まるため、サンプルの表示はすべて英語です。
- アナログ系はしきい値・係数を実機で校正してください（環境・個体で値が変わります）。

---

## 入力サンプル一覧

難易度は **Python 初心者の大学1年生**を対象に、5段階（**1=一番簡単 〜 5=一番難しい**）で示しています。

| 番号 | 難易度 | サンプル（.py へのリンク） | SKU | Product Name | 信号 | 動作の概要 |
| :---: | :---: | --- | --- | --- | --- | --- |
| IG1 | 1 | [tilt_switch.py](../Level1_samples/tilt_switch.py) | 111020063 | Grove - Tilt Switch | デジタル | 傾きで ON/OFF |
| IG2 | 1 | [touch_sensor.py](../Level1_samples/touch_sensor.py) | 101020746 | Grove - Touch Sensor | デジタル | 触れると `touched` |
| IG3 | 2 | [moisture_sensor.py](../Level1_samples/moisture_sensor.py) | 101020740 | Grove - Moisture Sensor | アナログ(ADC) | 土壌水分値を表示 |
| IG4 | 2 | [light_sensor.py](../Level1_samples/light_sensor.py) | 101020736 | Grove - Light Sensor v1.2 | アナログ(ADC) | 明るさを 0–65535 で表示 |
| IG5 | 3 | [water_sensor.py](../Level1_samples/water_sensor.py) | 101020733 | Grove - Water Sensor | アナログ(ADC) | しきい値で `WET`/`dry` |
| IG6 | 3 | [sound_sensor.py](../Level1_samples/sound_sensor.py) | 101020735 | Grove - Sound Sensor | アナログ(ADC) | 音量（振幅）を表示 |
| IG7 | 4 | [temperature_sensor.py](../Level1_samples/temperature_sensor.py) | 101020732 | Grove - Temperature Sensor | アナログ(ADC) | 温度[℃]を表示 |
| IG8 | 5 | [ultrasonic_ranger.py](../Level1_samples/ultrasonic_ranger.py) | 101020743 | Grove - Ultrasonic Ranger | デジタル(単線) | 距離[cm]を表示 |

---

## 各サンプルの解説

難易度の低い順に並べています。各見出しのリンクから `.py` を開けます。

### IG1. [tilt_switch.py](../Level1_samples/tilt_switch.py) ── 傾きスイッチ（難易度1）

傾き（姿勢）でオン/オフが切り替わる部品です。デジタル入力（ON/OFF）の一番やさしい例です。

```python
tilt = Pin(8, Pin.IN)          # 入力に設定（PORT.B 信号=G8）
if tilt.value() == 1:          # 1=傾き検知 / 0=水平
    print("ON  : tilt detected")
else:
    print("off : level")
```

ポイント：`Pin(8, Pin.IN)` の `value()` が 0/1 を返すだけです。多くの「スイッチ系」入力の基本形です。

### IG2. [touch_sensor.py](../Level1_samples/touch_sensor.py) ── タッチセンサー（難易度1）

指で触れる（近づける）と反応する静電容量式のセンサーです。押し込む必要がありません。

```python
touch = Pin(8, Pin.IN)         # PORT.B 信号=G8
if touch.value() == 1:         # 1=タッチあり / 0=なし
    print("TOUCH : touched")
else:
    print("-     : no touch")
```

ポイント：コードは傾きスイッチと同じ形です。物理ボタンの置き換え（非接触ボタン）に使えます。

### IG3. [moisture_sensor.py](../Level1_samples/moisture_sensor.py) ── 土壌水分センサー（難易度2）

土の水分量を **数値（0〜65535）** で読みます。キット付属スケッチと同じく、1秒ごとに値を表示するだけの素直な形です。

```python
moisture = ADC(Pin(8))         # PORT.B 信号=G8
moisture.atten(ADC.ATTN_11DB)  # 0〜3.3V を測れるようにする
value = moisture.read_u16()    # 0〜65535
print("Moisture =", value)
```

ポイント：`atten(ADC.ATTN_11DB)` と `read_u16()` がアナログ読み取りの定番です。乾いた土・湿った土で値を見て、必要なら自分でしきい値判定を足せます。

### IG4. [light_sensor.py](../Level1_samples/light_sensor.py) ── 明るさセンサー（難易度2）

明るさを **数値（0〜65535）** で読みます。コードは土壌水分センサーとほぼ同じで、明るいほど値が大きくなります。

```python
light = ADC(Pin(8))            # PORT.B 信号=G8
light.atten(ADC.ATTN_11DB)
value = light.read_u16()       # 0〜65535（明るいほど大）
print("light:", value)
```

ポイント：**部品が変わってもアナログ読み取りのコードはほぼ同じ**です。明るさ・音量・水分量はこの型を使い回せます。

### IG5. [water_sensor.py](../Level1_samples/water_sensor.py) ── 水検知センサー（難易度3）

水や水滴があると値が下がります。読んだアナログ値を **しきい値**と比べて `WET`/`dry` を判定します。

```python
WET_THRESHOLD = 60000          # この値より小さければ「水あり」（要校正）
value = adc.read_u16()         # 乾燥で最大付近、水ありで低下
if value < WET_THRESHOLD:
    print("water:", value, "(WET)")
else:
    print("water:", value, "(dry)")
```

ポイント：アナログ値＋しきい値判定の練習になります。本センサは 5V 動作で変化幅が小さいため、`WET_THRESHOLD` は実機で無水値と有水値の中間に校正してください（実測例：無水≒65535 / 有水≒54000 → 60000）。

### IG6. [sound_sensor.py](../Level1_samples/sound_sensor.py) ── 音量センサー（難易度3）

音の波形（交流）を短時間に高速サンプリングし、**最大値−最小値（振幅）**を音量の目安として求めます。

```python
lo, hi = 65535, 0
for i in range(500):           # 窓の中を高速に読み、最小と最大を記録
    v = adc.read_u16()
    if v < lo: lo = v
    if v > hi: hi = v
level = hi - lo                # 振幅（最大−最小）＝音量の目安
print("sound:", level)
```

ポイント：交流波形は平均するとほぼ一定になってしまうため、**振幅（最大−最小）**で音量を捉えます。無音で小さい値、声や拍手で大きい値になります。

### IG7. [temperature_sensor.py](../Level1_samples/temperature_sensor.py) ── 温度センサー（難易度4）

サーミスタ（温度で抵抗が変わる素子）の電圧を読み、計算式で温度[℃]に換算します。

```python
v = adc.read_u16() / 65535 * VREF     # ADCで測った実電圧（VREF≈3.05）
R = R0 * (VCC - v) / v                 # サーミスタ抵抗（VCC=5.0, R0=10kΩ）
tempC = 1.0 / (math.log(R / R0) / B + 1.0 / 298.15) - 273.15
print("temp: {:.1f} C".format(tempC))
```

ポイント：`import math` と `math.log` を使う数値計算のサンプルです。本センサは 5V 動作だが CoreS3 の ADC 基準は約 3.3V のため、実電圧を求めて電源 5V を別扱いにするのがコツです。表示が実温とずれたら `VREF` を微調整します（詳細は[発展編](31_M5Stack実装に向けたPython入門2_発展編.md)）。

### IG8. [ultrasonic_ranger.py](../Level1_samples/ultrasonic_ranger.py) ── 超音波距離センサー（難易度5）

1本の信号線で「トリガ送信」と「エコー受信」の両方を行うため、**ピンの入出力を
切り替え**ながらパルス幅を測り、距離[cm]に換算します。最も応用的なサンプルです。

```python
p = Pin(8, Pin.OUT)            # 送信時は出力
# ... 10us のトリガを出す ...
p = Pin(8, Pin.IN)            # 受信時は入力に切替
dur = time_pulse_us(p, 1, 30000)  # エコーのパルス幅[us]を測る
distance_cm = dur / 58.0          # 距離に換算
```

ポイント：ピンの向き切替・`time_pulse_us()`・タイムアウト・単位換算と要素が多く、
まとめて理解できると応用力がつきます。

---

## 入力モジュールの使い方のポイント

### デジタル入力（ON/OFF を読む）

`tilt_switch` / `touch_sensor` は基本形が同じで、`Pin(8, Pin.IN)` の `value()` が 0/1 を
返すだけです。判定したい論理に合わせて `== 1` / `== 0` を入れ替えれば、多くの「検知系」
入力に流用できます。

```python
from machine import Pin
import time
p = Pin(8, Pin.IN)        # PORT.B 信号=G8
while True:
    print(p.value())      # 0 か 1
    time.sleep(0.2)
```

### アナログ入力（強さを数値で読む）

`moisture_sensor` / `light_sensor` / `water_sensor` / `sound_sensor` は ADC で 0–65535 の
数値を読みます。**部品を変えてもコードの土台はほぼ同じ**です。

```python
from machine import Pin, ADC
adc = ADC(Pin(8))             # PORT.B 信号=G8
adc.atten(ADC.ATTN_11DB)      # 0-3.3V を測れるようにする
print(adc.read_u16())         # 0-65535
```

- そのまま値を使う：`moisture` / `light`
- **しきい値**で判定する：`water`（`value < WET_THRESHOLD` で WET）
- **振幅**で捉える：`sound`（一定回数読んで 最大−最小）

### 専用処理が要るもの

- **temperature_sensor.py**：アナログ値を電圧に直し、サーミスタの式（`math.log`）で温度に換算します。5V 動作×ADC 基準 3.3V のズレを補正するのがポイント。
- **ultrasonic_ranger.py**：1本の信号線でトリガ送信とエコー受信を行うため、ピンの入出力を切り替えて `time_pulse_us()` でパルス幅を測ります。

---

→ 出力モジュールは [11_Grove_出力サンプル.md](11_Grove_出力サンプル.md) を参照。
