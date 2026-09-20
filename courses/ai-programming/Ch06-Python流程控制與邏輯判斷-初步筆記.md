# 🤖 人工智慧 Ch06: Python 流程控制與邏輯判斷 (Flow Control & Logic)

> **授課教師**：溫敏淦 教授  
> **教材對齊**：進度大綱第 4～5 週 Python 流程控制  
> **核心主題**：條件分支 (`if-elif-else`)、迴圈結構 (`for`, `while`)、跳躍陳述 (`break`, `continue`, `pass`)、推導式 (List/Dict Comprehension) 效率優化

---

## 1. 條件判斷與三元運算子
```python
# 條件判斷
score = 85
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
else:
    grade = 'C'

# Python 三元運算子 (Ternary Operator)
status = "Pass" if score >= 60 else "Fail"
```

## 2. 推導式 (Comprehension) —— Python 向量化與簡潔風格
```python
# 列表推導式 (比傳統 for loop append 快 2~3 倍)
squares = [x**2 for x in range(10) if x % 2 == 0]

# 字典推導式
word_lengths = {word: len(word) for word in ['Python', 'AI', 'TensorFlow']}
```

---

## 🎯 課堂速記與實作留白區

```markdown
<!-- 上課重點即時填寫區 -->
> [!note] 課堂速記 (隨堂記錄溫老師補充)
> - 
```
