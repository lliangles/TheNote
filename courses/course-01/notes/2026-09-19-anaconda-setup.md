---
date: 2026-09-19
course: 環境建置
topic: Anaconda 安裝與驗證
tags: [python, anaconda, 環境, setup]
---

# Anaconda 安裝與驗證

## 🎯 這堂課要解決什麼問題 / 為什麼要學

老師要求裝 Anaconda 當 Python 開發環境。Anaconda 幫你一次裝好 Python + 資料科學會用到的幾百個套件（NumPy、Pandas、Jupyter 等），並附上 conda 這個環境管理工具。

## 📝 主要內容

### 安裝過程遇到的關鍵決定

1. **一開始搞混：安裝檔 ≠ 已安裝**
   - 下載 `.exe` 只是把安裝檔放到下載夾，還沒真的安裝
   - 要雙擊執行安裝精靈

2. **Advanced Options 頁的四個勾選**
   - ☑️ Create shortcuts → 勾
   - ⬜ Add to PATH → **不要勾**（官方標紅字 Not recommended，會跟其他軟體衝突）
   - ⬜ Register as default Python 3.14 → 因為系統已經有 3.14，這個被鎖住了，跳過沒關係
   - ☑️ Clear the package cache → 勾（省硬碟空間）

3. **裝完跳出來的註冊頁面可以直接關**
   - `installation-success?source=exe_installer` 是行銷頁，不是安裝流程
   - Anaconda 帳號綁的是他們的雲端服務，本機用完全不需要

### 怎麼驗證裝好了

不能用一般 CMD，要用**開始選單搜尋「Anaconda Prompt」**打開專屬視窗，然後跑：

```bash
conda --version    # → conda 26.5.3
python --version   # → Python 3.14.6
conda list         # → 噴出一大串已安裝套件
```

看到 `(base) C:\Users\kelly>` 這個提示符，代表目前在 conda 的 base 環境裡。

### Jupyter Notebook 開啟方式

```bash
jupyter notebook
```

會自動開瀏覽器到 `localhost:8888/tree`，這是 Jupyter 在本機跑的伺服器介面。

## 💭 我的理解（用自己的話重寫一次）

Anaconda 不是 Python 本身，它是「Python + 一堆套件 + conda 管理工具」的懶人包。conda 環境就像不同的工作桌，每張桌上放不同的工具組合。預設的桌子叫 `base`。之後每個專案應該開自己的環境，讓套件不打架。

「不加 PATH」是為了讓 Anaconda 待在自己的角落，不去污染系統的其他 Python。要用它時就開 Anaconda Prompt，這是最乾淨的設計。

## ❓ 我還不懂的地方
- conda 環境跟 Python venv 有什麼差別？什麼時候用哪個？
- 之後老師會不會要用 pip 裝套件？pip 跟 conda 一起用要注意什麼？

## 🔗 跟其他知識的連結
- 之後要學 [[conda 環境管理]]，替不同課建立獨立環境
- 跟 [[VSCode Python 環境設定]] 有關（VSCode 要能認得 Anaconda 的 Python）

## ✨ 這篇筆記我可以拿來做什麼？

同學問我 Anaconda 怎麼裝，直接丟這篇給他。以後自己重灌電腦，照這篇 15 分鐘搞定，不用再摸索一次。
