# 🐼 Ch08 Pandas 異質數據分析、清洗與量化交易時序實務

> **授課教師**：溫敏淦 教授  
> **對應教材**：`科學計算資料分析Pandas.pptx`、`F1700_ch09.pptx`  
> **重點導讀**：全面掌握 Pandas 核心異質資料結構（Series、DataFrame）之建立規則與純量擴展、索引標籤切片 (`loc` 端點閉區間 vs `iloc` 半開區間 vs `at`/`iat` 純量極速存取)、缺失值 (NaN) 運算防護 (`fill_value` 技巧與 `dropna`/`fillna`)、累積統計函式 (`cumsum`, `diff`, `skew`, `kurt`)、時間序列重組，以及第 9 章比特幣量化技術指標（移動平均線 MA、黃金交叉與死亡交叉回測買賣點演算法）。

---

## 📌 1. Pandas 核心架構：Series 與 DataFrame 生成機制

Pandas 建構於 NumPy 之上，專門處理具有標籤索引的**異質資料 (Heterogeneous Data)**。

### 1-1. 一維 Series 生成規則與純量擴展
語法：`pd.Series(data=None, index=None, name=None)`
* **data 為 Dictionary**：
  * 若未指定 `index`，預設以 dict 的 key 作為 Series 的 index。
  * **若顯式指定 `index`，Series 的長度與順序完全由 `index` 決定**！若 index 中存在 dict 所沒有的 key，該項數值**自動填入 `NaN`**！
* **data 為純量 (Scalar)**：
  * 系統會根據 `index` 的元素數量自動進行**純量擴展 (Scalar Expansion)**，將該純量複製填滿所有列。

```python
import pandas as pd
import numpy as np

# 1. 字典生成 Series：依指定 index 抽取，缺漏者補 NaN
price_dict = {"BTC": 65000, "ETH": 3500}
s_crypto = pd.Series(price_dict, index=["BTC", "ETH", "SOL"])
print(s_crypto)
# BTC    65000.0
# ETH     3500.0
# SOL        NaN

# 2. 純量擴展
s_scalar = pd.Series(100, index=["A", "B", "C"])
print(s_scalar)  # A, B, C 皆為 100
```

### 1-2. 二維 DataFrame 多樣化生成方式
* **List of Dicts**：取所有字典 Key 的**聯集**作為欄位名稱 (Columns)，無對應值者補 `NaN`。
* **Dict of Series**：各 Series 的長度**不必相同**，系統會依照各自的 index 自動外聯對齊，缺漏者補 `NaN`。

```python
# List of Dicts 生成 DataFrame
data_records = [
    {"symbol": "BTC", "price": 65000, "market_cap": "1.2T"},
    {"symbol": "ETH", "price": 3500}  # 缺少 market_cap
]
df_crypto = pd.DataFrame(data_records)
print(df_crypto) # ETH 的 market_cap 自動補 NaN
```

---

## 📌 2. 索引參照切片鐵律：`loc` vs `iloc` vs `at` / `iat`

> [!IMPORTANT] 簡報第 11 頁核心語法規範
> 存取 DataFrame 資料時，請嚴格遵守標籤 vs 整數位置之切片端點差異：

| 存取方法 | 定位標準 | 切片區間包含端點 | 適用情境 |
|:---|:---|:---:|:---|
| **`df.loc[r, c]`** | **名稱標籤 (Label-based)** | **包含末端 (Closed `[start:stop]`)** | 依日期、代碼或欄位名稱篩選 |
| **`df.iloc[r, c]`**| **整數下標 (Position-based)**| **不含末端 (Half-open `[start:stop)`)**| 純位置整數切片（同 Python 原生切片）|
| **`df.at[r, c]`**  | 名稱標籤 | 無切片（單一元素） | **極速存取單一純量值**（效能高於 loc） |
| **`df.iat[r, c]`** | 整數下標 | 無切片（單一元素） | **極速存取單一純量值**（效能高於 iloc） |

```python
# ==============================================================================
# 範例程式 8-1：loc 端點包含 vs iloc 端點排除
# ==============================================================================
import pandas as pd

df = pd.DataFrame({
    "Open": [100, 102, 105, 108],
    "Close": [102, 104, 107, 110]
}, index=["day1", "day2", "day3", "day4"])

# 1. loc 標籤切片：包含 "day3"
print(df.loc["day1":"day3", "Close"])  # 包含 day1, day2, day3 (共 3 列)

# 2. iloc 位置切片：不包含索引 3
print(df.iloc[0:2, 1])                 # 僅取第 0, 1 列 (共 2 列)

# 3. at / iat 極速純量取值
val1 = df.at["day2", "Close"]          # 104
val2 = df.iat[1, 1]                    # 104
```

