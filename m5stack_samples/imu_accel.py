"""
CoreS3 内蔵 IMU (BMI270 + BMM150)  ── 入力サンプル
------------------------------------------------------
本体内蔵の6軸IMU（3軸加速度＋3軸ジャイロ）の値を読み取り、
画面と PC のターミナルに表示します。配線は不要です（本体内蔵）。

対象 : M5Stack CoreS3 + UIFlow2 ファームウェア（M5 ライブラリ）
接続 : 不要（本体内蔵センサー）
実行 : python -m mpremote run imu_accel.py    （VSCode は Ctrl+Shift+B）
終了 : Ctrl-C（PC側ターミナルで送信）
参考 : https://uiflow-micropython.readthedocs.io/en/latest/hardware/imu.html
"""

import M5
from M5 import *      # Widgets, Imu などが使えるようになる
import time

# --- 設定 ---------------------------------------------------------
INTERVAL = 0.2        # loop() の実行間隔 [秒]

lbl_acc = None
lbl_gyr = None


def setup():
    """起動時に一度だけ実行する初期化処理"""
    global lbl_acc, lbl_gyr
    M5.begin()                                   # M5 機能の初期化（最初に必須）
    Widgets.fillScreen(0x222222)
    Widgets.Title("CoreS3 IMU", 3, 0xFFFFFF, 0x0000FF, Widgets.FONTS.DejaVu18)
    lbl_acc = Widgets.Label("Acc:", 6, 50, 1.0, 0xFFFFFF, 0x222222, Widgets.FONTS.DejaVu18)
    lbl_gyr = Widgets.Label("Gyro:", 6, 110, 1.0, 0x00FF00, 0x222222, Widgets.FONTS.DejaVu18)
    print("IMU started (Ctrl-C to stop)")


def loop():
    """繰り返し実行する処理"""
    M5.update()                                  # M5 の状態更新（ループ内で必須）
    ax, ay, az = Imu.getAccel()                  # 加速度 (x, y, z) [G]
    gx, gy, gz = Imu.getGyro()                   # 角速度 (x, y, z) [deg/s]
    lbl_acc.setText("Acc x:{:.2f}\n    y:{:.2f}\n    z:{:.2f}".format(ax, ay, az))
    lbl_gyr.setText("Gyro x:{:.1f}\n     y:{:.1f}\n     z:{:.1f}".format(gx, gy, gz))
    print("Acc({:.2f},{:.2f},{:.2f})  Gyro({:.1f},{:.1f},{:.1f})".format(ax, ay, az, gx, gy, gz))
    time.sleep(INTERVAL)


# --- エントリポイント ---------------------------------------------
setup()
try:
    while True:
        loop()
except KeyboardInterrupt:
    print("stopped")
