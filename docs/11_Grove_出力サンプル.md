# Grove 出力モジュール サンプル解説

Grove Creator Kit の **出力（アクチュエータ／表示）モジュール**を CoreS3 から
制御するサンプルの解説です。各リンクから `.py` を開けます。

## 共通事項

- **接続ポート**：**PORT.B（黒）**。
- **信号ピンは G8**：本キットの Level1 モジュールは、Port.B の **G8**（`SIG_PIN = 8`）で制御します。
- **ケーブル色**：黒=GND / 赤=5V（信号ピンはコード上 `Pin(8)` を使用）。
- **実行**：`python -m mpremote run ファイル名.py`（VSCode は対象を開いて `Ctrl+Shift+B`）。
- **停止（重要）**：出力（アクチュエータ）系は `Ctrl-C` だけでは止まらないことがあります。
  `python -m mpremote run` の Ctrl-C は PC 側の mpremote が終了するだけで、**デバイス上の
  ループは動き続け、GPIO も最後の状態を保持**するため、LED が点滅し続けたりモーターが
  回り続けたりします。**確実に止めるには CoreS3 本体のリセットボタン、または別ターミナルで
  `python -m mpremote reset`（ソフトリセット）**を実行してください（USB 抜き差しでも停止）。
- **表示の文字は英語**：実機では `print()` に日本語を渡すと出力が止まるため、表示は英語です。

---

## 出力サンプル一覧

難易度は **Python 初心者の大学1年生**を対象に、5段階（**1=一番簡単 〜 5=一番難しい**）で示しています。

| 番号 | 難易度 | サンプル（.py へのリンク） | SKU | Product Name | 信号 | 動作の概要 |
| :---: | :---: | --- | --- | --- | --- | --- |
| OG1 | 1 | [red_led.py](../Level1_samples/red_led.py) | 104020195 | Grove - Red LED | デジタル | 赤 LED を 0.5 秒ごとに点滅 |
| OG2 | 1 | [blue_led.py](../Level1_samples/blue_led.py) | 104020196 | Grove - Blue LED | デジタル | 青 LED を 0.5 秒ごとに点滅 |
| OG3 | 2 | [vibration_motor.py](../Level1_samples/vibration_motor.py) | 108020121 | Grove - Vibration Motor | デジタル | モーターを 1 秒ごとに振動/停止 |

---

## 各サンプルの解説

### OG1. [red_led.py](../Level1_samples/red_led.py) ── 赤 LED（難易度1）

赤 LED を 0.5 秒ごとに点滅させます。デジタル出力（ON/OFF）の基本です。
「点灯 → 待つ → 消灯 → 待つ」を `while` で繰り返すだけの、いちばんやさしい形です。

```python
led = Pin(8, Pin.OUT)     # 出力に設定（PORT.B 信号=G8）

def loop():
    led.value(1)          # 1 で点灯
    print("LED: ON")
    time.sleep(0.5)
    led.value(0)          # 0 で消灯
    print("LED: off")
    time.sleep(0.5)
```

ポイント：`value(1)` で点灯、`value(0)` で消灯し、`time.sleep` で待つだけです。
[入門編](30_M5Stack実装に向けたPython入門.md)の知識（import・メソッド呼び出し・try/except）と
入門I の基礎だけで読めます。**停止は本体リセット or `python -m mpremote reset`**（共通事項参照）。

### OG2. [blue_led.py](../Level1_samples/blue_led.py) ── 青 LED（難易度1）

青 LED を点滅させます。コードは `red_led.py` と**同じ**で、挿す LED が違うだけです。

```python
led = Pin(8, Pin.OUT)
led.value(1)   # 点灯
time.sleep(0.5)
led.value(0)   # 消灯
time.sleep(0.5)
```

ポイント：出力モジュールは「色や部品が変わっても ON/OFF のコードは同じ」です。
LED を Vibration Motor に替えても、この形がそのまま使えます。

### OG3. [vibration_motor.py](../Level1_samples/vibration_motor.py) ── 振動モーター（難易度2）

小型のバイブレーションモーターを 1 秒ごとに振動/停止させます。コードは LED と同じ
「`value(1)` で ON、`value(0)` で OFF」ですが、**アクチュエータ（動く出力）**なので
止め方に注意が必要です。

