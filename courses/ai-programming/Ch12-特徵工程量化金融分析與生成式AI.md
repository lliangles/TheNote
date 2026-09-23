# 🚀 Ch12 電腦視覺、車牌辨識系統與多模態生成式 AI 實務

> **授課教師**：溫敏淦 教授  
> **對應教材**：`F1700_ch10.pptx`、課堂專題實作  
> **重點導讀**：系統化貫穿電腦視覺 (Computer Vision) 與邊緣運算：OpenCV 影像讀取與縮放 (`imread`, `resize`, `imwrite`)、攝影機即時視訊串流採集 (`VideoCapture`, `waitKey` 鍵盤事件、資源釋放 `release`)、雲端電腦視覺 OCR API 介接（二進位串流 POST 請求與輪詢）、**車牌號碼正規表達式精準過濾 (`r'^[\w]{2,4}[-. ][\w]{2,4}$'`)**，以及比較傳統 OCR 與現代多模態生成式 AI (VLM: Vision-Language Model) 在智慧交通監控之典範轉移。

---

## 📌 1. OpenCV 影像處理基礎與視訊串流採集

> [!IMPORTANT] 簡報第 10 章第 3~20 頁 OpenCV 核心操作
> OpenCV (`cv2`) 是電腦視覺領域最強大且廣泛使用的開源函式庫，影像在 Python 中直接以 NumPy 的 `ndarray` 形式儲存（BGR 顏色空間排列）。

### 1-1. 影像讀取、縮放與儲存三大步驟
1. **`cv2.imread(path, flags)`**：讀取影像，預設為彩色 BGR；可傳入 `cv2.IMREAD_GRAYSCALE` 讀取為單通道灰階影像。
2. **`cv2.resize(src, (new_w, new_h))`**：注意！OpenCV 的尺寸元組順序為 **`(寬度 Width, 高度 Height)`**，與 NumPy 的 `(Rows, Cols)` 正好相反！
3. **`cv2.imwrite(path, img)`**：將矩陣儲存為 JPG、PNG 檔案。

### 1-2. 攝影機即時影像串流與鍵盤事件監控
* **`cv2.VideoCapture(0)`**：建立攝影機物件（`0` 代表本機第一台預設攝影機）。
* **`cap.isOpened()`**：檢查攝影機硬體是否成功啟用。
* **`ret, frame = cap.read()`**：從視訊流中擷取當前影格（`ret` 為布林值表示是否讀取成功，`frame` 為當前影格影像陣列）。
* **`cv2.waitKey(delay)` 核心規則**：
  * 若傳入 `0`：無限期暫停，直到使用者按下任意鍵為止。
  * 若傳入正整數 $n$：等待 $n$ 毫秒，期間若有按鍵則傳回該按鍵的 ASCII 碼值，無按鍵則傳回 -1。
  * **退出條件樣板**：`if cv2.waitKey(1) & 0xFF == ord('q'): break`（按下鍵盤 `q` 退出迴圈）。
* **資源釋放鐵律**：使用完畢必須執行 `cap.release()` 與 `cv2.destroyAllWindows()`，防止相機被作業系統死鎖！

```python
# ==============================================================================
# 範例程式 12-1：OpenCV 攝影機即時監控與拍照儲存
# ==============================================================================
import cv2

def run_camera_capture():
    # 1. 建立攝影機物件
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("❌ 無法開啟攝影機設備！")
        return

    print("📷 攝影機已啟動，按 'c' 拍照存檔，按 'q' 退出程式...")

    photo_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            print("無法接收視訊影格，終止連線。")
            break

        # 顯示影像於名為 'Camera View' 的視窗
        cv2.imshow("Camera View", frame)

        # 監聽鍵盤按鍵事件
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            # 按下 'q' 退出無窮迴圈
            break
        elif key == ord('c'):
            # 按下 'c' 觸發拍照存檔
            photo_count += 1
            filename = f"captured_car_{photo_count:02d}.jpg"
            # 縮放至標準尺寸 (寬 800, 高 600)
            resized_frame = cv2.resize(frame, (800, 600))
            cv2.imwrite(filename, resized_frame)
            print(f"✅ 已成功拍攝並存檔: {filename}")

    # 釋放相機硬體與銷毀所有視窗
    cap.release()
    cv2.destroyAllWindows()
    print("相機資源已安全釋放。")
```

---

## 📌 2. 雲端電腦視覺 OCR API 與二進位影像傳輸

> [!IMPORTANT] 簡報第 10 章第 28~37 頁 API 傳輸規範
> 本地端模型常受限於邊緣運算效能，透過雲端 Computer Vision RESTful API 能以高準確率萃取圖片中的文字：

### 2-1. 二進位串流傳送格式
* **HTTP Method**：`POST`
* **請求標頭 (Headers)**：
  ```python
  headers = {
      "Content-Type": "application/octet-stream",  # 指定傳送內容為純二進位影像
      "Ocp-Apim-Subscription-Key": "YOUR_API_KEY"  # 伺服器身分驗證金鑰
  }
  ```
