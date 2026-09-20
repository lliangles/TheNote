# 💻 自由程式實作區 (Code Workspace)

本資料夾為純程式碼專屬實作區，與筆記（Markdown）完全解耦，確保在行動端 **Termux（Txmu）** 或各平台終端環境下能無痛直接編譯與執行。

---

## 📂 目錄架構

```text
Code/
├── README.md               <-- 本說明文件（位於專屬資料夾外）
├── cpp/                    <-- 純 C++ 實作區（僅允許 .cpp/.h）
│   └── main.cpp
├── python/                 <-- 純 Python 實作區（僅允許 .py）
│   └── main.py
└── sql/                    <-- 純 SQL 腳本區（僅允許 .sql）
    └── test.sql
```

> [!IMPORTANT]
> **純淨規範**：
> - `cpp/`、`python/`、`sql/` 資料夾內部**嚴禁放置任何 `.md` 筆記或說明文件**。
> - 編譯出的二進位檔案（如 `*.out`、`*.exe`）及臨時資料庫（`*.db`）已被 `.gitignore` 排除，避免污染 Git。

---

## 📱 Termux 執行實測指令指南

在手機 Termux 中進入 `TheNote` 儲存庫目錄並執行以下指令：

### 1. C++ 環境測試 (`cpp/`)
```bash
# 1. 確保已安裝 clang 或 gcc（未安裝可執行: pkg install clang -y）
cd Code/cpp

# 2. 編譯
g++ -O2 main.cpp -o main
# 或使用 clang++
# clang++ main.cpp -o main

# 3. 執行
./main
```

### 2. Python 環境測試 (`python/`)
```bash
# 1. 確保已安裝 python（未安裝可執行: pkg install python -y）
cd Code/python

# 2. 執行
python main.py
```

### 3. SQL 環境測試 (`sql/`)
```bash
# 1. 確保已安裝 sqlite（未安裝可執行: pkg install sqlite -y）
cd Code/sql

# 2. 透過 SQLite 記憶體模式直接測試腳本
sqlite3 < test.sql

# 或輸出至暫存測試資料庫（已被 gitignore 自動忽略）
# sqlite3 test.db < test.sql
```
