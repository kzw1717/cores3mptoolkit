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

| サンプル（.py へのリンク） | 部品 | 信号 | 動作の概要 |
| --- | --- | --- | --- |
| [water_sensor.py](../Level1_samples/water_sensor.py) | Water Sensor | デジタル | 水検知で `WET`、乾燥で `dry` |
| [light_sensor.py](../Level1_samples/light_sensor.py) | Light Sensor v1.2 | アナログ(ADC) | 明るさを 0–65535 で表示 |
| [magnetic_switch.py](../Level1_samples/magnetic_switch.py) | Magnetic Switch | デジタル | 磁石の接近を検知 |
| [dht11.py](../Level1_samples/dht11.py) | 温湿度センサー DHT11 | デジタル(1線) | 温度[℃]・湿度[%]を表示 |
| [moisture_sensor.py](../Level1_samples/moisture_sensor.py) | Moisture Sensor | アナログ(ADC) | 土壌水分値と WET/dry |
| [pir_motion_sensor.py](../Level1_samples/pir_motion_sensor.py) | Mini PIR Motion | デジタル | 動きを検知すると `MOTION` |
| [loudness_sensor.py](../Level1_samples/loudness_sensor.py) | Loudness Sensor | アナログ(ADC) | 音量を 0–65535 で表示 |
| [ultrasonic_ranger.py](../Level1_samples/ultrasonic_ranger.py) | Ultrasonic Ranger | デジタル(単線) | 距離[cm]を表示 |

---

## それぞれの要点

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
