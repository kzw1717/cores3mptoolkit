# GitHub 公開手順（Mac で実行）

このリポジトリを GitHub に公開する手順です。**ご自身の Mac のターミナル**で実行してください。

> 補足：作業環境（サンドボックス）からフォルダへ git を直接実行すると、ファイル削除系の
> 操作が制限され最後まで完了できませんでした。そのため最初に、作りかけの `.git` を
> 削除してから作り直します（中身のファイルはそのまま使えます）。

## 1. リポジトリを初期化してコミット

```bash
cd "/Users/watanabekoichi/Developments/Claude_Projects/I0630_M5StackMicroPythonToolkit"

# 作りかけの .git を削除（初回のみ）
rm -rf .git

# 初期化 → コミット
git init -b main
git add -A
git commit -m "Initial commit: M5Stack Core S3 MicroPython Toolkit"
```

> 名前/メールが未設定なら、コミット前に一度だけ：
> ```bash
> git config --global user.name "あなたの名前"
> git config --global user.email "あなたのメール"
> ```

## 2. GitHub に公開（どちらか）

### A. GitHub CLI（`gh`）がある場合 — 最短

```bash
gh repo create m5stack-core-s3-micropython-toolkit --public --source=. --remote=origin --push
```

### B. 手動の場合

1. GitHub で **空のリポジトリ**を作成（README/.gitignore は付けない）。
   名前例：`m5stack-core-s3-micropython-toolkit`
2. 作成後に表示される URL を使って：

```bash
git remote add origin https://github.com/<あなたのユーザー名>/m5stack-core-s3-micropython-toolkit.git
git push -u origin main
```

## 3. 以降の更新

```bash
git add -A
git commit -m "変更内容のメモ"
git push
```

---

### 確認
公開後、GitHub 上でトップの `README.md` が目次として表示され、`docs/` の各解説ページから
`Level1_samples/` や `m5stack_samples/` の `.py` にリンクが張られていれば成功です。
