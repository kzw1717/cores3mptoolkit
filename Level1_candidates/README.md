# Level1 候補サンプル（動作チェック用）

Level1 を確定する前の**検証用フォルダ**です。ここのスクリプトは
`GroveCreaterKit.xlsx` の Level1 候補（15モジュール）に対応し、いずれも
`res/Grove-Creator-Kit-ganma.pdf` の Arduino スケッチを基に**標準MicroPython**へ移植しています。

> このフォルダは検証専用です。動作確認が済むまで、本番の `Level1_samples/` や docs、
> 番号(IG/OG)、教材分析ファイルは変更しません。

## チェック方法

各スクリプトを、対応する Grove モジュールを **PORT.B（黄=G9）** に挿してから実行します。

```bat
python -m mpremote run <ファイル名>.py
```

停止は PC 側ターミナルで `Ctrl-C`。出力（またはモジュールの動作）が想定どおりかを
下の表の「結果」に ○/× で記入してください。× のものは Level1 から外すか、原因を調べて修正します。

## 入力（12）

| 結果 | ファイル | モジュール | 期待する動作 | 備考 |
| :--: | --- | --- | --- | --- |
|  | `tilt_switch.py` | Tilt Switch | 傾けると `ON`、水平で `off` | デジタル入力 |
| （既存） | `water_sensor.py` | Water Sensor | 濡らすと `WET`、乾くと `dry` | 水検知で 0 |
|  | `switch_p.py` | Switch(P) | スライドで `ON`/`off` | デジタル入力 |
| （既存） | `light_sensor.py` | Light Sensor v1.2 | 明暗で数値が変化 | アナログ(ADC) |
|  | `sound_sensor.py` | Sound Sensor | 音で数値が変化（32回平均） | アナログ(ADC) |
|  | `rotary_angle_sensor.py` | Rotary Angle Sensor | 回すと角度 0〜300度が変化 | アナログ(ADC) |
| （既存） | `dht11.py` | 温湿度 (DHT11) | 温度[℃]・湿度[%]を表示 | `dht` 標準搭載 |
|  | `temperature_sensor.py` | Temperature Sensor | 温度[℃]を表示 | **要校正**：B=3975/R0=10kΩ |
| （既存） | `moisture_sensor.py` | Moisture Sensor | 湿らせると数値が変化 | アナログ(ADC) |
| （既存） | `pir_motion_sensor.py` | Mini PIR Motion | 動くと `MOTION` | 起動直後は数十秒安定待ち |
|  | `button.py` | Button | 押すと `PRESSED` | デジタル入力 |
| （既存） | `ultrasonic_ranger.py` | Ultrasonic Ranger | 距離[cm]を表示 | 単線SIG |

## 出力（3）

| 結果 | ファイル | モジュール | 期待する動作 | 備考 |
| :--: | --- | --- | --- | --- |
| （既存） | `red_led.py` | Red LED | 0.5秒ごとに点滅 | デジタル出力 |
| （既存） | `blue_led.py` | Blue LED | 0.5秒ごとに点滅 | デジタル出力 |
|  | `vibration_motor.py` | Vibration Motor | 1秒ごとに振動/停止 | デジタル出力 |

「（既存）」は現行 `Level1_samples/` から継続（PDFスケッチと論理一致を確認済み）。無印の7本が新規です。

## チェック時の注意

- **アナログ系**（light / sound / rotary / moisture / temperature）は環境で値が変わります。数値が**動く**ことを確認できればOKです。
- **temperature_sensor.py**：表示℃が実温度とずれる場合、ファイル先頭の `B`（B定数）と `R0`（基準抵抗）を実測で調整してください。
- **water_sensor.py**：水検知で値が 0（WET）になります。逆になる場合は配線・個体差を確認。
- 値が常に 0 / 65535 で動かない、`could not enter raw repl` などが出る場合は、配線（黄=G9・5V・GND）と PORT.B か、他アプリのポート占有を確認してください。

## この後の流れ

1. 上記の実機チェックで ○/× を確定。
2. ○ のものだけで **Level1 を確定**（× は除外または修正）。
3. 確定後に、本番反映（`Level1_samples/` へ移動 → 番号 IG/OG 再採番 → docs・README・教材分析xlsx 更新 → コミット）を一括で行います。