* **請求主體 (Body)**：傳入經過二進位編碼的影像位元組（`img_bytes`）。

### 2-2. 非同步作業輪詢 (Asynchronous Polling)
由於高解析度影像 OCR 運算需要數百毫秒至數秒：
1. 伺服器第一時間回傳 `HTTP 202 Accepted`，並在 Header 提供 `Operation-Location` URL。
2. 客戶端進入 `while` 輪詢迴圈，搭配 `time.sleep(1)` 每隔一秒向該 URL 查詢進度。
3. 當回傳的 JSON 中 `status` 轉變為 `"succeeded"` 時，即可取出最終解析出的文字陣列。

---

## 📌 3. 車牌號碼正規表達式精準過濾 (License Plate Regex)

> [!CAUTION] 簡報第 10 章第 38 頁關鍵演算法
> OCR 解析結果往往包含街景招牌、警示標語、廣告貼紙等雜訊文字。必須透過精準的正規表達式 (Regex) 進行特徵比對，才能精準過濾出唯一的車牌號碼！

### 台灣車牌格式正規表達式：
$$r'\text{\textasciicircum}[\backslash w]\{2,4\}[-. ][\backslash w]\{2,4\}\$ '$$

* **語法結構剖析**：
  * `^` 與 `$`：嚴格錨定字串開頭與結尾，不匹配中間子字串。
  * `[\w]{2,4}`：前半段為 2 到 4 個英數字元（如舊制 `AB`、`123`，新制 `ABC`、`1234`）。
  * `[-. ]`：車牌中間的分隔連字號、圓點或空格（如 `ABC-1234` 或 `9876-AA`）。
  * `[\w]{2,4}`：後半段為 2 到 4 個英數字元。

```python
# ==============================================================================
# 範例程式 12-2：車牌號碼正規過濾演算法實作
# ==============================================================================
import re

def filter_license_plate(ocr_text_lines: list[str]) -> list[str]:
    """
    從 OCR 辨識出的文字清單中，篩選出符合台灣車牌格式的字串
    """
    # 簡報指定車牌正規表達式
    plate_pattern = re.compile(r"^[\w]{2,4}[-. ][\w]{2,4}$", re.IGNORECASE)
    valid_plates = []

    for line in ocr_text_lines:
        cleaned_line = line.strip()
        # 進行正規比對
        if plate_pattern.match(cleaned_line):
            valid_plates.append(cleaned_line)

    return valid_plates

# 測試雜訊文字清單
mock_ocr_results = [
    "歡迎光臨停車場",
    "限高 2.1 公尺",
    "ABC-5678",       # ✅ 合法車牌
    "0800-092-000",   # ❌ 電話號碼 (多段)
    "9988-XY",        # ✅ 合法車牌
    "TOYOTA",         # ❌ 廠牌名稱
    "AB 1234"         # ✅ 空格分隔合法車牌
]

detected = filter_license_plate(mock_ocr_results)
print(f"🎉 成功過濾辨識出車牌: {detected}") # ['ABC-5678', '9988-XY', 'AB 1234']
```

---

## 📌 4. 傳統 OCR 系統 vs 多模態生成式 AI (VLM) 典範轉移

在現代人工智慧架構中，車牌辨識與智慧安防已從「OpenCV + 傳統 OCR + Regex」逐步邁向「多模態大型語言模型 (Vision-Language Models, VLM)」：

| 評估維度 | 傳統架構 (OpenCV + OCR + Regex) | 現代多模態架構 (VLM: Gemini / GPT-4o) |
|:---|:---|:---|
| **核心技術** | 邊緣檢測 + 字符模板匹配 + 正則規則 | 巨量參數多模態 Transformer 視覺語言模型 |
| **抗干擾能力** | 易受天候、雨水反光、髒污或傾斜角度影響 | **極強上下文推論能力**，輕微遮擋或髒污仍可準確推論 |
| **任務範疇** | 僅能讀取固定字元文字 | **端到端一網打盡**：同時辨識車牌、車輛品牌、車身顏色、車型及違規行為 |
| **運算成本** | 本地 CPU 即可運行，成本極低、速度快 (幾十毫秒) | 需要 GPU 或雲端 API 調用，具備一定延遲與 API 成本 |

```python
# ==============================================================================
# 範例程式 12-3：現代多模態 VLM 結構化車牌與車輛屬性辨識 (概念樣板)
# ==============================================================================
def vlm_vehicle_inspection_prompt() -> str:
    """建構多模態模型 Prompt 提示詞"""
    prompt = """
    請分析這張停車場監視器照片中的車輛，並以 JSON 格式精確回傳以下資訊：
    {
      "license_plate": "車牌號碼 (格式: ABC-1234)",
      "vehicle_brand": "車輛品牌 (如 Toyota, Tesla)",
      "vehicle_color": "車身外觀顏色",
      "vehicle_type": "車型 (如 轎車, 休旅車, 貨車)",
      "confidence": "辨識信心分數 (0.0~1.0)"
    }
    """
    return prompt.strip()
```
