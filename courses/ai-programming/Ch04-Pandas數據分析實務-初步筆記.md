# Ch04 Pandas 數據分析實務 (Pandas for Data Analysis) - 初步筆記

> [!NOTE] 課程資訊與學習目標
> - **授課進度**：第 5~6 週課程
> - **教材來源**：`D:\class-memo\migan-ai\class-mitirial\科學計算資料分析Pandas.pptx`
> - **核心目標**：掌握 Series 與 DataFrame 雙核心結構、精通 `loc` 與 `iloc` 資料選取、熟練處理缺失值（Missing Data）與分組聚合（`groupby`）。

---

## 1. 核心資料結構

- **Series**：帶有一維標籤索引（Index）的同質陣列。
- **DataFrame**：具備列索引（Index）與欄標籤（Columns）的二維表格資料結構。

```python
import pandas as pd

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [20, 21, 19],
    "Score": [88, 92, 75]
})
```

---

## 2. `loc` vs. `iloc` 切片定位

- `df.loc[row_label, col_label]`：**依據「名稱標籤」**選取資料（包含結尾標籤！）。
- `df.iloc[row_idx, col_idx]`：**依據「整數位置索引」**選取資料（遵循 Python 慣例：左閉右開，不包含結尾！）。

---

## 3. 缺失值處理與分組聚合

```python
# 1. 檢查與填補缺失值
df.isna().sum()                 # 統計各欄缺失值總數
df_clean = df.fillna(df.mean()) # 以平均值填補數值缺失

# 2. 分組聚合 (Groupby)
df.groupby("Department")["Salary"].agg(["mean", "count", "max"])
```

---

## 📌 隨堂註記 / 老師口述補充

> [!NOTE] 隨堂筆記區
> - 上課即時補充重點區。
