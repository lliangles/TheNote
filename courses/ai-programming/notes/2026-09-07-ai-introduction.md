---
tags:
  - 人工智慧程式設計
  - 課程筆記
date: 2026-07-21
aliases:
---
## AI

- Artificial intelligence 
	1. Raw data 
	2. ==Processing== 
	3. information 
	4. ==Cognition== 
		- 認知的介入（外界刺激）
	5. Knowledge
	6. ==Pettern Extraction== 
		- 特定的樣態，理解知識
	7. Understanding 
	8. ==Inference==
	9. Intelligence 
- 何為圖靈測試
	- 自然語言處理NLP
	- knowledge representation 
	
## LLM
 - RIG 
	- 人工智慧無法自主學習資訊，需要另外擴充資料取得答案（例如網路搜尋）
- Data-> (processing Training Optimization ) ->ML
- Model type _prediction 
	- Classification  分類已知類別 ／Clustering 分群後加上標籤 ／Regression
	- SVM分類器／線性回歸
 - Nearrow AI 
	 - RIG 人工智慧無法自主學習資訊，需要另外擴充資料取得答案（例如網路搜尋）
- AGI (artificial general intelligence )  (String AI )
	
- Supervised 監督式
	- Regression (在？環境下的特地結果，如預測股票)
- semi - Supervised 半監督式
- Reinforcement 
	- Agent (policy/value function /model )
	- Exploration ／exploitation
- overfitting 問題解方
	- Dropout layer （訓練時）
		- 隨機關閉：在訓練階段，它會以指定的機率（Dropout Rate）隨機將神經元的輸出設為零。停止傳遞：被關閉的神經元不參與該次迭代的訊息傳遞與權重更新。
		- 減少依賴：它阻止神經元之間產生共同適應（Co-adaptation），也就是過度依賴特定神經元特徵的情況。模型組合：每次迭代等於訓練不同的子網路結構，提升模型的泛化能
	- Data argumentation 把圖片旋轉／加雜訊

1. 訓練參數定義
- **Batch size（批次大小）**：
    - 每次進行反向傳播（Backpropagation）修正權重之前，所累積的訓練樣本（Train pattern）數量。
- **Epoch（時期/世代）**：
    - 整個訓練資料集被完整反覆訓練模型的次數。
	
調整權重法
	- 何為Optimizer 
		- 最佳化修訂參數的方法
		- 誤差估算（loss functions )的設計
		梯度下降法（Gradient Descent, GD）、隨機梯度下降法（SGD）、Adam、RMSprop 等。
		利用微積分的偏微分計算出損失函數對各個參數的梯度，再根據學習率（Learning Rate）來更新權重- 
	- Activation functions （激活函數）設計
		- 從xy的線性關係-＞二維／指數模型
		- 加入神經網路中的非線性函數，讓模型可以學習複雜的模式。
		常見例子：ReLU、Sigmoid、Tanh

