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

| サンプル（.py へのリンク） | 部品 | 信号 | 動作の概要 |
| --- | --- | --- | --- |
| [red_led.py](../Level1_samples/red_led.py) | Red LED | デジタル | 赤 LED を 0.5 秒ごとに点滅 |
| [blue_led.py](../Level1_samples/blue_led.py) | Blue LED | デジタル | 青 LED を 0.5 秒ごとに点滅 |

---

## 要点

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

→ 入力モジュールは [10_Grove_入力サンプル.md](10_Grove_入力サンプル.md) を参照。
