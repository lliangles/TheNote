# 📊 Ch09 Matplotlib 統計繪圖、雙 Y 軸架構與量價視覺化實務

> **授課教師**：溫敏淦 教授  
> **對應教材**：`科學計算資料分析matplotliby.pptx`、`F1700_ch06.pptx`  
> **重點導讀**：系統化解析 Matplotlib 核心繪圖語法（線型/標記/顏色縮寫格式字串）、10 級圖例方位碼、Windows 繁體中文與負號防護、物件導向多子圖 (`subplots`)、**跨數量級共用 X 軸之雙 Y 軸 (`twinx`) 繪圖技術**、常用圖表全解析（散佈圖 `scatter`、長條圖 `bar`/`barh`、直方圖 `hist`、圓餅圖 `pie` 的 `explode` 凸出效果）、Pandas 原生 `plot()` 語法，以及股市量價雙軸視覺化實務。

---

## 📌 1. Matplotlib 基礎語法與格式縮寫代碼

Matplotlib 核心繪圖函式為 `plt.plot(x, y, "格式字串", label="圖例說明")`。當 `x` 省略時，預設使用整數索引 `[0, 1, 2, ...]` 作為 X 軸。

### 1-1. 格式字串語法規範：`[顏色][標記][線型]`
簡報第 2 頁特別統整之精簡縮寫代碼，例如 `"ro--"` 代表「紅色 (r)、圓圈標記 (o)、虛線 (--)」：

| 顏色代碼 (Color) | 意義 | 線型代碼 (Linestyle) | 意義 | 標記代碼 (Marker) | 意義 |
|:---:|:---|:---:|:---|:---:|:---|
| `b` | 藍色 (Blue) | `-` | 實線 (Solid) | `.` | 點 (Point) |
| `g` | 綠色 (Green) | `--` | 虛線 (Dashed) | `,` | 像素 (Pixel) |
| `r` | 紅色 (Red) | `:` | 點線 (Dotted) | `o` | 實心圓 (Circle) |
| `c` | 青色 (Cyan) | `-.` | 虛點線 (Dash-dot) | `s` | 正方形 (Square) |
| `m` | 洋紅 (Magenta) | (省略) | 無線（純散佈點） | `^` | 上三角形 (Triangle) |
| `y` | 黃色 (Yellow) | | | `*` | 星號 (Star) |
| `k` | 黑色 (Black) | | | `D` | 菱形 (Diamond) |
| `w` | 白色 (White) | | | `x` | 叉號 (Cross) |

---

## 📌 2. 常用圖表屬性配置與中文防護

### 2-1. Windows 繁體中文抗亂碼與負號防護
```python
import matplotlib.pyplot as plt

# 1. 指定繁體中文字型（微軟正黑體）
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'DejaVu Sans']
# 2. 解決座標軸負號 '-' 顯示為空白方塊的問題
plt.rcParams['axes.unicode_minus'] = False
```

### 2-2. 圖例位置 (Legend Location) 10 級方位碼
`plt.legend(loc=位置)` 支援字串或整數代碼：
* `0`: `'best'` (由系統自動計算遮蔽最少的位置，預設)
* `1`: `'upper right'` (右上) | `2`: `'upper left'` (左上)
* `3`: `'lower left'` (左下) | `4`: `'lower right'` (右下)
* `5`: `'right'` (右側中)   | `6`: `'center left'` (左側中)
* `7`: `'center right'` (右側中) | `8`: `'lower center'` (正下方)
* `9`: `'upper center'` (正上方) | `10`: `'center'` (正中央)

### 2-3. 坐標軸範圍與刻度控制
* `plt.axis([x_min, x_max, y_min, y_max])`：顯式限定繪製範圍。
* `plt.axis("equal")`：設定 X 軸與 Y 軸比例為 1:1（繪製圓形或等比例幾何圖形必備）。
* `plt.xticks(index_array, label_list, rotation=45)`：自訂 X 軸標籤與旋轉角度。

---

## 📌 3. 雙 Y 軸架構 (`twinx`)：跨數量級量價圖實務

> [!IMPORTANT] 簡報第 4 頁核心技術
> 當同一張圖表中存在兩組時間序列，但**數值數量級差異極大**（例如：股票價格 500~600 元 vs 成交量 10,000~50,000 張），若共用單一 Y 軸會導致股價線被壓成一直線！  
> **解決方案**：呼叫 `ax2 = ax.twinx()`，共用 X 軸但獨立左右兩個 Y 軸！

