# 🧮 Ch07 NumPy 高效科學計算與矩陣運算

> **授課教師**：溫敏淦 教授  
> **對應簡報**：`科學計算資料分析Numpy.pptx`  
> **重點導讀**：深入理解 NumPy 核心 `ndarray` 物件之記憶體連續排列本質、陣列建構屬性 (shape, ndim, dtype)、強大的廣播機制 (Broadcasting)、向量化運算取代 Python 慢速 for 迴圈之原理、布林遮罩索引、統計聚合函數，以及線性代數矩陣運算。

---

## 📌 1. 為什麼人工智慧底層必用 NumPy？

Python 原生 `list` 是物件指標陣列，元素散落在記憶體各處，且每次存取需動態型別檢查；  
NumPy 的 `ndarray` 具有：
1. **連續的 C 語言記憶體區塊**：極高的快取命中率 (CPU Cache Hit)。
2. **同質性資料 (Homogeneous)**：固定記憶體大小（如 `float64`, `int32`）。
3. **向量化 (Vectorization) 與 SIMD 指令集支援**：底層利用 BLAS/LAPACK 進行高度平行計算。

```python
# ==============================================================================
# 範例程式 7-1：NumPy 向量化運算 vs 原生 Python 迴圈速度對決
# ==============================================================================
import numpy as np
import time

size = 1_000_000

# 1. 原生 Python list 平方運算
py_list = list(range(size))
start = time.time()
py_result = [x ** 2 for x in py_list]
py_time = time.time() - start

# 2. NumPy 向量化平方運算
np_arr = np.arange(size)
start = time.time()
np_result = np_arr ** 2
np_time = time.time() - start

print(f"原生 Python 執行時間: {py_time:.5f} 秒")
print(f"NumPy 向量化執行時間: {np_time:.5f} 秒")
print(f"🚀 NumPy 效能加速倍數: 約 {py_time / np_time:.1f} 倍！")
```

---

## 📌 2. ndarray 建立、屬性與形狀重塑 (Reshape)

```python
# ==============================================================================
# 範例程式 7-2：陣列建構與維度形狀轉換
# ==============================================================================
import numpy as np

# 1. 建立陣列
a1 = np.array([1, 2, 3, 4, 5, 6])
zeros_arr = np.zeros((2, 3))          # 全 0 矩陣 (2x3)
ones_arr = np.ones((3, 3))            # 全 1 矩陣 (3x3)
eye_matrix = np.eye(3)                # 3x3 單位矩陣 (Identity Matrix)
linspace_arr = np.linspace(0, 1, 5)   # 在 0 到 1 之間產生 5 個等間距點

print(f"等間距陣列: {linspace_arr}")

# 2. 檢視核心屬性
print(f"維度數量 (ndim): {zeros_arr.ndim}")        # 2
print(f"形狀形狀 (shape): {zeros_arr.shape}")      # (2, 3)
print(f"元素總數 (size):  {zeros_arr.size}")       # 6
print(f"資料型別 (dtype): {zeros_arr.dtype}")      # float64

# 3. 形狀變更 reshape(-1 由系統自動推算)
matrix_2x3 = a1.reshape(2, 3)
matrix_3x2 = a1.reshape(3, -1)        # 自動推斷欄數為 2
flattened = matrix_2x3.flatten()      # 展平成一維陣列

print(f"2x3 矩陣:\n{matrix_2x3}")
print(f"展平後: {flattened}")
```

---

## 📌 3. 廣播機制 (Broadcasting) 規則

廣播允許不同維度形狀的陣列進行算術運算，無需額外複製記憶體。  
**廣播兩大相容規則**：從末端維度（最右邊）開始往前比對：
1. 維度大小**完全相同**，或
2. 其中一個維度的大小**為 1**。

```python
# ==============================================================================
# 範例程式 7-3：廣播機制實例（特徵標準化常用）
# ==============================================================================
import numpy as np

# 假設資料矩陣為 3 筆樣本、每筆樣本有 2 個特徵 (形狀 3x2)
data = np.array([
    [10.0, 200.0],
    [20.0, 400.0],
    [30.0, 600.0]
])

# 每個特徵的平均值 (形狀 1x2)
means = np.array([20.0, 400.0])

# 廣播運算：(3, 2) 減去 (2,) -> 自動將 (2,) 廣播擴展為 3 列進行逐元素相減
centered_data = data - means

print("--- 零均值化資料 (Centering) ---")
print(centered_data)
```

---

## 📌 4. 布林遮罩索引 (Boolean Masking) 與統計聚合

```python
# ==============================================================================
# 範例程式 7-4：條件遮罩篩選與統計運算
# ==============================================================================
import numpy as np

scores = np.array([55, 78, 92, 45, 88, 60, 99, 30])

# 1. 布林遮罩 (Boolean Mask)
pass_mask = scores >= 60
print(f"及格遮罩陣列: {pass_mask}")
passed_scores = scores[pass_mask]      # 提取及格的所有成績
print(f"及格成績清單: {passed_scores}")

# 2. 條件替換 np.where(條件, 真值替換, 假值替換)
# 將所有不及格 (<60) 的成績全部補正為 60 分
adjusted_scores = np.where(scores < 60, 60, scores)
print(f"調分後成績:   {adjusted_scores}")

# 3. 沿軸統計聚合運算 (axis=0 沿列向下壓縮 / 垂直; axis=1 沿欄向右壓縮 / 水平)
mat = np.array([[10, 20], [30, 40], [50, 60]])
print(f"整體平均: {mat.mean()}")
print(f"各特徵欄位平均 (axis=0): {mat.mean(axis=0)}")  # [30. 40.]
print(f"各樣本列總和   (axis=1): {mat.sum(axis=1)}")   # [30 70 110]
```

---

## 📌 5. 線性代數與矩陣乘法 (Matrix Multiplication)

```python
# ==============================================================================
# 範例程式 7-5：矩陣內積 (@ 運算子) 與線性方程組求解
# ==============================================================================
import numpy as np

# 1. 矩陣內積 (Matrix Dot Product)
# A 是 2x3 矩陣，B 是 3x2 矩陣 -> 相乘結果為 2x2 矩陣
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[7, 8], [9, 1], [2, 3]])

# 使用 @ 運算子或 np.dot()
C = A @ B
print(f"矩陣內積 C = A @ B:\n{C}")

# 2. 解線性聯立方程式: 2x + y = 8, x + 3y = 13
coeff_matrix = np.array([[2, 1], [1, 3]])  # 係數矩陣
const_vector = np.array([8, 13])           # 常數向量

solution = np.linalg.solve(coeff_matrix, const_vector)
print(f"方程組求解結果: x = {solution[0]:.1f}, y = {solution[1]:.1f}")  # x=2.2, y=3.6
```
