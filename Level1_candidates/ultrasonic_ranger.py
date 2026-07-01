"""
Grove - Ultrasonic Ranger (SKU: 101020743)
------------------------------------------
超音波で対象までの距離を非接触で測定する距離センサー。
1本の信号線(SIG)でトリガ送信とエコー受信を行います。測定範囲 約2〜350cm。

対象   : M5Stack CoreS3 + UIFlow2 ファームウェア (MicroPython)
接続   : PORT.B  ( 黒=GND / 赤=5V / 黄=G9 / 白=G8 )
         センサーの信号(SIG)は 黄線 = G9 です
実行   : mpremote run ultrasonic_ranger.py
終了   : Ctrl-C (PC側ターミナルで送信)
"""

from machine import Pin, time_pulse_us
import time

# --- 設定 ---------------------------------------------------------
SIG_PIN = 9          # PORT.B 黄線 (G9)
INTERVAL = 0.3       # loop() の実行間隔 [秒]
TIMEOUT_US = 30000   # エコー待ちタイムアウト [マイクロ秒]


def measure_cm():
    """SIG ピンでトリガを送り、エコー時間から距離[cm]を返す"""
    # 10us のトリガパルスを出力
    p = Pin(SIG_PIN, Pin.OUT)
    p.value(0)
    time.sleep_us(2)
    p.value(1)
    time.sleep_us(10)
    p.value(0)
    # 同じピンを入力に切り替えてエコーパルス幅を測定
    p = Pin(SIG_PIN, Pin.IN)
    dur = time_pulse_us(p, 1, TIMEOUT_US)
    if dur < 0:
        return -1.0                 # タイムアウト(範囲外)
    return dur / 58.0               # 往復時間[us] -> 距離[cm]


def setup():
    """起動時に一度だけ実行する初期化処理"""
    print("Grove Ultrasonic Ranger 開始 (Ctrl-C で終了)")


def loop():
    """繰り返し実行する処理"""
    d = measure_cm()
    if d < 0:
        print("range : 測定範囲外")
    else:
        print("dist  : {:.1f} cm".format(d))
    time.sleep(INTERVAL)


# --- エントリポイント ---------------------------------------------
setup()
try:
    while True:
        loop()
except KeyboardInterrupt:
    print("終了しました")
