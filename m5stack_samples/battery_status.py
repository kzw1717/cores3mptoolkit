"""
CoreS3 内蔵 電源管理 (AXP2101)  ── 入力サンプル
------------------------------------------------------
内蔵バッテリーの残量[%]・電圧[mV]・充電中かどうかを読み取り、
画面と PC のターミナルに表示します。配線は不要です（本体内蔵）。

対象 : M5Stack CoreS3 + UIFlow2 ファームウェア（M5 ライブラリ）
接続 : 不要（本体内蔵 PMU）
実行 : python -m mpremote run battery_status.py    （VSCode は Ctrl+Shift+B）
終了 : Ctrl-C（PC側ターミナルで送信）
参考 : https://uiflow-micropython.readthedocs.io/en/latest/hardware/power.html
"""

import M5  # type: ignore
from M5 import *  # type: ignore
import time  # type: ignore

# --- 設定 ---------------------------------------------------------
INTERVAL = 1.0        # loop() の実行間隔 [秒]

lbl_level = None
lbl_volt = None
lbl_chg = None


def setup():
    """起動時に一度だけ実行する初期化処理"""
    global lbl_level, lbl_volt, lbl_chg
    M5.begin()
    Widgets.fillScreen(0x222222)
    Widgets.Title("CoreS3 Battery", 3, 0xFFFFFF, 0x0000FF, Widgets.FONTS.DejaVu18)
    lbl_level = Widgets.Label("Battery:", 10, 55, 1.0, 0xFFFFFF, 0x222222, Widgets.FONTS.DejaVu18)
    lbl_volt = Widgets.Label("Voltage:", 10, 100, 1.0, 0xFFFFFF, 0x222222, Widgets.FONTS.DejaVu18)
    lbl_chg = Widgets.Label("Charging:", 10, 145, 1.0, 0xFFFFFF, 0x222222, Widgets.FONTS.DejaVu18)
    print("Battery monitor started (Ctrl-C to stop)")


def loop():
    """繰り返し実行する処理"""
    M5.update()
    level = Power.getBatteryLevel()          # 残量 [%] (0-100)
    volt = Power.getBatteryVoltage()         # 電圧 [mV]
    charging = Power.isCharging()            # 充電中なら True
    lbl_level.setText("Battery: {} %".format(level))
    lbl_volt.setText("Voltage: {} mV".format(volt))
    lbl_chg.setText("Charging: {}".format("YES" if charging else "no"))
    print("level={}%  volt={}mV  charging={}".format(level, volt, charging))
    time.sleep(INTERVAL)


# --- エントリポイント ---------------------------------------------
setup()
try:
    while True:
        loop()
except KeyboardInterrupt:
    print("stopped")