---

## 📌 3. 缺失值處理與安全運算 (`fill_value`)

### 3-1. 運算元含 `NaN` 時的傳播與防護
在 Pandas 中，任何數值與 `NaN` 直接運算，結果必定為 `NaN`。
* **`s.add(s2, fill_value=0)` 技巧**：在運算之前，將缺漏項預先視為 0 進行加總，防止因單一缺失值導致整列失效。

### 3-2. 清洗四大函式
* `df.isna()` / `df.isnull()`：回傳布林遮罩表。
* `df.dropna(axis='index', subset=['Close'], thresh=n)`：剔除無效列；`thresh=n` 代表至少保留有 $n$ 個非空值的列。
* `df.fillna(value)`：填補指定常數或平均數。

---

## 📌 4. 統計聚合與累積時序函式

| 統計函式 | 說明與作用 | 實用場景 |
|:---|:---|:---|
| `describe()` | 輸出計數、均值、標準差、四分位數及極值 | 資料快速探索 (EDA) |
| `cumsum()` / `cumprod()` | 沿軸向計算累積總和 / 累積乘積 | 累積收益率計算 |
| `cummax()` / `cummin()` | 沿軸向計算累積最大值 / 累積最小值 | 計算歷史天花板與資金最大回撤 (MDD) |
| `diff(periods=1)` | **一階差分**（當期減去前一期數值） | 計算每日價格變動額、時間序列平穩化 |
| `pct_change()` | 百分比變動率（當期變動百分比） | 計算股票/比特幣每日報酬率 |
| `skew()` / `kurt()` | 偏度 (Skewness) 與 峰度 (Kurtosis) | 檢驗收益率是否偏離常態分佈 |

---

## 📌 5. 比特幣量化交易實戰：移動平均線 (MA) 與交叉策略回測

> [!IMPORTANT] 對應教材第 9 章 (`F1700_ch09.pptx`) 實戰範例
> 移動平均線 (Moving Average, MA) 代表過去 $N$ 天價格的算術平均，常用於過濾短線雜訊、辨識趨勢方向。

### 5-1. 移動平均與雙均線建構
* **短期均線 (SMA_Fast)**：例如 5 日均線（反映敏銳短線趨勢）。
* **長期均線 (SMA_Slow)**：例如 20 日均線（反映平穩中長線趨勢）。
* **買賣訊號規則**：
  * **黃金交叉 (Golden Cross)**：短均線由下往上突破長均線 $\Rightarrow$ **買進訊號 (Buy)**。
  * **死亡交叉 (Death Cross)**：短均線由上往下跌破長均線 $\Rightarrow$ **賣出訊號 (Sell)**。

```python
# ==============================================================================
# 範例程式 8-2：比特幣時序分析與黃金交叉交易訊號演算法
# ==============================================================================
import pandas as pd
import numpy as np

# 模擬比特幣 10 日歷史收盤價時序資料
dates = pd.date_range("2026-09-01", periods=10, freq="D")
prices = [60000, 60500, 61200, 62000, 61800, 63000, 64500, 64000, 65500, 67000]

df_btc = pd.DataFrame({"Close": prices}, index=dates)

# 1. rolling(window) 計算移動平均線
df_btc["MA3"] = df_btc["Close"].rolling(window=3).mean()   # 3 日短均線
df_btc["MA5"] = df_btc["Close"].rolling(window=5).mean()   # 5 日長均線

# 2. 計算每日報酬率與累積收益
df_btc["Daily_Return"] = df_btc["Close"].pct_change()
df_btc["Cum_Return"]   = (1 + df_btc["Daily_Return"]).cumprod()

# 3. 雙均線交叉判定
# 訊號: 短均 > 長均 標記為 1 (多頭持倉)，否則為 0
df_btc["Position"] = np.where(df_btc["MA3"] > df_btc["MA5"], 1, 0)
# 訊號差分：1 - 0 = 1 (黃金交叉買點); 0 - 1 = -1 (死亡交叉賣點)
df_btc["Signal"] = df_btc["Position"].diff()

print("=== 比特幣移動平均與量化訊號表 ===")
print(df_btc[["Close", "MA3", "MA5", "Position", "Signal"]].tail(6))

# 篩選買賣決策點
buy_dates = df_btc[df_btc["Signal"] == 1].index
sell_dates = df_btc[df_btc["Signal"] == -1].index
print(f"\n觸發黃金交叉買點日期: {[d.strftime('%Y-%m-%d') for d in buy_dates]}")
print(f"觸發死亡交叉賣點日期: {[d.strftime('%Y-%m-%d') for d in sell_dates]}")
```
