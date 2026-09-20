# 🚀 Ch12 特徵工程、量化金融分析與生成式 AI

> **授課教師**：溫敏淦 教授  
> **對應簡報**：`F1700_ch09.pptx`、`F1700_ch10.pptx`、`bitcoin.7z`  
> **重點導讀**：將資料科學與 AI 全面落地於兩大頂尖應用：(1) 特徵工程與比特幣 (Bitcoin) 歷史時間序列量化分析、雙均線 (SMA) 買賣交易策略回測；(2) 對話機器人 (ChatBot) 架構、Line Messaging API 串接、OpenAI API / ChatGPT 模型串接，以及提示工程 (Prompt Engineering) 結構化輸出實戰。

---

## 📌 1. 比特幣 (Bitcoin) 量化金融特徵工程 (對應課堂 Ch09)

在金融科技 (FinTech) 中，我們透過移動平均線 (Simple Moving Average, SMA) 來過濾市場隨機噪音：
- **短天期均線 (如 SMA-5)**：反應價格最新動態。
- **長天期均線 (如 SMA-20)**：代表中期趨勢防線。
- **黃金交叉 (Golden Cross)**：短均線上穿長均線 $\implies$ **買進信號 (Buy Signal)**。
- **死亡交叉 (Death Cross)**：短均線下穿長均線 $\implies$ **賣出信號 (Sell Signal)**。

```python
# ==============================================================================
# 範例程式 12-1：比特幣歷史價格讀取、特徵工程與雙均線策略回測
# 說明：對應溫敏淦教授 F1700_ch09 課堂主題
# ==============================================================================
import pandas as pd
import numpy as np

# 建立模擬比特幣 100 天交易價格時間序列
np.random.seed(42)
dates = pd.date_range("2024-01-01", periods=100)
# 幾何布朗運動模擬價格走勢
price_changes = np.random.normal(0.002, 0.03, 100)
prices = 42000 * np.cumprod(1 + price_changes)

df_btc = pd.DataFrame({"Date": dates, "Close": prices}).set_index("Date")

# 1. 特徵工程：計算日收益率、滾動波動率、5日均線與20日均線
df_btc["Daily_Return"] = df_btc["Close"].pct_change()
df_btc["SMA_5"] = df_btc["Close"].rolling(window=5).mean()
df_btc["SMA_20"] = df_btc["Close"].rolling(window=20).mean()

# 2. 交易信號判定 (Signal)
# 當 SMA_5 > SMA_20 時持倉 (1)，否則空手 (0)
df_btc["Signal"] = np.where(df_btc["SMA_5"] > df_btc["SMA_20"], 1, 0)
# 部位變更點 (前日信號次日開盤執行)
df_btc["Position"] = df_btc["Signal"].shift(1)

# 3. 策略報酬率計算
df_btc["Strategy_Return"] = df_btc["Position"] * df_btc["Daily_Return"]

# 4. 累積報酬率對比
df_btc["Cum_Market_Return"] = (1 + df_btc["Daily_Return"]).cumprod()
df_btc["Cum_Strategy_Return"] = (1 + df_btc["Strategy_Return"]).cumprod()

print("=== 比特幣雙均線量化策略回測結果 ===")
print(f"市場買進持有 (Buy & Hold) 最終累積報酬: {df_btc['Cum_Market_Return'].iloc[-1]:.4f}")
print(f"雙均線量化策略 (SMA Strategy) 最終累積報酬: {df_btc['Cum_Strategy_Return'].iloc[-1]:.4f}")
```

---

## 📌 2. 對話機器人架構與 Line Messaging API (對應課堂 Ch10)

### Line Bot 運作架構：
$$\text{Line 使用者手機} \xrightarrow{\text{傳送訊息}} \text{Line 官方伺服器} \xrightarrow{\text{Webhook POST}} \text{自建 Flask/FastAPI 後端} \xrightarrow{\text{Reply Token 回應}} \text{使用者}$$

```python
# ==============================================================================
# 範例程式 12-2：Line Bot Webhook 回應伺服器範本 (Flask 架構)
# 說明：對應溫敏淦教授 F1700_ch10 聊天系統實作
# ==============================================================================
from flask import Flask, request, abort

app = Flask(__name__)

@app.route("/callback", methods=["POST"])
def callback():
    """接收 Line Platform 發送的 Webhook 事件通知"""
    signature = request.headers.get("X-Line-Signature")
    body = request.get_data(as_text=True)

    print(f"收到 Line 伺服器通知事件:\n{body}")

    # 實務上在此處使用 line-bot-sdk 驗證簽章並解析 Event
    # event.reply_token 可用於免費回覆訊息
    return "OK"

if __name__ == "__main__":
    # 本地測試可搭配 ngrok 穿透內網: ngrok http 5000
    print("Line Bot 伺服器已就緒...")
```

---

## 📌 3. 生成式 AI 與大型語言模型 API 介接 (OpenAI API)

```python
# ==============================================================================
# 範例程式 12-3：串接現代 LLM API 實現結構化分析與提示工程
# ==============================================================================
import os

def call_llm_assistant(user_prompt: str, system_role: str = "你是一位資深 AI 程式設計教授助教") -> str:
    """
    呼叫大型語言模型生成專業分析回覆（通用範本）
    """
    try:
        # 示範使用 OpenAI 官方最新 API 格式 (v1.0+)
        from openai import OpenAI

        # 建議將金鑰存於環境變數，切勿明文寫入程式碼
        api_key = os.getenv("OPENAI_API_KEY", "your-api-key-here")
        client = OpenAI(api_key=api_key)

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_role},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )
        return response.choices[0].message.content

    except Exception as e:
        return f"API 介接呼叫異常: {e}"

# 提示工程 (Prompt Engineering) 最佳實踐：
# 1. 給定明確角色 (Role)
# 2. 給定具體任務與邊界 (Task & Constraints)
# 3. 指定輸出格式 (Markdown 表格或 JSON)
sample_prompt = """
請分析 Python 中 list.sort() 與內建函式 sorted(list) 的兩大核心差異，
並分別給出一段 3 行以內的示範程式碼。
"""
print("=== 提示工程測試範例 ===")
print("提示詞 (Prompt):\n", sample_prompt)
```