```python
# ==============================================================================
# 範例程式 9-1：雙 Y 軸量價走勢圖 (Twinx)
# ==============================================================================
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False

days = [f"Day {i}" for i in range(1, 8)]
stock_prices = [580, 585, 592, 588, 605, 610, 615]     # 數量級: 數百
volumes = [15000, 18000, 22000, 12000, 35000, 28000, 40000] # 數量級: 數萬

fig, ax1 = plt.subplots(figsize=(10, 5))

# 左側 Y 軸：繪製股價折線圖 (紅線)
line1 = ax1.plot(days, stock_prices, "ro-", linewidth=2, label="收盤價 (TWD)")
ax1.set_xlabel("交易日期", fontsize=12)
ax1.set_ylabel("股價 (元)", color="r", fontsize=12)
ax1.tick_params(axis="y", labelcolor="r")
ax1.grid(True, linestyle="--", alpha=0.5)

# 右側 Y 軸：共用 X 軸，繪製成交量長條圖 (藍色柱狀)
ax2 = ax1.twinx()
bar1 = ax2.bar(days, volumes, alpha=0.3, color="b", width=0.4, label="成交量 (張)")
ax2.set_ylabel("成交張數", color="b", fontsize=12)
ax2.tick_params(axis="y", labelcolor="b")

# 合併兩軸圖例
lines = line1 + [bar1]
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc=2) # 2: upper left

plt.title("台積電單週股價走勢與成交量 (雙 Y 軸展示)", fontsize=14, fontweight="bold")
plt.savefig("stock_twinx_demo.png", dpi=150)
plt.close()
```

---

## 📌 4. 統計分析四大核心圖表實務

```python
# ==============================================================================
# 範例程式 9-2：散佈圖、長條圖、直方圖與圓餅圖實作
# ==============================================================================
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 1. 散佈圖 (Scatter Plot) + Colorbar 顏色映射
x = np.random.randn(100)
y = 2 * x + np.random.randn(100) * 0.5
colors = np.sqrt(x**2 + y**2)
scatter = axes[0, 0].scatter(x, y, c=colors, cmap="viridis", s=50, alpha=0.8)
axes[0, 0].set_title("特徵散佈圖 (附顏色映射 Colorbar)")
fig.colorbar(scatter, ax=axes[0, 0])

# 2. 長條圖 (Bar Chart)
categories = ["Python", "Java", "C++", "JavaScript", "Go"]
popularity = [85, 62, 54, 78, 45]
axes[0, 1].bar(categories, popularity, color=["#3498db", "#e74c3c", "#2ecc71", "#f39c12", "#9b59b6"])
axes[0, 1].set_title("2026 程式語言受歡迎指數")
axes[0, 1].set_ylabel("指數分")

# 3. 直方圖 (Histogram)：統計區間個數與回傳 bins
data_dist = np.random.normal(loc=70, scale=10, size=500)
counts, bin_edges, _ = axes[1, 0].hist(data_dist, bins=10, color="teal", edgecolor="black", alpha=0.7)
axes[1, 0].set_title("期末成績分佈直方圖 (10 Bins)")
axes[1, 0].set_xlabel("成績分段")

# 4. 圓餅圖 (Pie Chart)：explode 凸出特定切片
market_share = [40, 25, 20, 15]
labels = ["比特幣 (BTC)", "以太幣 (ETH)", "幣安幣 (BNB)", "其他幣種"]
explode = (0.1, 0, 0, 0)  # 僅將第 0 個切片 (BTC) 突出 10%
axes[1, 1].pie(market_share, explode=explode, labels=labels, autopct="%1.1f%%",
               shadow=True, startangle=140, colors=["#f39c12", "#3498db", "#f1c40f", "#95a5a6"])
axes[1, 1].set_title("加密貨幣市場份額佔比 (Pie Chart)")

plt.tight_layout()
plt.savefig("statistical_plots_demo.png", dpi=150)
plt.close()
```

---

## 📌 5. Pandas 原生繪圖介面速查

Pandas 的 `Series` 與 `DataFrame` 均內建封裝了 Matplotlib 的 `.plot()` 方法：
* **`df.plot(kind="line", ...)`**：
  * `kind="line"`：折線圖（預設以 index 為 X 軸，多欄位自動畫多條線）。
  * `kind="bar"` / `kind="barh"`：垂直/水平長條圖。
  * `kind="hist"`：頻率直方圖。
  * `kind="box"` 或 `df.boxplot()`：箱型圖（檢視中位數與離群值）。
  * `kind="scatter", x="col1", y="col2"`：兩欄位間的散佈圖。
* **常用控制參數**：
  * `rot=45`：X 軸標籤旋轉角度。
  * `subplots=True`：將每一欄自動畫在各自獨立的子圖上。
  * `figsize=(w, h)`：直接指定畫布寬度與高度。
