# CoreS3 固有機能 入力サンプル解説

M5Stack CoreS3 の**本体内蔵機能（入力系）**を使うサンプルの解説です。
Grove と違い**配線は不要**で、UIFlow2 の **M5 ライブラリ**で簡潔に書けます。
各リンクから `.py` を開けます。

## 共通事項

- **接続**：不要（すべて本体内蔵）。
- **書き方**：`import M5` ＋ `from M5 import *`。`setup()` で `M5.begin()`、`loop()` で `M5.update()` を必ず呼ぶ。
- **実行**：`mpremote run ファイル名.py`（VSCode は対象を開いて `Ctrl+Shift+B`）。
- **停止**：PC 側ターミナルで `Ctrl-C`。

---

## 入力サンプル一覧

難易度は **Python 初心者の大学1年生**を対象に、5段階（**1=一番簡単 〜 5=一番難しい**）で示しています。

| 番号 | 難易度 | サンプル（.py へのリンク） | 機能（内蔵デバイス） | 動作の概要 |
| :---: | :---: | --- | --- | --- |
| IM1 | 2 | [touch_position.py](../m5stack_samples/touch_position.py) | タッチパネル（FT6336U） | 触れた座標 (x, y) を表示 |
| IM2 | 2 | [battery_status.py](../m5stack_samples/battery_status.py) | 電源管理（AXP2101） | 電池残量[%]・電圧[mV]・充電状態を表示 |
| IM3 | 3 | [imu_accel.py](../m5stack_samples/imu_accel.py) | IMU（BMI270：加速度＋ジャイロ） | 6軸の値を画面と端末に表示 |
| IM4 | 3 | [touch_counter.py](../m5stack_samples/touch_counter.py) | タッチパネル | 画面タッチ回数を表示 |
| IM5 | 4 | [touch_button_single.py](../m5stack_samples/touch_button_single.py) | タッチパネル | 1つのボタンを押した回数を表示 |
| IM6 | 4 | [touch_button_yesno.py](../m5stack_samples/touch_button_yesno.py) | タッチパネル | YES/NO 2ボタンの押下回数を表示 |

---

## 各サンプルの解説

難易度の低い順に並べています。各見出しのリンクから `.py` を開けます。

### IM1. [touch_position.py](../m5stack_samples/touch_position.py) ── タッチ座標（難易度2）

画面に触れた位置の座標 (x, y) を読んで表示します。タッチ入力の一番やさしい例です。

```python
if M5.Touch.getCount():        # 触れている点の数（0=触れていない）
    x = M5.Touch.getX()        # X 座標
    y = M5.Touch.getY()        # Y 座標
```

ポイント：`M5.begin()` と、ループ内の `M5.update()` を忘れるとタッチが更新されません。

### IM2. [battery_status.py](../m5stack_samples/battery_status.py) ── バッテリー状態（難易度2）

内蔵バッテリーの残量・電圧・充電中かどうかを読んで表示します。関数を呼んで値を受け取るだけです。

```python
level = Power.getBatteryLevel()    # 残量 [%] (0-100)
volt  = Power.getBatteryVoltage()  # 電圧 [mV]
charging = Power.isCharging()      # 充電中なら True
```

ポイント：USB 接続中は `charging` が True になります。残量表示や省電力の判断に使えます。

### IM3. [imu_accel.py](../m5stack_samples/imu_accel.py) ── IMU（加速度・ジャイロ）（難易度3）

本体の傾きや動きを、加速度・ジャイロの 6 個の数値として読みます。

```python
ax, ay, az = Imu.getAccel()    # 加速度 (x, y, z) [G]
gx, gy, gz = Imu.getGyro()     # 角速度 (x, y, z) [deg/s]
```

ポイント：戻り値は 3 個セットの**タプル**なので、`ax, ay, az = ...` の形で 3 変数に分けて
受け取ります（タプルの展開の練習になります）。

### IM4. [touch_counter.py](../m5stack_samples/touch_counter.py) ── タッチ回数カウンタ（難易度3）

画面のどこでもタッチすると、タッチした回数を数えて表示します。

```python
touching = M5.Touch.getCount() > 0
if touching and not prev_touching:    # 「無→有」に変わった瞬間だけ
    touch_count += 1                   # 1回ぶん数える
prev_touching = touching
```

ポイント：直前の状態 `prev_touching` と比べて「押した瞬間」だけ数えます。これをしないと
触れている間ずっと数え続けてしまいます（**立ち上がり検出**という考え方）。

### IM5. [touch_button_single.py](../m5stack_samples/touch_button_single.py) ── 1ボタン（難易度4）

画面にボタンを 1 つ描き、その上をタッチしたら所定の関数を実行して回数を表示します。

```python
def in_rect(px, py, rect):             # 点が四角形の中か判定
    x, y, w, h = rect
    return x <= px <= x + w and y <= py <= y + h

if touching and not prev_touching:
    if in_rect(M5.Touch.getX(), M5.Touch.getY(), BTN):
        on_button_pressed()            # ← ボタンが押されたときの処理
```

