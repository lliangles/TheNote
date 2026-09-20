# 🌐 網管 W12: EIGRP 進階配置與非等價負載平衡 (Advanced EIGRP & DUAL)

> **授課教師**：張朝旭 教授  
> **教材對齊**：進度大綱第 13～14 週、EIGRP 協定深探  
> **核心主題**：複合度量值 (Metric) 計算公式、可行性條件 (Feasibility Condition, FC)、可行後繼者 (Feasible Successor, FS)、DUAL 狀態機、非等價負載平衡 (`variance`)

---

## 1. EIGRP 複合度量值公式 (Composite Metric)

EIGRP 預設採用**頻寬 (Bandwidth)** 與**延遲 (Delay)** 計算 Metric（$K_1=1, K_3=1, K_2=K_4=K_5=0$）：
$$\mathbf{\text{Metric} = 256 \times \left( \frac{10^7}{\text{Min Bandwidth (kbps)}} + \frac{\text{Total Delay (}\mu\text{s)}}{10} \right)}$$

---

## 2. DUAL 核心名詞與可行性條件 (FC 條件 - 必考)

- **可行距離 (Feasible Distance, FD)**：本地路由器到達目的地的**最佳總度量值**。
- **回報距離 (Reported Distance, RD)**：相鄰鄰居路由器向本地回報它自己到達目的地的度量值。
- **後繼者 (Successor)**：通往目的地的主要下一跳路由器（FD 最低者）。
- **可行後繼者 (Feasible Successor, FS)**：備援下一跳路由器。成為 FS 必須滿足**可行性條件 (FC)**：
  $$\mathbf{RD_{\text{備援}} < FD_{\text{當前最佳}}}$$
  *(意義：備援鄰居離目的地的距離比我自己當前的最佳距離還要短，保證該鄰居絕不可能回頭繞過我自己，徹底杜絕 Routing Loop！)*

---

## 3. 非等價負載平衡 (`variance`)
多數協定僅支援等價負載平衡 (Equal-cost)。EIGRP 是唯一支援非等價負載平衡的協定：
```text
Router(config-router)# variance 2
```
只要滿足 FC 條件的備援路徑，其 Metric 小於等於 `FD * variance`，即可同時納入尋徑表進行流量分擔！

---

## 🎯 課堂速記與期末考檢核重點

```markdown
<!-- 上課重點即時填寫區 -->
> [!note] 課堂速記 (隨堂記錄張老師補充)
> - 
```
