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

| サンプル（.py へのリンク） | 機能（内蔵デバイス） | 動作の概要 |
| --- | --- | --- |
| [imu_accel.py](../m5stack_samples/imu_accel.py) | IMU（BMI270：加速度＋ジャイロ） | 6軸の値を画面と端末に表示 |
| [touch_position.py](../m5stack_samples/touch_position.py) | タッチパネル（FT6336U） | 触れた座標 (x, y) を表示 |
| [battery_status.py](../m5stack_samples/battery_status.py) | 電源管理（AXP2101） | 電池残量[%]・電圧[mV]・充電状態を表示 |

---

## それぞれの要点

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

→ 出力系は [21_CoreS3固有機能_出力サンプル.md](21_CoreS3固有機能_出力サンプル.md) を参照。

### 参考（公式 API）
- IMU：<https://uiflow-micropython.readthedocs.io/en/latest/hardware/imu.html>
- Touch：<https://uiflow-micropython.readthedocs.io/en/latest/hardware/touch.html>
- Power：<https://uiflow-micropython.readthedocs.io/en/latest/hardware/power.html>
