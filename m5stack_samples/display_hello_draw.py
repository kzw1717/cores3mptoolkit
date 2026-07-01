"""
CoreS3 内蔵 ディスプレイ ── 図形描画のみ サンプル（出力・まとめ）
------------------------------------------------------
画面にいろいろな図形をまとめて描きます（円以外も含む）。
個々の図形だけを試したい場合は draw_*.py（図形ごとのサンプル）を参照。

対象 : M5Stack CoreS3 + UIFlow2 ファームウェア（M5 ライブラリ / M5.Lcd 描画）
接続 : 不要（本体内蔵ディスプレイ）
実行 : python -m mpremote run display_hello_draw.py    （VSCode は Ctrl+Shift+B）
終了 : Ctrl-C（PC側ターミナルで送信）
参考 : https://uiflow-micropython.readthedocs.io/en/latest/widgets/index.html

座標系 : 画面は 320 x 240 px。左上が (0, 0)。色は 0xRRGGBB。
"""

import M5  # type: ignore
import time  # type: ignore


def setup():
    M5.begin()
    M5.Lcd.fillScreen(0x000000)
    M5.Lcd.setTextColor(0xFFFFFF, 0x000000)
    M5.Lcd.setTextSize(2)
    M5.Lcd.setCursor(10, 6)
    M5.Lcd.print("Shapes")

    # 四角形（枠線 / 塗り）
    M5.Lcd.drawRect(10, 40, 60, 45, 0x00FF00)
    M5.Lcd.fillRect(80, 40, 60, 45, 0x0000FF)
    # 角丸四角形
    M5.Lcd.fillRoundRect(150, 40, 60, 45, 10, 0xFF9800)
    # 円（枠線 / 塗り）
    M5.Lcd.drawCircle(250, 62, 22, 0x33CCFF)
    M5.Lcd.fillCircle(300, 62, 18, 0x00FFFF)

    # 直線
    M5.Lcd.drawLine(10, 110, 140, 160, 0xFF0000)
    # 三角形（枠線 / 塗り）
    M5.Lcd.drawTriangle(160, 160, 185, 110, 210, 160, 0xFFFF00)
    M5.Lcd.fillTriangle(220, 160, 245, 110, 270, 160, 0xFF00FF)
    # 楕円
    M5.Lcd.fillEllipse(80, 205, 45, 25, 0x00FF00)
    # 円弧（扇形）
    M5.Lcd.fillArc(220, 205, 20, 35, 0, 180, 0x9C27B0)

    print("Shapes sample (Ctrl-C to stop)")


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
