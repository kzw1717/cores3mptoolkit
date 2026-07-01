"""
CoreS3 → Discord Webhook テキスト送信サンプル（出力）
------------------------------------------------------
Wi-Fi に接続し、Discord の Webhook URL にテキストメッセージを POST します。

対象 : M5Stack CoreS3 + UIFlow2 ファームウェア（M5 ライブラリ）
接続 : 不要（Wi-Fi を使用）
準備 : 下の WIFI_SSID / WIFI_PASS / WEBHOOK_URL を自分の値に書き換える
実行 : python -m mpremote run discord_text.py    （VSCode は Ctrl+Shift+B）
終了 : Ctrl-C（PC側ターミナルで送信）
参考 : https://uiflow-micropython.readthedocs.io/en/latest/software/requests2.html

Webhook の作り方（解説ページ参照）:
  Discord のサーバー設定 → 連携サービス → ウェブフック → 新しいウェブフック →
  URL をコピーして WEBHOOK_URL に貼る。
"""

import M5  # type: ignore
from M5 import *  # type: ignore
import network  # type: ignore
import requests2  # type: ignore
import time  # type: ignore

# --- 設定（自分の値に書き換える）---------------------------------
WIFI_SSID = "your-wifi-ssid"
WIFI_PASS = "your-wifi-password"
WEBHOOK_URL = "https://discord.com/api/webhooks/xxxxx/yyyyy"
MESSAGE = "M5Stack CoreS3 からこんにちは！"


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
    return wlan.ifconfig()[0]   # 取得した IP アドレス


def send_text(message):
    """Discord Webhook にテキストを送る。"""
    res = requests2.post(WEBHOOK_URL, json={"content": message})
    code = res.status_code
    res.close()
    return code


def setup():
    """起動時に一度だけ実行：Wi-Fi 接続 → メッセージ送信"""
    M5.begin()
    Widgets.fillScreen(0x222222)
    label = Widgets.Label("Wi-Fi connecting...", 10, 60, 1.0, 0xFFFFFF, 0x222222, Widgets.FONTS.DejaVu18)

    ip = connect_wifi(WIFI_SSID, WIFI_PASS)
    print("Wi-Fi connected  IP:", ip)
    label.setText("Sending...")

    code = send_text(MESSAGE)
    print("Discord response code:", code)   # 204 なら送信成功
    label.setText("Sent (code {})".format(code))


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
