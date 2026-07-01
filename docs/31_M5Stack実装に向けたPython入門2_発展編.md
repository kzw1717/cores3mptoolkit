# M5Stack実装に向けたPython入門2（発展編）

[入門編](30_M5Stack実装に向けたPython入門.md)では、どのサンプルにも共通する3つの考え方
（import／メソッド呼び出し／try・except）を学びました。

この発展編では、**一部のサンプルだけに出てくる**少し進んだ書き方をまとめます。
たとえばタッチUI（`touch_counter.py`／`touch_button_single.py`／`touch_button_yesno.py`）や、
Discord へ送るサンプル（`discord_text.py`／`discord_camera.py`）、IMU（`imu_accel.py`）などです。

**すべてを最初から覚える必要はありません。** それぞれのサンプルを読むときに、
必要な項目だけここに戻って確認すれば大丈夫です。各項目は、プログラミング入門I で
学んだ知識に「少しだけ足す」形で説明します。

---

## 1. 論理演算子 `and` / `or` / `not`

`if` の条件で「**AかつB**」「**AまたはB**」「**Aではない**」を表したいときに使います。
入門I では比較（`==` や `>=`）は学びましたが、それを**組み合わせる**のがこの `and` / `or` / `not` です。

`touch_counter.py`（タッチ回数カウンタ）から引用します。

```python
touching = M5.Touch.getCount() > 0        # 今 触れている？（True / False）
if touching and not prev_touching:        # 「今 触れている」かつ「直前は触れていなかった」
    on_touch()                            # → 触れた瞬間だけ1回実行
prev_touching = touching
```

`and` は「両方が True のときだけ True」、`not` は「True と False を反転」します。
ここでは「今は触れていて、さっきは触れていない」＝**押した瞬間**を見分けるために使っています。

`discord_text.py` では `not` を単独で使っています。

```python
if not wlan.isconnected():   # まだ Wi-Fi につながっていなければ
    wlan.connect(ssid, password)
```

> 使用サンプル：`touch_counter.py`(IM4)、`touch_button_single.py`(IM5)、`touch_button_yesno.py`(IM6)、`discord_text.py`(OM14)、`discord_camera.py`(OM15)

---

## 2. 条件付き表式（三項演算子）

`if`〜`else` は学びましたが、「**条件によって値を1つ選ぶ**」だけなら、1行で書ける書き方があります。
`Aになる値 if 条件 else Bになる値` の形です。

`battery_status.py`（バッテリー状態表示）から引用します。

```python
lbl_chg.setText("Charging: {}".format("YES" if charging else "no"))
# charging が True なら "YES"、そうでなければ "no" を選んで表示する
```

これは次の `if`〜`else` と**同じ意味**を、短く書いたものです。

```python
if charging:
    text = "YES"
else:
    text = "no"
lbl_chg.setText("Charging: {}".format(text))
```

> 使用サンプル：`battery_status.py`(IM2)

---

## 3. タプルの代入（複数の値をまとめて受け取る）

入門I で「関数はタプルを返せる」ことは学びました。その**受け取り方**が、この
「タプルの代入（アンパック）」です。左辺に変数をカンマで並べると、**複数の値を一度に**受け取れます。

`imu_accel.py`（IMU）から引用します。

```python
ax, ay, az = Imu.getAccel()   # 加速度の (x, y, z) を、3つの変数に一度に受け取る
gx, gy, gz = Imu.getGyro()    # ジャイロの (x, y, z) も同様
```

タプル以外（リストなど）でも同じように分けられます。`touch_button_single.py` では、
4つの数がまとまった `rect` を4つの変数に分けています。

```python
def in_rect(px, py, rect):
    x, y, w, h = rect          # rect（x, y, 幅, 高さ）を4つに分ける
    return x <= px <= x + w and y <= py <= y + h
```

> 使用サンプル：`imu_accel.py`(IM3)、`touch_button_single.py`(IM5)、`touch_button_yesno.py`(IM6)

---

## 4. `for` でリストを順に処理する

「リストの横断的処理」で学んだ **`for`** を、そのまま使います（復習＋応用）。
リストの要素を1つずつ取り出して、同じ処理を繰り返します。

`speaker_tone.py`（スピーカー）から引用します。

```python
SCALE = [262, 294, 330, 349, 392, 440, 494, 523]   # ドレミ…の周波数のリスト
for freq in SCALE:            # リストの数を1つずつ freq に取り出して
    Speaker.tone(freq, 300)   # その周波数の音を鳴らす
```

`while` でも書けますが、「リストの中身を順に使う」ときは `for` の方が短く分かりやすくなります。

> 使用サンプル：`speaker_tone.py`(OM10)

---

## 5. 辞書（名前と値のセット）

リストは「順番」で値を管理しましたが、**辞書（dict）** は「**名前（キー）**」で値を管理します。
`{"名前": 値}` の形で書きます。ネットワーク送信のサンプルで、送るデータの形として使います。

`discord_text.py`（Discord へテキスト送信）から引用します。

```python
requests2.post(WEBHOOK_URL, json={"content": "こんにちは"})
#                                 ^^^^^^^^^^^^^^^^^^^^^^^^^
#   "content" という名前に "こんにちは" という値を対応させた辞書
```

