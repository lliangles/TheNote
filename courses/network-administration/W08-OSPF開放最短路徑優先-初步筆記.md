# W08 OSPF 開放最短路徑優先 (Open Shortest Path First) - 初步筆記

> [!NOTE] 課程資訊與學習目標
> - **授課進度**：第 15~16 週課程
> - **核心目標**：掌握 OSPF 鏈路狀態通告（LSA）與 Dijkstra 演算法、熟悉階層式 Area 0 骨幹架構、精通 Router ID 決定順序與 DR/BDR 選舉機制。

---

## 1. OSPF 基本概念

- **鏈路狀態協定 (Link-State Protocol)**：每台路由器透過交換 LSA（Link-State Advertisement），在本地建構出一張完整的**全網拓撲資料庫（LSDB）**。
- **Dijkstra SPF 演算法**：以自己為樹根，計算到達各網段的最短路徑樹。
- **Cost（度量值）計算公式**：
  $$\text{Cost} = \frac{\text{Reference Bandwidth (預設 100 Mbps)}}{\text{介面頻寬 (bps)}}$$

---

## 2. 路由器 ID (Router ID, RID) 決定三大順序

OSPF 識別每台設備的 32-bit 唯一標識，決定順序如下：
1. **手動設定**：`router-id x.x.x.x` 指令優先權最高。
2. **最高 Loopback 介面 IP**：若無手動指定，取已啟動之 Loopback 介面中 IP 數值最高者。
3. **最高實體活動介面 IP**：若無 Loopback，取已啟動之實體介面中 IP 數值最高者。

---

## 3. 多重存取網路上的 DR / BDR 選舉機制

在乙太網路等廣播多重存取環境中，若每台路由器皆相互建立鄰接關係，將產生 $\frac{n(n-1)}{2}$ 個鄰接，導致 LSA 廣播風暴。
- **解決方案**：選舉出一位 **DR (Designated Router, 指定路由器)** 與一位 **BDR (Backup DR, 備援指定路由器)**。
- 所有一般路由器（DROther）僅與 DR / BDR 建立 Full 鄰接關係：
  - DROther 送出 LSA 至多播位址 **`224.0.0.6`**（所有 DR 監聽）。
  - DR 收集後，透過多播位址 **`224.0.0.5`** 轉發給所有路由器。

---

## 4. Cisco CLI 單區域 OSPF 基本配置

```cisco
Router# configure terminal
Router(config)# router ospf 1
Router(config-router)# router-id 1.1.1.1
! 注意：OSPF 使用反向遮罩 (Wildcard Mask)
Router(config-router)# network 192.168.1.0 0.0.0.255 area 0
Router(config-router)# network 10.0.0.0 0.0.0.3 area 0
Router(config-router)# exit
```

---

## 📌 隨堂註記 / 老師口述補充

> [!NOTE] 隨堂筆記區
> - 上課即時補充重點區。
