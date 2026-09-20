# 📚 nuu-notes

聯合大學資管系大二上：修課筆記 × 時間管理 × 進度追蹤整合系統

---

## 🎯 這個 Repo 的目的

1. **唯一真相來源** — 統一管理七門專業課與通識筆記、手寫掃描檔與程式碼，徹底解決散落問題。
2. **時間與作息導航** — 嚴格落實「睡滿 8 小時（22:30~06:30）」與「讀書 ➔ 操場慢跑 1h ➔ 滿血讀書」心流模型。
3. **學科進度看板** — 追蹤各科 DDL、章節進度、18 週考期與期末專題。
4. **三端無縫同步** — 電腦（Obsidian/VSCode）寫作、平板（Obsidian+Git）隨行閱讀、手機（Termux）快速查閱。

---

## 🧭 導航中樞 (Dashboard)

- ⏰ **[[dashboard/routine-schedule|日常作息與時間管理導航]]**：含每週完整課表、各科教室、黃金空堂深度工作塊（週三/週五下午）、操場慢跑重開機循環。
- 📊 **[[dashboard/progress|學期進度看板與 DDL 追蹤]]**：18 週重大里程碑、本週待辦、各科卡關點與每週回顧。

---

## 📁 課程資料夾結構

```
nuu-notes/
├── dashboard/
│   ├── routine-schedule.md   ← 課表、作息、空堂深度工作塊、慢跑心流模型
│   └── progress.md           ← 學期里程碑、本週 DDL、各科每週進度
│
├── courses/                  ← 一門課一資料夾（英文命名，相容跨平台）
│   ├── data-structures/      ← 資料結構 (温敏淦)
│   ├── database-systems/     ← 資料庫系統管理 (陳士杰)
│   ├── statistics/           ← 統計學(一) (張志信)
│   ├── network-administration/← 網路管理 / CCNA (張朝旭)
│   ├── management/           ← 管理學 (陳振東)
│   ├── ai-programming/       ← 人工智慧程式設計 (温敏淦)
│   ├── financial-markets/    ← 金融機構與市場 (楊屯山)
│   ├── business-english/     ← 商用英文實務(一) (王淳瑩)
│   ├── historical-thinking/  ← 歷史思維 (黃偉雯)
│   └── sketching-graphics/   ← 素描與圖學 (楊德全)
│       ├── README.md         ← 各科 18 週大綱、評分佔比、筆記索引
│       ├── notes/            ← 上課筆記 (.md)
│       ├── code/             ← 程式作業 (.py / .ipynb / .cpp)
│       ├── assignments/      ← 作業檔、投影片報告
│       └── assets/           ← 筆記附圖、手寫筆記掃描檔
│
├── assets/                   ← Obsidian 全域附件庫 (貼圖/圖片)
├── templates/                ← 筆記與課程模板
└── archive-freshman/         ← 大一筆記歸檔區
```

---

## 🛠️ 三端工作流程

| 裝置 | 主要工具 | 場景與用途 |
|:---|:---|:---|
| **電腦 (Desktop)** | Obsidian + VSCode | 主力開發：寫筆記、寫 Code、跑模擬、Git Commit & Push |
| **平板 (Tablet)** | Obsidian + Git plugin | 課堂隨行：隨身閱讀、複習進度看板、上課手寫/打字筆記 |
| **手機 (Mobile)** | Termux / Git | 通勤速查：檢視當日作息、查詢指令備忘、突發靈感記錄 |

---

## 📏 核心使用規則

1. **嚴格作息保證**：每日 `22:30` 就寢、`06:30` 起床（睡滿 8 小時，專注力基石）。
2. **每篇筆記結尾寫一行**：「這篇筆記我可以拿來做什麼？」（強化知識活用）。
3. **每日結束前 Commit 一次**：`git add . && git commit -m "yyyy-mm-dd 進度"`（22:00 前完成）。
4. **課程目錄維持英文命名**：避免跨平台終端（Termux）路徑編碼錯誤。
5. **筆記檔名標準格式**：`YYYY-MM-DD-主題.md`（例如：`2026-09-08-ch01-data-and-statistics.md`）。

---

## 🔧 常用 Git 指令備忘

```bash
git status                    # 查看目前變更
git add .                     # 將所有筆記與圖檔加入暫存
git commit -m "feat: 今日進度" # 提交變更
git push                      # 推上 GitHub (供平板拉取)
git pull                      # 從 GitHub 拉取最新進度
```

---

## 📝 學期資訊

- **學校班級**：國立聯合大學 資訊管理學系 日資管二甲
- **學期**：115 學年度 第 1 學期
- **開始使用日**：2026-09-19
