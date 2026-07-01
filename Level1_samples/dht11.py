"""
Grove - Temperature & Humidity Sensor (DHT11) (SKU: 101020739)
-------------------------------------------------------------
DHT11 による温度と湿度を同時計測する1線式デジタルセンサー。
読み取りは 1 秒以上の間隔をあける必要があります。

対象   : M5Stack CoreS3 + UIFlow2 ファームウェア (MicroPython)
接続   : PORT.B  ( 黒=GND / 赤=5V / 黄=G9 / 白=G8 )
         センサーの信号は 黄線 = G9 で読み取ります
実行   : python -m mpremote run dht11.py
終了   : Ctrl-C (PC側ターミナルで送信)
備考   : dht モジュールは MicroPython に標準搭載（追加導入不要）
"""

from machine import Pin  # type: ignore
import dht  # type: ignore
import time  # type: ignore

# --- 設定 ---------------------------------------------------------
SIG_PIN = 9          # PORT.B 黄線 (G9)
INTERVAL = 2.0       # loop() の実行間隔 [秒] (DHT11は2秒以上推奨)

# グローバル変数 (setup() で初期化)
sensor = None


def setup():
    """起動時に一度だけ実行する初期化処理"""
    global sensor
    sensor = dht.DHT11(Pin(SIG_PIN))
    print("Grove DHT11 started (Ctrl-C to stop)")


def loop():
    """繰り返し実行する処理"""
    try:
        sensor.measure()
        print("temp: {} C  humi: {} %".format(
            sensor.temperature(), sensor.humidity()))
    except OSError:
        print("read failed (check wiring/power)")
    time.sleep(INTERVAL)


# --- エントリポイント ---------------------------------------------
setup()
try:
    while True:
        loop()
except KeyboardInterrupt:
    print("stopped")
