# 🤖 人工智慧 Ch10: 物件導向程式設計 OOP (Object-Oriented Programming)

> **授課教師**：溫敏淦 教授  
> **教材對齊**：進度大綱第 10～12 週 類別與物件導向  
> **核心主題**：類別與實例 (Class & Instance)、魔術方法 (`__init__`, `__str__`, `__repr__`)、封裝/繼承/多型、類別方法 (`@classmethod`) 與靜態方法 (`@staticmethod`)

---

## 1. AI 代理模型類別封裝範例
```python
class NeuralLayer:
    def __init__(self, in_features: int, out_features: int):
        self.in_features = in_features
        self.out_features = out_features
        self.weights = None
        self.bias = None

    def forward(self, x):
        return f"Computing layer: ({self.in_features} -> {self.out_features})"

class DenseLayer(NeuralLayer):
    def __init__(self, in_features: int, out_features: int, activation: str = 'relu'):
        super().__init__(in_features, out_features)
        self.activation = activation
```

---

## 🎯 課堂速記與實作留白區

```markdown
<!-- 上課重點即時填寫區 -->
> [!note] 課堂速記 (隨堂記錄溫老師補充)
> - 
```
