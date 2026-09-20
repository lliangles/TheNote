# W05 RIP 路由協定實作 (RIPv1 and RIPv2 Protocols) - 初步筆記

> [!NOTE] 課程資訊與學習目標
> - **授課進度**：第 6~8, 10~11 週課程
> - **核心目標**：掌握 RIP 運作機制與 Hop Count 限制、熟記距離向量五大防環機制、精通 RIPv2 CLI 配置與關閉自動彙總。

---

## 1. RIP 基礎特性與限制

- **度量值 (Metric)**：以 **跳數 (Hop Count)** 衡量路徑優劣，每經過一台路由器跳數加 1。
- **最大跳數上限**：**最大有效跳數為 15 跳，16 跳視為不可達（Unreachable）**。
- **更新週期**：預設每隔 **30 秒** 定期廣播/多播路由更新。

### RIPv1 vs. RIPv2 差異對照：

| 特性 | RIPv1 | RIPv2 |
|:---|:---|:---|
| **路由類型** | 有類別路由 (Classful) | **無類別路由 (Classless)** |
| **VLSM 與 CIDR**| 不支援（不攜帶子網路遮罩） | **完整支援（攜帶子網路遮罩）** |
| **通告傳送方式**| 廣播 `255.255.255.255` | **多播 `224.0.0.9`** |
| **安全認證** | 無 | 支援 MD5 雜湊金鑰認證 |

---

## 2. 距離向量五大防環機制 (Loop Prevention Mechanisms)

> [!TIP] 期中考經典問答題
> 1. **最大跳數限制 (Max Hop Count)**：限制封包最多 15 跳，防止無窮迴圈消耗全網頻寬。
> 2. **水平分割 (Split Horizon)**：從某一介面學到的路由資訊，絕不再從同一個介面反向廣播回去。
> 3. **毒性反轉 (Poison Reverse)**：當某網路斷線時，主動將該路由跳數標記為 16（Poisoned），並立即回傳給鄰居使其更新。
> 4. **抑制定時器 (Holddown Timers)**：當收到路徑失效通告後，啟動 180 秒計時器，在此期間內拒絕接受任何劣質或不穩定的新路徑資訊。
> 5. **觸發更新 (Triggered Updates)**：一旦拓撲發生變更立即廣播更新，不需苦等 30 秒週期。

---

## 3. Cisco CLI RIPv2 配置實作範本

```cisco
Router# configure terminal
Router(config)# router rip
Router(config-router)# version 2             ! 啟用 Version 2
Router(config-router)# no auto-summary       ! 務必關閉自動彙總 (以完整支援 VLSM)
Router(config-router)# network 192.168.1.0   ! 宣告直連的主類別網段 (Classful Network)
Router(config-router)# network 10.0.0.0
Router(config-router)# exit
```

---

## 📌 隨堂註記 / 老師口述補充

> [!NOTE] 隨堂筆記區
> - 上課即時補充重點區。
