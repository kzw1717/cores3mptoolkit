# M5Stack Core S3 MicroPython Toolkit

M5Stack **CoreS3**（UIFlow2 ファームウェア / MicroPython）と **Grove Creator Kit** を使った、
**学生向け PBL（課題解決型学習）**のためのサンプル集です。

入力系・出力系のサンプルスクリプトを並べてあるので、**作りたいものに合わせて
スクリプトをコピー＆ペーストして組み合わせる**ことで、プロトタイプを素早く作れます。

スクリプトは PC（Windows 11 / VSCode）で編集し、`mpremote` で CoreS3 に送って実行します。

---

## 使い方の全体像

```
PC で .py を書く  →  USB で CoreS3 に接続  →  mpremote run で実行  →  Ctrl-C で停止
```

1. **環境を準備する**（最初の1回）
   - [docs/00_Windows環境構築_VSCode.md](docs/00_Windows環境構築_VSCode.md) … Python 3.13・mpremote・VSCode の準備
   - [docs/01_ファームウェア書き込み手順.md](docs/01_ファームウェア書き込み手順.md) … UIFlow2 v2.4.7 の書き込み
2. **サンプルを動かす／組み合わせる**（下の「サンプル解説」へ）

---

## Python 補足教材（サンプルを読む前に）

M5Stack のサンプルは、プログラミング入門I で学ぶ基礎（変数・`if`・`while`・関数・`print` など）に、
いくつか新しい書き方が加わります。**サンプルを読み解くには、次の補足教材を先に読む必要があります。**

### [docs/30_M5Stack実装に向けたPython入門.md](docs/30_M5Stack実装に向けたPython入門.md) 〔全サンプル共通・必読〕

`import`／メソッド呼び出し（`モノ.機能()`）／`try`・`except` の3つを解説します。
これらは **すべてのサンプル（Grove・CoreS3 の全31本）** に共通で出てくるため、
**どのサンプルを読む前にも、まずこの入門編に目を通してください。**

### [docs/31_M5Stack実装に向けたPython入門2_発展編.md](docs/31_M5Stack実装に向けたPython入門2_発展編.md) 〔一部サンプルで必要〕

特定のサンプルだけに出てくる発展的な書き方を解説します。
**下記のサンプルを理解するには、発展編の該当項目を読む必要があります。**

