"""
Grove - Temperature & Humidity Sensor (DHT11) (SKU: 101020739)
--------------------------------------------------------------
DHT11 で温度と湿度を読み取る 1線式デジタルセンサー。
※ UIFlow2 ファームウェアには標準の dht モジュールが無いため、1-Wire プロトコルを
   自前で読み取る（ビットバング）実装にしている。タイミングにより読み取りに失敗する
   ことがあるので、失敗時はメッセージを出して次の回にリトライする。

対象   : M5Stack CoreS3 + UIFlow2 ファームウェア (MicroPython)
接続   : PORT.B  ( 黒=GND / 赤=5V / 黄=G9 / 白=G8 )  信号は 黄線 = G9
実行   : python -m mpremote run dht11.py
終了   : Ctrl-C (PC側ターミナルで送信)
"""

from machine import Pin, time_pulse_us, disable_irq, enable_irq  # type: ignore
import time  # type: ignore

# --- 設定 ---------------------------------------------------------
SIG_PIN = 9          # PORT.B 黄線 (G9)
INTERVAL = 2.0       # DHT11 は 2 秒以上の間隔が必要


def read_dht11(pin_num):
    """DHT11 から (温度[℃], 湿度[%]) を読み取る。失敗時は OSError。"""
    # --- スタート信号：20ms LOW → 解放 ---
    pin = Pin(pin_num, Pin.OUT)
    pin.value(0)
    time.sleep_ms(20)
    pin.value(1)
    time.sleep_us(30)
    pin.init(Pin.IN, Pin.PULL_UP)

    data = bytearray(5)
    state = disable_irq()          # タイミング安定化のため割り込み停止
    try:
        # 応答：LOW約80us → HIGH約80us
        if time_pulse_us(pin, 0, 500) < 0:
            raise OSError("no response (low)")
        if time_pulse_us(pin, 1, 500) < 0:
            raise OSError("no response (high)")
        # 40ビット：各ビットは LOW約50us → HIGH（約26us=0 / 約70us=1）
        for i in range(40):
            if time_pulse_us(pin, 0, 500) < 0:
                raise OSError("bit low timeout")
            w = time_pulse_us(pin, 1, 500)
            if w < 0:
                raise OSError("bit high timeout")
            if w > 50:
                data[i // 8] |= 1 << (7 - (i % 8))
    finally:
        enable_irq(state)

    # チェックサム確認
    if ((data[0] + data[1] + data[2] + data[3]) & 0xFF) != data[4]:
        raise OSError("checksum error")
    humidity = data[0]        # DHT11 は整数部のみ
    temperature = data[2]
    return temperature, humidity


def setup():
    print("Grove DHT11 started (Ctrl-C to stop)")


def loop():
    try:
        t, h = read_dht11(SIG_PIN)
        print("temp:", t, "C  humi:", h, "%")
    except OSError as e:
        print("read failed (retry):", e)   # タイミング等で失敗した回
    time.sleep(INTERVAL)


setup()
try:
    while True:
        loop()
except KeyboardInterrupt:
    print("stopped")
