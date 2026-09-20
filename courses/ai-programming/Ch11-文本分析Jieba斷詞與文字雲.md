# 📰 Ch11 文本分析、Jieba 中文斷詞與文字雲

> **授課教師**：溫敏淦 教授  
> **對應簡報**：`F1700_ch08n.pptx`  
> **重點導讀**：系統化貫穿自然語言處理 (NLP) 完整管線：從新聞網站爬蟲（ETtoday / Yahoo 新聞）、中文斷詞核心工具 Jieba（精確模式、全模式、搜尋引擎模式）、自訂專業詞典、停用詞 (Stopwords) 過濾清洗、TF-IDF 關鍵字詞頻加權，到使用 WordCloud 與 Matplotlib 產生自訂造型遮罩之高解析度視覺化文字雲。

---

## 📌 1. 中文自然語言處理 (NLP) 處理管線

英文文本天然具備空白作為單詞分隔；而中文語句連綿成串，必須先透過**中文分詞 (Tokenization)** 算法識別詞彙邊界：

```mermaid
flowchart LR
    A[原始新聞文本爬取] --> B[文字清洗/去除標點]
    B --> C[Jieba 中文斷詞]
    C --> D[自訂字典擴充/停用詞過濾]
    D --> E[詞頻統計 / TF-IDF 加權]
    E --> F[WordCloud 遮罩文字雲]
```

---

## 📌 2. Jieba 中文斷詞三大模式與自訂詞典

```python
# ==============================================================================
# 範例程式 11-1：Jieba 三大斷詞模式與自訂專業辭典
# ==============================================================================
import jieba

sentence = "溫敏淦教授在國立聯合大學開設人工智慧與機器學習實務課程。"

# 1. 預設模式（精確模式 Accurate Mode）：最適合文本分析，無多餘重複詞
words_accurate = jieba.lcut(sentence)
print("1. 精確模式斷詞:", "/ ".join(words_accurate))

# 2. 全模式 (Full Mode)：把句子中所有可能的詞語都掃描出來，速度極快但冗餘
words_full = jieba.lcut(sentence, cut_all=True)
print("2. 全模式斷詞:  ", "/ ".join(words_full))

# 3. 搜尋引擎模式 (Search Engine Mode)：在精確模式基礎上，對長詞再次切分
words_search = jieba.lcut_for_search(sentence)
print("3. 搜尋模式斷詞:", "/ ".join(words_search))

# 4. 解決專有名詞被誤切問題：動態加入自訂詞彙
jieba.add_word("溫敏淦", freq=1000)
jieba.add_word("國立聯合大學", freq=1000)

words_custom = jieba.lcut(sentence)
print("4. 加入辭典後精確斷詞:", "/ ".join(words_custom))
```

---

## 📌 3. 停用詞 (Stopwords) 過濾與詞頻統計

在文字探勘中，「的」、「了」、「在」、「和」等虛詞無助於分析核心語意，必須建立**停用詞庫**過濾：

```python
# ==============================================================================
# 範例程式 11-2：停用詞過濾與 Counter 高頻詞統計
# ==============================================================================
from collections import Counter
import jieba

# 模擬新聞長篇文本
news_article = """
人工智慧技術近期快速突破，大型語言模型與生成式AI在全球科技產業引發熱潮。
國立聯合大學資管系溫敏淦教授強調，學生應掌握Python程式設計、爬蟲與機器學習基礎，
並能結合大數據分析與金融科技，才能在未來AI時代維持強大競爭力。人工智慧不僅是工具，
更是重塑商業模式與企業決策的核心科技。
"""

# 定義中文停用詞集合
stopwords = {
    "的", "了", "在", "和", "是", "與", "等", "及", "更", "並", 
    "能", "才能", "不僅", "近期", "一個", "。", "，", "、", "\n"
}

# 斷詞並過濾
words = jieba.lcut(news_article)
cleaned_words = [w.strip() for w in words if len(w.strip()) > 1 and w.strip() not in stopwords]

# 詞頻統計 (Frequency Distribution)
word_counts = Counter(cleaned_words)

print("=== 前 5 大最高頻核心關鍵詞 ===")
for word, count in word_counts.most_common(5):
    print(f"  關鍵詞: {word:<10} | 出現頻率: {count} 次")
```

---

## 📌 4. TF-IDF 關鍵字權重萃取與 WordCloud 文字雲生成

- **TF (Term Frequency, 詞頻)**：詞彙在當前文章出現的頻率。
- **IDF (Inverse Document Frequency, 逆文檔頻率)**：詞彙在全體語料庫中罕見程度之對數權重：
  $$TF\text{-}IDF = TF \times \log\left(\frac{N}{DF + 1}\right)$$

```python
# ==============================================================================
# 範例程式 11-3：TF-IDF 萃取與產生高解析度文字雲圖檔
# ==============================================================================
import jieba.analyse
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 1. 運用 Jieba 內建 TF-IDF 演算法萃取前 10 大關鍵詞
keywords = jieba.analyse.extract_tags(news_article, topK=10, withWeight=True)
print("=== TF-IDF 權重排行榜 ===")
for kw, weight in keywords:
    print(f"  詞彙: {kw:<8} | 權重: {weight:.4f}")

# 2. 構建文字雲輸入文字
text_for_cloud = " ".join(cleaned_words)

# 3. 配置 WordCloud（務必指定中文字型路徑，否則中文會變框框）
wc = WordCloud(
    font_path="C:/Windows/Fonts/msjh.ttc",   # 指定微軟正黑體
    width=800,
    height=500,
    background_color="white",
    max_words=100,
    colormap="viridis"
)

wc.generate(text_for_cloud)

# 儲存與繪製
wc.to_file("news_wordcloud.png")
print("✅ 中文文字雲已成功生成並儲存為 news_wordcloud.png！")
```
