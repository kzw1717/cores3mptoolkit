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

ライセンスは未定です（後日追加予定）。それまでの利用条件は作者にご確認ください。
