# Ch05 Matplotlib 與 Seaborn 資料視覺化 (Data Visualization) - 初步筆記

> [!NOTE] 課程資訊與學習目標
> - **授課進度**：第 7~8 週課程
> - **教材來源**：`D:\class-memo\migan-ai\class-mitirial\科學計算資料分析matplotliby.pptx`
> - **核心目標**：熟練 Matplotlib 物件導向畫布架構（Figure / Axes）、掌握四種常用統計圖表（折線圖、散佈圖、直方圖、長條圖）、利用 Seaborn 繪製相關係數熱力圖。

---

## 1. 物件導向繪圖標準樣板

```python
import matplotlib.pyplot as plt
import seaborn as sns

# 建立 1 列 2 欄的子圖畫布
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 子圖 1: 折線圖
axes[0].plot(x, y, color="royalblue", marker="o", label="Trend")
axes[0].set_title("Line Chart")
axes[0].set_xlabel("X-Axis")
axes[0].set_ylabel("Y-Axis")
axes[0].legend()
axes[0].grid(True, linestyle="--", alpha=0.6)

# 子圖 2: Seaborn 相關係數熱力圖
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", ax=axes[1])
axes[1].set_title("Correlation Heatmap")

plt.tight_layout()
plt.show()
```

---

## 📌 隨堂註記 / 老師口述補充

> [!NOTE] 隨堂筆記區
> - 上課即時補充重點區。
