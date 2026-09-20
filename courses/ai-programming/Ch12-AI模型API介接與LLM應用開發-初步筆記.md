# 🤖 人工智慧 Ch12: AI 模型 API 介接與 LLM 應用開發 (LLM APIs & Prompting)

> **授課教師**：溫敏淦 教授  
> **教材對齊**：進度大綱第 15～16 週 人工智慧相關 Python API 應用  
> **核心主題**：現代 LLM API (Google Gemini API / OpenAI API)、提示詞工程 (Prompt Engineering)、結構化 JSON 輸出 (Structured Outputs)、函式呼叫 (Function Calling) 與智慧 Agent 雛形

---

## 1. Gemini API 官方 SDK 呼叫範本
```python
from google import genai

# 初始化客戶端 (環境變數 GEMINI_API_KEY)
client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="請用三句話向大二資管系學生解釋什麼是 Transformer 架構？"
)

print(response.text)
```

---

## 🎯 課堂速記與實作留白區

```markdown
<!-- 上課重點即時填寫區 -->
> [!note] 課堂速記 (隨堂記錄溫老師補充)
> - 
```
