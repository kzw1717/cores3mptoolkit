"""
Grove - Temperature & Humidity Sensor (DHT11) (SKU: 101020739)
--------------------------------------------------------------
DHT11 で温度と湿度を読み取る 1線式デジタルセンサー。
※ UIFlow2 ファームウェアには標準の dht モジュールが無いため、1-Wire プロトコルを
   自前で読み取る（ビットバング）実装にしている。ESP32/MicroPython の μs 級タイミングは
   環境依存で不安定なため、失敗時はメッセージを出して次の回にリトライする。

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
    pin = Pin(pin_num, Pin.OUT)
    pin.value(1)
    time.sleep_ms(50)
    # スタート信号：18ms以上 LOW
    pin.value(0)
    time.sleep_ms(20)

    data = bytearray(5)
    state = disable_irq()          # ここから割り込み停止（タイミング死守）
    try:
        pin.value(1)               # 解放
        pin.init(Pin.IN, Pin.PULL_UP)
        # 解放直後の HIGH を測る → DHT が LOW に引くまで（取り逃し防止）
        if time_pulse_us(pin, 1, 200) < 0:
            raise OSError("no response (release high)")
        # 応答：LOW約80us → HIGH約80us
        if time_pulse_us(pin, 0, 200) < 0:
            raise OSError("no response (low)")
        if time_pulse_us(pin, 1, 200) < 0:
            raise OSError("no response (high)")
        # 40ビット：各ビット LOW約50us → HIGH（約26us=0 / 約70us=1）
        for i in range(40):
            if time_pulse_us(pin, 0, 200) < 0:
                raise OSError("bit low timeout")
            w = time_pulse_us(pin, 1, 200)
            if w < 0:
                raise OSError("bit high timeout")
            if w > 50:
                data[i // 8] |= 1 << (7 - (i % 8))
    finally:
        enable_irq(state)

    if ((data[0] + data[1] + data[2] + data[3]) & 0xFF) != data[4]:
        raise OSError("checksum error")
    return data[2], data[0]        # (温度, 湿度)  DHT11 は整数部のみ


def setup():
    print("Grove DHT11 started (Ctrl-C to stop)")


def loop():
    try:
        t, h = read_dht11(SIG_PIN)
        print("temp:", t, "C  humi:", h, "%")
    except OSError as e:
        print("read failed (retry):", e)
    time.sleep(INTERVAL)


setup()
try:
    while True:
        loop()
except KeyboardInterrupt:
    print("stopped")