`discord_camera.py` では、送信の設定（ヘッダ）を辞書で作っています。

```python
headers = {"Content-Type": "multipart/form-data; boundary=" + BOUNDARY}
```

> 辞書はキー（名前）で値を取り出せるのが特長です（`d["content"]` のように使います）。
> 使用サンプル：`discord_text.py`(OM14)、`discord_camera.py`(OM15)

---

## 6. `True` / `False` を返す関数

関数の作り方と「戻り値」は学びました。その戻り値を **`True` / `False`（真偽値）** にすると、
「**〜かどうかを判定する関数**」が作れます。`if` の条件にそのまま使えて便利です。

`touch_button_single.py` の `in_rect` は「点がボタンの四角形の中か？」を判定して返します。

```python
def in_rect(px, py, rect):
    x, y, w, h = rect
    return x <= px <= x + w and y <= py <= y + h   # 中なら True、外なら False

if in_rect(M5.Touch.getX(), M5.Touch.getY(), BTN):  # 戻り値(True/False)をそのまま条件に
    on_button_pressed()
```

判定の中身を関数にまとめておくと、`if` の行がすっきり読みやすくなります。

> 使用サンプル：`touch_button_single.py`(IM5)、`touch_button_yesno.py`(IM6)

---

## 7. 関数の引数の発展：デフォルト値とキーワード引数

「仮引数と実引数」で、関数に値を渡す方法は学びました。ここではその発展を2つ紹介します。

**(1) デフォルト値（省略できる引数）** … 仮引数に `=値` を付けておくと、
呼び出すときに省略でき、省略時はその値が使われます。

`discord_text.py` の Wi-Fi 接続関数から引用します。

```python
def connect_wifi(ssid, password, timeout=15):   # timeout は省略すると 15 になる
    ...

connect_wifi(WIFI_SSID, WIFI_PASS)          # timeout を省略 → 15 が使われる
connect_wifi(WIFI_SSID, WIFI_PASS, 30)      # timeout に 30 を指定
```

**(2) キーワード引数（名前を付けて渡す）** … `名前=値` の形で渡すと、
どの引数に渡しているかが一目で分かります。

`discord_camera.py` のカメラ初期化から引用します。

```python
camera.init(pixformat=camera.RGB565, framesize=camera.QVGA)
#           ^^^^^^^^^ どの設定に渡しているか名前で分かる
requests2.post(WEBHOOK_URL, json={"content": "..."})   # json= もキーワード引数
```

> 使用サンプル：`discord_text.py`(OM14)、`discord_camera.py`(OM15)

---

## 8. 大域変数 `global`

関数の中で作った変数は、その関数の中だけの「ローカル変数」でした（入門I で学習済み）。
関数の**外**で作った変数を、関数の**中から書き換えたい**ときは、`global` と宣言します。

`display_hello.py`（更新カウンタ）から引用します。

```python
count = 0                 # 関数の外で作った変数

def loop():
    global count          # この count は、外の count のことだと宣言
    count += 1            # 外の count を書き換えられる
    lbl_count.setText("count: {}".format(count))
```

`global count` を書かないと、`count += 1` は「関数の中だけの新しい count」を作ろうとして
エラーになります。「外の変数を関数から増やしていく」ときの、おまじないだと考えてください。

> 使用サンプル：`display_hello.py`(OM13)

---

## 9. 数値計算（`math` モジュールと小数の表示）

対数や平方根などの数学関数は、`math` モジュールを `import` して使います。
`temperature_sensor.py`（温度センサー）では、サーミスタの抵抗値から温度を求めるのに
`math.log`（自然対数）を使っています。

```python
import math

tempC = 1.0 / (math.log(R / R0) / B + 1.0 / 298.15) - 273.15
print("temp: {:.1f} C".format(tempC))   # {:.1f} は「小数第1位まで」の表示
```

`import math` の後は `math.log(...)`／`math.sqrt(...)` のように「モノ.機能()」の形で呼びます
（[入門編](30_M5Stack実装に向けたPython入門.md)の「メソッド呼び出し」と同じ形）。
表示の `"{:.1f}".format(値)` は、小数の桁数をそろえたいときの書き方です（`.1f`＝小数第1位まで）。

> 使用サンプル：`temperature_sensor.py`(IG7)

---

## まとめ

ここで扱ったのは、特定のサンプルに出てくる発展的な書き方です。
入門I の基礎と[入門編](30_M5Stack実装に向けたPython入門.md)の3概念があれば、
必要になったときにこの発展編の該当項目を読むだけで、どのサンプルも読み解けるようになります。

各サンプルの詳しい説明は、次の解説ページを参照してください。

- Grove 入力：[10_Grove_入力サンプル.md](10_Grove_入力サンプル.md) ／ 出力：[11_Grove_出力サンプル.md](11_Grove_出力サンプル.md)
- CoreS3 固有機能 入力：[20_CoreS3固有機能_入力サンプル.md](20_CoreS3固有機能_入力サンプル.md) ／ 出力：[21_CoreS3固有機能_出力サンプル.md](21_CoreS3固有機能_出力サンプル.md)
