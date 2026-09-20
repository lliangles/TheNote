# 📊 Ch09 Matplotlib 與 Seaborn 統計視覺化實務

> **授課教師**：溫敏淦 教授  
> **對應簡報**：`科學計算資料分析matplotliby.pptx`  
> **重點導讀**：徹底掌握 Matplotlib 物件導向架構 (`Figure` 與 `Axes`)、折線圖、散佈圖、長條圖、直方圖、箱型圖 (Boxplot) 繪製、Windows 平台繁體中文微軟正黑體字型渲染抗亂碼、多子圖佈局，以及 Seaborn 進階統計熱力圖 (Heatmap)。

---

## 📌 1. Matplotlib 物件導向架構與中文顯示設定

在 Windows 系統中使用 Matplotlib，預設字型為 DejaVu Sans，無法顯示中文會出現豆腐格（亂碼方塊）。  
**標準解決方案**：
```python
import matplotlib.pyplot as plt

# 設定 Windows 內建微軟正黑體與負號正常顯示
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'SimHei', 'Arial']
plt.rcParams['axes.unicode_minus'] = False  # 解決負號 '-' 顯示為方塊的問題
```

### 物件導向層級觀念：
- `Figure`：代表整個畫布視窗。
- `Axes`：代表畫布上的一個獨立子圖表（具有自身的 X 軸、Y 軸、標題與圖例）。

```python
# ==============================================================================
# 範例程式 9-1：物件導向雙子圖繪製（折線圖與散佈圖）
# ==============================================================================
import matplotlib.pyplot as plt
import numpy as np

# 繁體中文字型與負號防護
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False

# 模擬生成訓練數據
epochs = np.arange(1, 21)
# 模擬損失函數 (Loss) 與準確率 (Accuracy)
train_loss = 2.0 * np.exp(-0.2 * epochs) + np.random.normal(0, 0.05, len(epochs))
train_acc = 0.5 + 0.45 * (1 - np.exp(-0.25 * epochs)) + np.random.normal(0, 0.02, len(epochs))

# 建立 1 列 2 欄的子圖畫布 (Figure, Axes)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# 子圖 1: 訓練損失曲線 (折線圖)
ax1.plot(epochs, train_loss, color='#E74C3C', marker='o', linewidth=2, label='訓練損失 (Train Loss)')
ax1.set_title('AI 模型訓練損失收斂曲線', fontsize=14, fontweight='bold')
ax1.set_xlabel('訓練週期 (Epochs)', fontsize=12)
ax1.set_ylabel('Loss 數值', fontsize=12)
ax1.grid(True, linestyle='--', alpha=0.6)
ax1.legend(loc='upper right')

# 子圖 2: 準確率走勢 (散佈圖 + 趨勢線)
ax2.scatter(epochs, train_acc, color='#3498DB', alpha=0.8, s=50, label='週期實測點')
ax2.plot(epochs, train_acc, color='#2980B9', linestyle='-', label='準確率趨勢')
ax2.set_title('AI 模型預測準確率提升曲線', fontsize=14, fontweight='bold')
ax2.set_xlabel('訓練週期 (Epochs)', fontsize=12)
ax2.set_ylabel('Accuracy 準確率', fontsize=12)
ax2.set_ylim(0.4, 1.05)
ax2.grid(True, linestyle='--', alpha=0.6)
ax2.legend(loc='lower right')

plt.tight_layout()
plt.savefig("model_training_curves.png", dpi=150)
print("✅ 模型訓練曲線圖已成功繪製並儲存！")
plt.close()
```

---

## 📌 2. 統計圖表四大天王實作

1. **長條圖 (Bar Chart)**：比較離散類別之數量或數值大小。
2. **直方圖 (Histogram)**：觀察連續型變數的機率密度分佈形態（如偏態、常態分佈）。
3. **箱型圖 (Boxplot)**：快速檢視四分位距 (IQR)、中位數與異常值 (Outliers)。
4. **熱力圖 (Heatmap)**：展示變數之間的相關係數矩陣 (Correlation Matrix)。

```python
# ==============================================================================
# 範例程式 9-2：長條圖、直方圖、箱型圖與 Seaborn 熱力圖
# ==============================================================================
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False

# 建立示範數據集
np.random.seed(42)
df_demo = pd.DataFrame({
    '演算法成績': np.random.normal(75, 10, 200),
    '統計學成績': np.random.normal(70, 15, 200),
    'AI程式成績': np.random.normal(82, 8, 200)
})

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# 1. 直方圖與 KDE 密度估計
sns.histplot(df_demo['AI程式成績'], bins=15, kde=True, color='teal', ax=axes[0])
axes[0].set_title('AI 程式設計期末成績分佈直方圖')
axes[0].set_xlabel('分數')

# 2. 多科目箱型圖 (Boxplot)
sns.boxplot(data=df_demo, palette='Set2', ax=axes[1])
axes[1].set_title('各科目四分位距與極端值箱型圖')
axes[1].set_ylabel('成績區間')

# 3. 相關係數熱力圖 (Heatmap)
corr_matrix = df_demo.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', vmin=-1, vmax=1, ax=axes[2])
axes[2].set_title('科目間成績相關性熱力矩陣')

plt.tight_layout()
plt.savefig("statistical_summary_plots.png", dpi=150)
print("✅ 統計分析圖表庫已成功生成！")
plt.close()
```
