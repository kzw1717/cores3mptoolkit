"""
CoreS3 カメラ撮影 → Discord Webhook 画像送信サンプル（出力）
------------------------------------------------------
内蔵カメラ(GC0308)で1枚撮影し、JPEG に変換して Discord の Webhook に
画像として POST します（multipart/form-data で送信）。

対象 : M5Stack CoreS3 + UIFlow2 ファームウェア（M5 ライブラリ / camera・jpg モジュール）
接続 : 不要（本体内蔵カメラ ＋ Wi-Fi を使用）
準備 : 下の WIFI_SSID / WIFI_PASS / WEBHOOK_URL を自分の値に書き換える
実行 : python -m mpremote run discord_camera.py    （VSCode は Ctrl+Shift+B）
終了 : Ctrl-C（PC側ターミナルで送信）
参考 : camera   https://uiflow-micropython.readthedocs.io/en/latest/advanced/camera.html
       jpg      https://uiflow-micropython.readthedocs.io/en/latest/advanced/jpg.html
       requests https://uiflow-micropython.readthedocs.io/en/latest/software/requests2.html

メモ : camera / jpg モジュールは CoreS3 専用です。
"""

import M5
from M5 import *
import network
import requests2
import camera
import jpg
import time

# --- 設定（自分の値に書き換える）---------------------------------
WIFI_SSID = "your-wifi-ssid"
WIFI_PASS = "your-wifi-password"
WEBHOOK_URL = "https://discord.com/api/webhooks/xxxxx/yyyyy"
CAPTION = "CoreS3 カメラからの写真"
JPEG_QUALITY = 80          # JPEG 品質 0-100（高いほど高画質・大容量）
BOUNDARY = "----m5stackCoreS3Boundary"


def connect_wifi(ssid, password, timeout=15):
    """Wi-Fi に接続する。接続済みなら何もしない。"""
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        wlan.connect(ssid, password)
        start = time.time()
        while not wlan.isconnected():
            if time.time() - start > timeout:
                raise RuntimeError("Wi-Fi connect timeout")
            time.sleep(0.5)
    return wlan.ifconfig()[0]


def capture_jpeg():
    """カメラで1枚撮影し JPEG のバイト列を返す。"""
    # 自動露出を安定させるため数フレーム捨ててから撮る
    for _ in range(10):
        img = camera.snapshot()
        M5.update()
        time.sleep(0.05)
    img = camera.snapshot()
    M5.Lcd.show(img, 0, 0, 320, 240)        # 撮影画像を画面に表示
    img_jpg = jpg.encode(img, JPEG_QUALITY)  # RGB565 → JPEG
    return img_jpg.bytearray()


def build_multipart(text, filename, jpeg_bytes):
    """Discord 用の multipart/form-data 本体（bytes）を組み立てる。"""
    b = BOUNDARY.encode()
    parts = []
    parts.append(b"--" + b + b"\r\n")
    parts.append(b'Content-Disposition: form-data; name="content"\r\n\r\n')
    parts.append(text.encode() + b"\r\n")
    parts.append(b"--" + b + b"\r\n")
    parts.append(b'Content-Disposition: form-data; name="file"; filename="' + filename.encode() + b'"\r\n')
    parts.append(b"Content-Type: image/jpeg\r\n\r\n")
    parts.append(bytes(jpeg_bytes))
    parts.append(b"\r\n")
    parts.append(b"--" + b + b"--\r\n")
    return b"".join(parts)


def send_image(jpeg_bytes):
    """JPEG 画像を Discord Webhook に送る。"""
    body = build_multipart(CAPTION, "photo.jpg", jpeg_bytes)
    headers = {"Content-Type": "multipart/form-data; boundary=" + BOUNDARY}
    res = requests2.post(WEBHOOK_URL, data=body, headers=headers)
    code = res.status_code
    res.close()
    return code


def setup():
    """起動時に一度だけ実行：カメラ初期化 → Wi-Fi → 撮影 → 送信"""
    M5.begin()
    Widgets.fillScreen(0x222222)
    camera.init(pixformat=camera.RGB565, framesize=camera.QVGA)  # 320x240

    ip = connect_wifi(WIFI_SSID, WIFI_PASS)
    print("Wi-Fi connected  IP:", ip)

    jpeg_bytes = capture_jpeg()
    print("Captured  JPEG size:", len(jpeg_bytes), "bytes")

    code = send_image(jpeg_bytes)
    print("Discord response code:", code)   # 204（環境により200）なら送信成功
    print("Sent (Ctrl-C to stop)")


def loop():
    M5.update()
    time.sleep(0.5)


# --- エントリポイント ---------------------------------------------
setup()
try:
    while True:
        loop()
except KeyboardInterrupt:
    print("stopped")
