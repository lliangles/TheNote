# 📚 nuu-notes

聯合大學資管系大二上：修課筆記 × 時間管理 × 手寫稿數位整合庫

---

## 🎯 這個 Repo 的目的

1. **唯一真相來源** — 統一管理七門專業課與通識筆記、課堂手寫掃描稿、各章初步骨幹筆記，徹底告別檔案散落與重複抄寫 PPT。
2. **極簡無噪聲知識庫** — 嚴格剔除無意義之樣板空資料夾（`code/`、`assignments/`），以扁平清爽的章節筆記結構直通 Obsidian。
3. **時間與作息導航** — 嚴格落實「睡滿 8 小時（22:30~06:30）」與「讀書 ➔ 操場慢跑 1h ➔ 滿血讀書」心流模型。
4. **學科進度看板** — 追蹤各科 DDL、章節進度、18 週考期與期末專題。
5. **三端無縫同步** — 電腦（Obsidian/VSCode）寫作、平板（Obsidian+Git）課堂即時劃記與修改、手機（Termux）快速查閱。

---

## 🧭 導航中樞 (Dashboard)

- ⏰ **[[dashboard/routine-schedule|日常作息與時間管理導航]]**：含每週完整課表、各科教室、黃金空堂深度工作塊（週三/週五下午）、操場慢跑重開機循環。
- 📊 **[[dashboard/progress|學期進度看板與 DDL 追蹤]]**：18 週重大里程碑、本週待辦、各科卡關點與每週回顧。

---

## 📁 課程資料夾結構 (極簡扁平版)

```
D:\NOTE/
├── README.md                      ← 筆記庫導覽與指引
├── dashboard/
│   ├── routine-schedule.md        ← 課表、作息、深度工作塊
│   └── progress.md                ← 學期里程碑、本週 DDL
│
├── courses/                       ← 一門課一資料夾（英文目錄名稱，相容跨平台）
│   ├── data-structures/           ← 資料結構 (温敏淦)
│   │   ├── README.md              ← 18 週大綱與全章索引
│   │   ├── Ch01-基礎概念與效能分析.md
│   │   ├── Ch02-陣列結構與稀疏矩陣.md
│   │   └── Ch03~Ch08 投影片校準初步筆記
│   │
│   ├── database-systems/          ← 資料庫系統管理 (陳士杰)
│   │   ├── README.md              ← 18 週進度與評分
│   │   ├── Ch01-資料庫系統概念與架構.md (融合手寫稿 L1)
│   │   ├── Ch02-關聯式資料模型與完整性限制.md
│   │   ├── Ch03~Ch04 ER 與 SQL 初步筆記
│   │   └── assets/ (存放手寫原圖)
│   │
│   ├── statistics/                ← 統計學(一) (張志信)
│   │   ├── README.md
│   │   ├── Ch01-資料與統計導論.md (融合手寫稿 P1-P2)
│   │   ├── Ch02-Excel敘述統計與絕對參照.md
│   │   ├── Ch03~Ch08 數值度量/機率/抽樣/區間估計初步筆記
│   │   └── assets/ (存放手寫 PDF)
│   │
│   ├── network-administration/    ← 網路管理 CCNA (張朝旭)
│   │   ├── README.md
│   │   ├── W01-Cisco-CLI操作模式與常用指令.md (融合手寫稿)
│   │   ├── W02-光纖與序列介面設定實作.md (融合手寫稿)
│   │   ├── W03~W08 靜態路由/動態協定/RIP/路由表/EIGRP/OSPF初步筆記
│   │   └── assets/ (存放 CCNA 手寫 PDF)
│   │
│   ├── management/                ← 管理學 (陳振東)
│   │   ├── README.md
│   │   ├── Ch01-管理者與管理思維.md
│   │   └── Ch02~Ch03 決策與組織文化初步筆記
│   │
│   ├── financial-markets/         ← 金融機構與市場 (楊屯山)
│   │   ├── README.md
│   │   ├── W01-金融市場概論與財報架構.md
│   │   ├── W02-公司內在價值與ETF評價機制.md
│   │   └── Ch03~Ch04 利率期間結構與貨幣市場初步筆記
│   │
│   ├── ai-programming/            ← 人工智慧程式設計 (温敏淦)
│   │   ├── README.md
│   │   ├── Ch01-人工智慧導論與LLM基礎.md
│   │   ├── Ch02-神經網路架構與反向傳播.md (融合手寫神經元模型)
│   │   ├── Ch03~Ch05 NumPy / Pandas / 可視化初步筆記
│   │   ├── Anaconda開發環境配置指引.md
│   │   └── assets/ (存放手寫神經網路圖)
│   │
│   ├── business-english/          ← 商用英文實務(一) (王淳瑩)
│   ├── historical-thinking/       ← 歷史思維 (黃偉雯)
│   └── sketching-graphics/        ← 素描與圖學 (楊德全)
│
├── assets/                        ← 全域 Obsidian 圖片庫
└── templates/                     ← 筆記模板
```

---

## 🛠️ 三端工作流程

| 裝置 | 主要工具 | 場景與用途 |
|:---|:---|:---|
| **電腦 (Desktop)** | Obsidian + VSCode | 主力學習：深入補充筆記、對照教科書、撰寫程式實作、Git Commit & Push |
| **平板 (Tablet)** | Obsidian + Git plugin | 課堂隨行：隨堂劃記重點、直接修改預建初步筆記、手寫圖檔比對複習 |
| **手機 (Mobile)** | Termux / Git | 通勤速查：檢視當日作息、查詢指令備忘、突發靈感記錄 |

---

## 📏 核心使用規則

1. **嚴格作息保證**：每日 `22:30` 就寢、`06:30` 起床（睡滿 8 小時，專注力基石）。
2. **手寫掃描即時融入**：課堂上傳的手寫紙稿，掃描至對應科目的 `assets/`，提煉要點後整合進對應章節筆記。
3. **每日結束前 Commit 一次**：`git add . && git commit -m "yyyy-mm-dd 進度"`（22:00 前完成）。
4. **課程目錄維持英文命名**：避免跨平台終端（Termux）路徑編碼錯誤。

---

## 🔧 常用 Git 指令備忘

```bash
git status                    # 查看目前變更
git add .                     # 將所有筆記與圖檔加入暫存
git commit -m "feat: 今日進度" # 提交變更
git push                      # 推上 GitHub (供平板拉取)
git pull                      # 從 GitHub 拉取最新進度
```