```python
motor = Pin(8, Pin.OUT)   # PORT.B 信号=G8

def loop():
    motor.value(1)        # 振動
    print("VIB : vibrating")
    time.sleep(1.0)
    motor.value(0)        # 停止
    print("--- : stopped")
    time.sleep(1.0)
```

ポイント：LED と同じ ON/OFF 出力ですが、**`Ctrl-C` では止まらず回り続けることがある**ため、
確実に止めるには**本体リセットボタン or `python -m mpremote reset`**を使います（共通事項参照）。
終了処理（Ctrl-C が届いたとき）では `motor.value(0)` で停止してから終わります。

---

## 出力モジュールの使い方のポイント

### デジタル出力（ON/OFF で光らせる・動かす）

LED やモーターは `Pin(8, Pin.OUT)` の `value(1)` で ON、`value(0)` で OFF する基本形です。
**この型は、LED / Vibration Motor / Relay / Buzzer など多くの出力モジュールに
そのまま流用できます**（光らせる・回す・鳴らす、はすべて同じ「ON/OFF 出力」です）。

```python
from machine import Pin
import time
out = Pin(8, Pin.OUT)     # PORT.B 信号=G8
while True:
    out.value(1); time.sleep(0.5)   # ON
    out.value(0); time.sleep(0.5)   # OFF
```

### 発展（PWM で強さ・音程を変える）

ブザーやスピーカー、明るさ調整をしたいときは PWM を使います。

```python
from machine import Pin, PWM
buz = PWM(Pin(8))
buz.freq(2000)          # 周波数 [Hz]（音程）
buz.duty_u16(32768)     # デューティ（強さ）。0 で停止
```

> **メモ**：現在の Level1 の出力サンプルは LED 2 種と振動モーターです。今後 Buzzer / Relay /
> Speaker などを追加する場合も、上記「デジタル出力」「PWM 出力」の型を流用できます。

---

## チャレンジ課題：入力＋出力の 2 モジュールを同時に使う（接続ポートの選び方）

センサー（入力）とLED等（出力）を**同時に**使うときは、2つを別々のポートに挿します。
入力をアナログ向きの Port B に、出力をもう一方のポート（Port A か Port C）に割り当てるのが定番です。

| ポート | 信号に使える GPIO | 補足 |
| --- | --- | --- |
| PORT.A（赤） | G1 / G2 | I2Cモジュール（LCD/加速度/RTC等）を同じ Port A に挿すときは流用不可。挿さなければ通常GPIOとして使用可 |
| PORT.B（黒） | G8 / G9 | 標準。アナログ入力に最適。**本キットのモジュールは G8 側** |
| PORT.C（青） | G17 / G18 | デジタル/PWM 出力は可。※ADC2 のためアナログ「入力」には不向き（出力なら無関係） |

> **重要**：Grove コネクタは信号線が2本あり、どちらの GPIO に信号が出るかは**モジュールによって
> 異なります**。本キットの Port.B モジュールはすべて **G8** でした。別ポート（A/C）に挿し替える
> ときは、**そのポートの2つの GPIO のうちどちらで動くかを実機で確認**してください（片方で動かな
> ければもう片方を試す）。

### 例：入力＝Port B（G8）、出力＝Port A

サンプルの**ピン番号を、挿したポートで実際に動く GPIO に合わせて変える**だけです。

```python
from machine import Pin, ADC
import time

sensor = ADC(Pin(8)); sensor.atten(ADC.ATTN_11DB)  # 入力: PORT.B 信号=G8
led = Pin(1, Pin.OUT)                                # 出力: PORT.A（G1 で動かなければ G2 を試す）

while True:
    if sensor.read_u16() > 30000:   # しきい値は実機で校正
        led.value(1)
    else:
        led.value(0)
    time.sleep(0.1)
```

> ポート別の信号 GPIO は 2 本のどちらか（A=G1/G2 · B=G8/G9 · C=G17/G18）。
> サンプルの `Pin(8, ...)` を、挿したポートで実際に動く番号に置き換えれば、そのまま動きます。

---

→ 入力モジュールは [10_Grove_入力サンプル.md](10_Grove_入力サンプル.md) を参照。
