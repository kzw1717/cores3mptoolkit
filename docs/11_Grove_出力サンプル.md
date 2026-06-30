# Grove 出力モジュール サンプル解説

Grove Creator Kit の **出力（アクチュエータ／表示）モジュール**を CoreS3 から
制御するサンプルの解説です。各リンクから `.py` を開けます。

## 共通事項

- **接続ポート**：**PORT.B（黒）**。信号は **黄線＝G9**。
- **ケーブル色**：黒=GND / 赤=5V / 黄=信号(主) / 白=信号(副)。
- **実行**：`mpremote run ファイル名.py`（VSCode は対象を開いて `Ctrl+Shift+B`）。
- **停止**：PC 側ターミナルで `Ctrl-C`。

---

## 出力サンプル一覧

難易度は **Python 初心者の大学1年生**を対象に、5段階（**1=一番簡単 〜 5=一番難しい**）で示しています。

| 番号 | 難易度 | サンプル（.py へのリンク） | SKU | Product Name | 信号 | 動作の概要 |
| :---: | :---: | --- | --- | --- | --- | --- |
| OG1 | 1 | [red_led.py](../Level1_samples/red_led.py) | 104030005 | Grove - Red LED | デジタル | 赤 LED を 0.5 秒ごとに点滅 |
| OG2 | 1 | [blue_led.py](../Level1_samples/blue_led.py) | 104030010 | Grove - Blue LED | デジタル | 青 LED を 0.5 秒ごとに点滅 |

---

## 各サンプルの解説

### [red_led.py](../Level1_samples/red_led.py) ── 赤 LED（難易度1）

赤 LED を 0.5 秒ごとに点滅させます。デジタル出力（ON/OFF）の基本です。

```python
led = Pin(9, Pin.OUT)        # 出力に設定（PORT.B 黄=G9）
state = 1 - state            # 0 と 1 を交互に反転
led.value(state)             # 1=点灯 / 0=消灯
```

ポイント：`state = 1 - state` で点灯・消灯を交互に切り替えています。終了時（Ctrl-C）には
`led.value(0)` で消灯してから終わるようにしています。

### [blue_led.py](../Level1_samples/blue_led.py) ── 青 LED（難易度1）

青 LED を点滅させます。コードは `red_led.py` と**同じ**で、挿す LED が違うだけです。

```python
led = Pin(9, Pin.OUT)
led.value(1)   # 点灯
led.value(0)   # 消灯
```

ポイント：出力モジュールは「色や部品が変わっても ON/OFF のコードは同じ」です。
LED を Relay（リレー）や Vibration Motor に替えても、この形がそのまま使えます。

---

## 出力モジュールの使い方のポイント

### デジタル出力（ON/OFF で光らせる・動かす）

LED は `Pin(9, Pin.OUT)` の `value(1)` で点灯、`value(0)` で消灯する基本形です。
**この型は、Relay（リレー）/ Buzzer / Vibration Motor など他の出力モジュールにも
ほぼそのまま流用できます**（鳴らす・回す・スイッチする、はすべて同じ「ON/OFF 出力」です）。

```python
from machine import Pin
import time
out = Pin(9, Pin.OUT)     # PORT.B 黄=G9
while True:
    out.value(1); time.sleep(0.5)   # ON
    out.value(0); time.sleep(0.5)   # OFF
```

### 発展（PWM で強さ・音程を変える）

ブザーやスピーカー、明るさ調整をしたいときは PWM を使います。

```python
from machine import Pin, PWM
buz = PWM(Pin(9))
buz.freq(2000)          # 周波数 [Hz]（音程）
buz.duty_u16(32768)     # デューティ（強さ）。0 で停止
```

> **メモ**：現在の Level1 では出力サンプルは LED 2 種です。今後 Buzzer / Relay /
> Speaker などを追加する場合も、上記「デジタル出力」「PWM 出力」の型を流用できます。

---

## チャレンジ課題：入力＋出力の 2 モジュールを同時に使う（接続ポートの選び方）

センサー（入力）とLED等（出力）を**同時に**使うときは、2つを別々のポートに挿します。
**デジタル/PWM 出力は Port A・Port C どちらでも動く**ので、入力をアナログ向きの Port B に、
出力を Port A か Port C に割り当てるのが定番です。

| ポート | 黄線(信号:主) | 白線(信号:副) | 出力での注意 |
| --- | --- | --- | --- |
| PORT.A（赤） | G2 | G1 | I2Cモジュール（LCD/加速度/RTC等）を同じ Port A に挿すときは流用不可。挿さなければ通常GPIOとして使用可 |
| PORT.B（黒） | G9 | G8 | 標準。アナログ入力に最適 |
| PORT.C（青） | G17 | G18 | デジタル/PWM 出力は可。※ADC2 のためアナログ「入力」には不向き（出力なら無関係） |

補足：CoreS3 の内蔵 I2C（IMU/PMU/RTC 等）は G11/G12 の別系統なので、Port A（G1/G2）を
デジタル出力に使っても内蔵機能とは競合しません。

### 例：入力＝Port B、出力＝Port A

サンプルの**ピン番号を挿したポートの黄線に合わせて変える**だけです。

```python
from machine import Pin, ADC
import time

sensor = ADC(Pin(9)); sensor.atten(ADC.ATTN_11DB)  # 入力: PORT.B 黄=G9
led = Pin(2, Pin.OUT)                                # 出力: PORT.A 黄=G2
# 出力を PORT.C に挿すなら led = Pin(17, Pin.OUT)   # PORT.C 黄=G17

while True:
    if sensor.read_u16() > 30000:   # しきい値は実機で校正
        led.value(1)
    else:
        led.value(0)
    time.sleep(0.1)
```

> ポート別の黄線（信号:主）：**A=G2 / B=G9 / C=G17**。
> 出力サンプル（`red_led.py` など）の `Pin(9, ...)` を、挿したポートの番号に置き換えれば、そのまま動きます。

---

→ 入力モジュールは [10_Grove_入力サンプル.md](10_Grove_入力サンプル.md) を参照。
