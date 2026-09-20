# Ch03 NumPy 高效科學計算 (NumPy Essentials) - 初步筆記

> [!NOTE] 課程資訊與學習目標
> - **授課進度**：第 3~4 週課程
> - **教材來源**：`D:\class-memo\migan-ai\class-mitirial\科學計算資料分析Numpy.pptx`
> - **核心目標**：熟練 `ndarray` 核心結構與屬性、掌握向量化運算（Vectorization）、精通廣播機制（Broadcasting）與布林遮罩篩選。

---

## 1. `ndarray` 核心屬性與建立方式

```python
import numpy as np

# 建立不同維度的陣列
a = np.array([1, 2, 3])                 # 一維向量
b = np.array([[1, 2, 3], [4, 5, 6]])   # 二維矩陣 (2, 3)

# 核心屬性
print(b.ndim)   # 維度 (Number of dimensions): 2
print(b.shape)  # 形狀 (Shape): (2, 3)
print(b.dtype)  # 資料型態: int64 / int32
print(b.size)   # 總元素數: 6
```

---

## 2. 廣播機制 (Broadcasting Rules)

當兩個陣列維度不同時，NumPy 會自動在後方維度相容的前提下複製延伸，避免不必要的記憶體拷貝：
```python
A = np.array([[1, 2, 3], [4, 5, 6]])  # shape: (2, 3)
B = np.array([10, 20, 30])             # shape: (3,)
C = A + B                              # 自動廣播為 (2, 3) 逐項相加
```

---

## 3. 布林索引與遮罩篩選 (Boolean Indexing)

```python
scores = np.array([55, 78, 92, 43, 88, 60])
pass_mask = scores >= 60               # 產生布林陣列: [False, True, True, False, True, True]
passing_scores = scores[pass_mask]      # 篩選出大於等於 60 分者
```

---

## 📌 隨堂註記 / 老師口述補充

> [!NOTE] 隨堂筆記區
> - 上課即時補充重點區。
