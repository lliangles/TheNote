# 📚 nuu-notes

聯合大學資管系大二上修課筆記 + 進度管理系統

## 🎯 這個 repo 的目的

1. **統一筆記散落問題** — 手寫、Word、電腦資料夾散在各處，這裡是唯一真相來源
2. **管理七門課的進度** — 作業 DDL、章節進度、待複習項目
3. **三端同步** — 電腦 / 平板 / 手機 都能寫、都能讀
4. **未來作品集底稿** — 整理好的部分可以 fork 出去做 public repo

## 📁 資料夾結構

```
nuu-notes/
├── courses/              ← 七門課，一課一資料夾
│   ├── course-01/        ← 請改名成實際課名（例如：statistics）
│   │   ├── README.md     ← 課程總覽（老師、教材、進度）
│   │   ├── notes/        ← 上課筆記（.md）
│   │   ├── code/         ← 程式作業（.ipynb / .py）
│   │   └── assignments/  ← 作業檔、報告
│   └── ...
│
├── dashboard/
│   └── progress.md       ← 進度看板：本週 DDL、七門課狀態
│
├── archive-freshman/     ← 大一筆記慢慢遷移過來（不急）
│
└── templates/            ← 筆記/課程 README 的模板
```

## 🛠️ 三端工作流程

| 裝置 | 主要工具 | 場景 |
|---|---|---|
| **電腦** | Obsidian + VSCode | 主力：寫筆記、跑 code、commit |
| **平板** | Obsidian + Git plugin | 上課即時寫筆記 |
| **手機** | Termux | 通勤查筆記、記待辦 |

## 📏 使用規則（自訂，可改）

1. **每篇筆記結尾寫一行**：這篇筆記我可以拿來做什麼？
2. **每天結束前 commit 一次**：`git add . && git commit -m "yyyy-mm-dd 進度"`
3. **課程資料夾用英文命名**：避免 Termux 上處理中文路徑麻煩
4. **筆記檔名格式**：`YYYY-MM-DD-主題.md`（例如：`2026-09-19-變異數分析.md`）

## 🔧 常用 Git 指令備忘

```bash
git status                    # 看目前有哪些變更
git add .                     # 把所有變更加入暫存
git commit -m "訊息"          # 提交
git push                      # 推上 GitHub
git pull                      # 從 GitHub 拉最新
```

## 📝 學期資訊

- **學期**：2026 秋（大二上）
- **開始使用日**：2026-09-19