ポイント：「ボタンを描く」「座標が中か判定する」「押した瞬間だけ反応する」の 3 つを
組み合わせます。詳しくは下の[画面ボタン（タッチUI）](#画面ボタンタッチui)を参照。

### IM6. [touch_button_yesno.py](../m5stack_samples/touch_button_yesno.py) ── YES/NO 2ボタン（難易度4）

YES と NO の 2 つのボタンを描き、押した方に応じて別々の関数を実行します。

```python
if in_rect(x, y, YES_BTN):
    on_yes()
elif in_rect(x, y, NO_BTN):
    on_no()
```

ポイント：1ボタンの考え方をそのまま 2 個に増やしただけです。ボタンの座標と
呼び出す関数を足していけば、3 個以上にも応用できます。

---

## 入力モジュールの使い方のポイント

### IMU（傾き・動きを読む）

`Imu.getAccel()` が加速度 (x, y, z)[G]、`Imu.getGyro()` がジャイロ (x, y, z)[deg/s] を
タプルで返します。傾き検知・歩数・ふり検出などに使えます。

```python
ax, ay, az = Imu.getAccel()
gx, gy, gz = Imu.getGyro()
```

### タッチパネル（画面タッチを入力にする）

`M5.Touch.getCount()` が触れている点の数（0=触れていない）、`getX()` / `getY()` が
座標を返します。画面上にボタン領域を作り、その範囲内かどうかで判定すると
「画面ボタン」になります。

```python
if M5.Touch.getCount():
    x = M5.Touch.getX()
    y = M5.Touch.getY()
```

### バッテリー（電源状態を読む）

`Power.getBatteryLevel()`（0–100[%]）、`Power.getBatteryVoltage()`（mV）、
`Power.isCharging()`（充電中なら True）。電池残量表示や省電力制御に使えます。

```python
level = Power.getBatteryLevel()
volt  = Power.getBatteryVoltage()
charging = Power.isCharging()
```

> **必須メモ**：`M5.begin()` と、ループ内の `M5.update()` を忘れると、IMU 値や
> タッチが更新されません。M5 ライブラリを使うときの「お約束」です。

---

## 画面ボタン（タッチUI）

タッチ座標を使って「画面上のボタン」を作るサンプルです。ボタンの絵は
`M5.Lcd`（描画ライブラリ）で四角形を描き、タッチ座標がその四角形の中なら
**所定の関数を実行する**、という作りです。

| サンプル | 内容 |
| --- | --- |
| [touch_button_single.py](../m5stack_samples/touch_button_single.py) | 1つのボタン。押すたびに `on_button_pressed()` を実行し回数を表示 |
| [touch_button_yesno.py](../m5stack_samples/touch_button_yesno.py) | YES / NO の2ボタン。それぞれ `on_yes()` / `on_no()` を実行し回数を表示 |
| [touch_counter.py](../m5stack_samples/touch_counter.py) | 画面のどこでもタッチで `on_touch()` を実行しタッチ回数を表示 |

### しくみ（3つの部品）

**1. ボタンを描く**（四角形＋文字）

```python
M5.Lcd.fillRect(x, y, w, h, 0x1E88E5)   # 塗りつぶし四角（ボタン本体）
M5.Lcd.drawRect(x, y, w, h, 0xFFFFFF)   # 枠線
M5.Lcd.setTextColor(0xFFFFFF, 0x1E88E5)
M5.Lcd.setTextSize(3)
M5.Lcd.setCursor(x + 24, y + 16)
M5.Lcd.print("PUSH")
```

**2. タッチが「ボタンの中」か判定する**

```python
def in_rect(px, py, rect):
    x, y, w, h = rect
    return x <= px <= x + w and y <= py <= y + h
```

**3. 「押した瞬間」だけ1回反応する（押しっぱなし対策）**

タッチが「無→有」に変わった瞬間だけ処理します（こうしないと連続でカウントされます）。

```python
touching = M5.Touch.getCount() > 0
if touching and not prev_touching:
    if in_rect(M5.Touch.getX(), M5.Touch.getY(), BTN):
        on_button_pressed()     # ← 所定の関数を呼ぶ
prev_touching = touching
```

ボタンを増やしたいときは、四角形の座標を増やして `in_rect()` の判定と
呼び出す関数を足すだけです（YES/NO サンプルがその例）。

### 日本語の表示について（注意）

本体の内蔵フォントは**日本語を含みません**。そのため各サンプルでは、
**画面表示は英字**（例：`Pushed: 3 times`）、**日本語は PC のターミナル**に
`print()` で出しています（例：`ボタンが 3 回押されました`）。
画面に日本語を出したい場合は、日本語フォントを別途読み込む必要があります。

---

→ 出力系は [21_CoreS3固有機能_出力サンプル.md](21_CoreS3固有機能_出力サンプル.md) を参照。

### 参考（公式 API）
- IMU：<https://uiflow-micropython.readthedocs.io/en/latest/hardware/imu.html>
- Touch：<https://uiflow-micropython.readthedocs.io/en/latest/hardware/touch.html>
- Power：<https://uiflow-micropython.readthedocs.io/en/latest/hardware/power.html>
