# 🐼 Ch08 Pandas 數據清洗與統計分析

> **授課教師**：溫敏淦 教授  
> **對應簡報**：`科學計算資料分析Pandas.pptx`  
> **重點導讀**：系統化掌握一維 Series 與二維 DataFrame 核心架構、外部資料匯入匯出 (`read_csv`, `to_excel`)、精準選取切片 (`loc` vs `iloc`)、缺失值偵測與補值 (`dropna`, `fillna`)、群組聚合統計 (`groupby`, `agg`)、資料透視表 (`pivot_table`)，以及多資料集整合 (`merge`, `concat`)。

---

## 📌 1. Pandas 兩大核心資料架構

1. **Series**：帶有標籤索引 (Index) 的一維同質陣列。
2. **DataFrame**：表格型二維資料結構，每一欄可具備不同的資料型別（數字、字串、布林等），擁有「列索引 (Index)」與「欄位名稱 (Columns)」。

```python
# ==============================================================================
# 範例程式 8-1：DataFrame 建立與基本屬性探索
# ==============================================================================
import pandas as pd
import numpy as np

# 透過字典建立 DataFrame
raw_data = {
    "StudentID": ["A01", "A02", "A03", "A04", "A05"],
    "Department": ["資管", "資工", "資管", "財金", "資管"],
    "Midterm": [85, 92, np.nan, 75, 90],  # 含缺失值
    "Final": [88, 95, 60, 70, 94],
    "Attendance": [95, 100, 70, 80, 100]
}

df = pd.DataFrame(raw_data)
print("=== 原始學生資料表 ===")
print(df)

# 基本結構資訊探查
print(f"\n資料維度 (Rows, Cols): {df.shape}")
print(f"欄位型別:\n{df.dtypes}")
print("\n--- 數值統計摘要 describe() ---")
print(df.describe())
```

---

## 📌 2. 資料選取：`loc`（標籤索引）vs `iloc`（整數位置）

| 選取方式 | 語法規則 | 範例與意義 |
| :--- | :--- | :--- |
| **`loc`** | **以列/欄的「名稱標籤」定位** | `df.loc[0:2, ['StudentID', 'Midterm']]` |
| **`iloc`** | **以列/欄的「整數下標 (0-indexed)」定位** | `df.iloc[0:2, 0:3]`（含前不含後） |

```python
# ==============================================================================
# 範例程式 8-2：loc, iloc 與布林條件篩選
# ==============================================================================

# 1. iloc 純整數位置選取：取前 3 列、前 2 欄
sub_iloc = df.iloc[:3, :2]
print("iloc 前三列與前兩欄:\n", sub_iloc)

# 2. loc 條件過濾選取：資管系且期末考 >= 80 分的同學
condition = (df["Department"] == "資管") & (df["Final"] >= 80)
filtered_df = df.loc[condition, ["StudentID", "Department", "Final"]]
print("\n篩選資管系且期末考優秀者:\n", filtered_df)
```

---

## 📌 3. 缺失值處理 (Missing Data Cleaning)

在機器學習與統計分析中，遺漏值 (NaN) 會導致模型無法訓練，必須進行嚴格清洗：

```python
# ==============================================================================
# 範例程式 8-3：缺失值檢測、剔除與智慧填補
# ==============================================================================

# 1. 檢測缺失值數量
print("各欄位缺失值統計:\n", df.isnull().sum())

# 2. 策略 A：直接刪除含有缺失值的列
df_dropped = df.dropna()
print(f"刪除缺失值後剩餘列數: {len(df_dropped)}")

# 3. 策略 B：統計填補（以期中考平均值填補缺考者）
midterm_mean = df["Midterm"].mean()
df_filled = df.copy()
df_filled["Midterm"] = df_filled["Midterm"].fillna(midterm_mean)
print(f"\n以平均分 ({midterm_mean:.1f}) 填補後的期中成績:\n", df_filled["Midterm"])
```

---

## 📌 4. 群組分析 (GroupBy) 與資料透視表 (Pivot Table)

```python
# ==============================================================================
# 範例程式 8-4：分組聚合統計與 Pivot Table 應用
# ==============================================================================

# 1. 分組統計 (GroupBy)：計算各學系在期中與期末的平均成績與人數
dept_summary = df_filled.groupby("Department").agg(
    學生人數=("StudentID", "count"),
    期中平均=("Midterm", "mean"),
    期末平均=("Final", "mean")
).reset_index()

print("=== 各系所成績彙整表 ===")
print(dept_summary)

# 2. 新增衍生欄位 (Feature Engineering)
df_filled["TotalScore"] = df_filled["Midterm"] * 0.4 + df_filled["Final"] * 0.6

# 3. 資料透視表 (Pivot Table)
pivot_res = df_filled.pivot_table(
    values="TotalScore",
    index="Department",
    aggfunc=["mean", "max", "min"]
)
print("\n=== 學系總評分透視表 ===")
print(pivot_res)
```

---

## 📌 5. 多表合併：`concat` 與 `merge`

```python
# ==============================================================================
# 範例程式 8-5：資料表串接 (Concat) 與資料庫關聯合併 (Merge / Join)
# ==============================================================================

# 表 1: 學生課外社團
df_clubs = pd.DataFrame({
    "StudentID": ["A01", "A02", "A04"],
    "Club": ["AI 研究社", "程式競賽社", "吉他社"]
})

# 類似 SQL INNER JOIN 進行學號關聯
merged_df = pd.merge(df_filled, df_clubs, on="StudentID", how="left")
# 填充沒參加社團者的缺失值
merged_df["Club"] = merged_df["Club"].fillna("未參加社團")

print("=== 學生名冊與社團資料合併結果 ===")
print(merged_df[["StudentID", "Department", "TotalScore", "Club"]])
```
