# Windows 11 開発環境セットアップ（VSCode + Python + mpremote）

M5Stack CoreS3 用の MicroPython スクリプトを **VSCode で書いて、mpremote で転送・実行**
するための、Windows 11 側の環境構築手順です。

流れ：**Python（Store版）を入れる → mpremote を入れる → VSCode を入れる → このプロジェクトを開く → 実行**

---

## 1. Python 3.13 をインストール（Microsoft Store 版）

1. スタートメニュー →「Microsoft Store」を開く。
2. 「**Python 3.13**」を検索し、インストールする。
3. 確認：PowerShell またはコマンドプロンプトを開いて、

   ```bat
   python --version
   ```

   `Python 3.13.x` と表示されればOK。

> **Store 版 Python の注意（重要）**
> Store 版は `python` と `pip` には PATH が通りますが、`pip install` で入る
> コマンド（`mpremote` など）の置き場所（Scripts フォルダ）には **PATH が通りません**。
> そのため本プロジェクトでは、コマンドを `mpremote ...` ではなく
> **`python -m mpremote ...`** の形で実行します（VSCode のタスクもこの形にしてあります）。

---

## 2. mpremote をインストール

PowerShell またはコマンドプロンプトで：

```bat
python -m pip install --upgrade pip
python -m pip install mpremote
```

確認：

```bat
python -m mpremote --help
```

ヘルプが表示されればOKです。

> `mpremote` と直接打って「コマンドが見つかりません」と出ても問題ありません。
> 上記のとおり **`python -m mpremote`** を使ってください。
> どうしても短く打ちたい場合は、PowerShell で次のエイリアスを設定できます（任意）。
> ```powershell
> function mpremote { python -m mpremote @args }
> ```

---

## 3. VSCode をインストール

1. <https://code.visualstudio.com/> から VSCode をインストール。
2. 起動後、左の拡張機能アイコンから次を入れる（このプロジェクトを開くと推奨表示されます）。
   - **Python**（ms-python.python）
   - **Pylance**（ms-python.vscode-pylance）

---

## 4. このプロジェクトを開く

1. VSCode →「ファイル」→「フォルダーを開く」→ このプロジェクトフォルダ
   （`I0630_M5StackMicroPythonToolkit`）を選ぶ。
2. 右下に「推奨拡張機能をインストールしますか？」と出たら **インストール**。
3. 左下の Python インタープリター表示をクリックし、**Python 3.13（Store 版）** を選ぶ。

---

## 5. CoreS3 をつないで動かす

1. UIFlow2 v2.4.7 を書き込み済みの CoreS3 を、USB Type-C で PC に接続
   （未書き込みなら `docs/01_ファームウェア書き込み手順.md`）。
2. 接続確認（コマンドパレットからタスク実行、または統合ターミナルで）：

   ```bat
   python -m mpremote devs
   ```

   `COM3` のように表示されればOK。
3. 動かしたい `.py` をエディタで開いた状態で、**実行タスク**を使います。

### VSCode タスクの使い方

`Ctrl + Shift + B`（ビルドタスク）で「**mpremote: 現在のファイルを実行**」が走り、
今開いている `.py` を CoreS3 に送って実行します（本体には保存されません）。
**停止はターミナルで `Ctrl + C`**。

その他のタスクは `Ctrl + Shift + P` →「Tasks: Run Task」から選べます。

| タスク名 | 内容 | 対応コマンド |
| --- | --- | --- |
| mpremote: 現在のファイルを実行 | 開いている .py を転送して実行（既定のビルドタスク） | `python -m mpremote run "${file}"` |
| mpremote: デバイス一覧 | 接続中のポートを表示 | `python -m mpremote devs` |
| mpremote: REPL | 対話モードに入る（抜けるのは Ctrl-]） | `python -m mpremote repl` |
| mpremote: 現在のファイルを本体へコピー | 本体にファイルを保存 | `python -m mpremote cp "${file}" :` |
| mpremote: 本体をリセット | CoreS3 を再起動 | `python -m mpremote reset` |

---

## 6. よくあるつまずき

| 症状 | 対処 |
| --- | --- |
| `python` が見つからない | Store から Python 3.13 を入れ直す。PowerShell を開き直す |
| `mpremote` が見つからない | `python -m mpremote ...` の形で実行する（Store 版の仕様） |
| `mpremote devs` にポートが出ない | データ通信対応ケーブルか確認 → USB ドライバ（CP210x/CH9102）→ 別ポート |
| `could not enter raw repl` | UIFlow デスクトップ・シリアルモニタ等がポートを占有していないか確認して閉じる |
| タスクで日本語が文字化け | 統合ターミナルの文字コードを UTF-8 に（`chcp 65001`）。本リポジトリは UTF-8/LF 前提 |

---

### 参考リンク
- mpremote 公式ドキュメント：<https://docs.micropython.org/en/latest/reference/mpremote.html>
- Microsoft Store 版 Python について（公式 FAQ）：<https://learn.microsoft.com/en-us/windows/python/faqs>