| 発展概念 | 読む必要があるサンプル |
| --- | --- |
| 論理演算子 `and`/`or`/`not` | [IM4] [touch_counter.py](https://github.com/kzw1717/cores3mptoolkit/blob/main/m5stack_samples/touch_counter.py), [IM5] [touch_button_single.py](https://github.com/kzw1717/cores3mptoolkit/blob/main/m5stack_samples/touch_button_single.py), [IM6] [touch_button_yesno.py](https://github.com/kzw1717/cores3mptoolkit/blob/main/m5stack_samples/touch_button_yesno.py), [OM14] [discord_text.py](https://github.com/kzw1717/cores3mptoolkit/blob/main/m5stack_samples/discord_text.py), [OM15] [discord_camera.py](https://github.com/kzw1717/cores3mptoolkit/blob/main/m5stack_samples/discord_camera.py) |
| 条件付き表式（三項演算子） | [IG6] [moisture_sensor.py](https://github.com/kzw1717/cores3mptoolkit/blob/main/Level1_samples/moisture_sensor.py), [IM2] [battery_status.py](https://github.com/kzw1717/cores3mptoolkit/blob/main/m5stack_samples/battery_status.py) |
| タプルの代入（複数まとめて受け取る） | [IM3] [imu_accel.py](https://github.com/kzw1717/cores3mptoolkit/blob/main/m5stack_samples/imu_accel.py), [IM5] [touch_button_single.py](https://github.com/kzw1717/cores3mptoolkit/blob/main/m5stack_samples/touch_button_single.py), [IM6] [touch_button_yesno.py](https://github.com/kzw1717/cores3mptoolkit/blob/main/m5stack_samples/touch_button_yesno.py) |
| `for` でリストを順に処理 | [OM10] [speaker_tone.py](https://github.com/kzw1717/cores3mptoolkit/blob/main/m5stack_samples/speaker_tone.py) |
| 辞書 / キーワード引数・デフォルト値 | [OM14] [discord_text.py](https://github.com/kzw1717/cores3mptoolkit/blob/main/m5stack_samples/discord_text.py), [OM15] [discord_camera.py](https://github.com/kzw1717/cores3mptoolkit/blob/main/m5stack_samples/discord_camera.py) |
| `True`/`False` を返す関数 | [IM5] [touch_button_single.py](https://github.com/kzw1717/cores3mptoolkit/blob/main/m5stack_samples/touch_button_single.py), [IM6] [touch_button_yesno.py](https://github.com/kzw1717/cores3mptoolkit/blob/main/m5stack_samples/touch_button_yesno.py) |
| 大域変数 `global` | [OM13] [display_hello.py](https://github.com/kzw1717/cores3mptoolkit/blob/main/m5stack_samples/display_hello.py) |

> これらのサンプルは、上の発展概念を使っています。該当サンプルを読む前に、
> 表の右側にある概念の項目を発展編で確認してください。

---

## サンプル解説（入力 / 出力で整理）

作りたいプログラムは、「**入力（読み取る）**」と「**出力（光らせる・鳴らす・表示する）**」の
組み合わせで作れます。下の解説ページから必要な `.py` を開いてコピーしてください。

### Grove モジュール（外付け・PORT.B 接続）

| 解説ページ | 内容 |
| --- | --- |
| [docs/10_Grove_入力サンプル.md](docs/10_Grove_入力サンプル.md) | 水・光・磁気・温湿度・土壌・人感・音・距離などの**読み取り** |
| [docs/11_Grove_出力サンプル.md](docs/11_Grove_出力サンプル.md) | LED など**光らせる/動かす**出力 |

実体スクリプト：[`Level1_samples/`](Level1_samples/)（フォルダ内 README あり）

### CoreS3 固有機能（本体内蔵・配線不要）

| 解説ページ | 内容 |
| --- | --- |
| [docs/20_CoreS3固有機能_入力サンプル.md](docs/20_CoreS3固有機能_入力サンプル.md) | IMU（傾き/動き）・タッチ・バッテリーの**読み取り** |
| [docs/21_CoreS3固有機能_出力サンプル.md](docs/21_CoreS3固有機能_出力サンプル.md) | ディスプレイ表示・スピーカー再生の**出力** |

実体スクリプト：[`m5stack_samples/`](m5stack_samples/)（フォルダ内 README あり）

---

## 構成

```
.
├── README.md                       … このファイル
├── docs/                           … 解説ページ（環境構築・FW・入力/出力解説）
├── Level1_samples/                 … Grove サンプル(.py)＋解説 README
├── m5stack_samples/                … CoreS3 固有機能サンプル(.py)＋解説 README
├── .vscode/                        … mpremote 実行タスク等（VSCode 設定）
└── GroveCreaterKit.xlsx ほか        … 部品リスト
```

---

## 前提環境

| 項目 | 内容 |
| --- | --- |
| 本体 | M5Stack CoreS3 |
| ファームウェア | UIFlow2 v2.4.7（MicroPython ベース） |
| 転送・実行 | mpremote（`python -m mpremote ...`） |
| 編集 | VSCode（Windows 11） |
| Python | Microsoft Store 版 Python 3.13.x |

---

## ライセンス

本リポジトリは [MIT License](LICENSE) の下で公開しています。
Copyright (c) 2026 KOICHI WATANABE

## 免責事項（注意書き）

本リポジトリに掲載しているサンプルスクリプトおよび解説は、学習・参考を目的として
「現状のまま（AS IS）」提供されるものであり、その正確性・完全性・特定目的への適合性・
動作を含め、明示・黙示を問わず一切の保証をしません。

本リポジトリ内のコンテンツ（スクリプト、解説、設定例などを含みます）の利用、
または利用できないことに起因して生じたいかなる結果・損害（機器の故障・破損、
データの消失、金銭的損害、その他の直接・間接の損害を含みますが、これらに限りません）
についても、作成者および関係者は一切の責任を負いません。

本リポジトリの内容の利用は、利用者ご自身の判断と責任において行ってください。
ハードウェアの配線・電源・接続にあたっては、各機器の公式ドキュメントおよび
安全上の注意を必ずご確認ください。

---

## Disclaimer

The sample scripts and documentation in this repository are provided "AS IS",
without warranty of any kind. The authors are not liable for any damages or
consequences arising from the use of, or inability to use, the contents of this
repository. Use at your own risk.
