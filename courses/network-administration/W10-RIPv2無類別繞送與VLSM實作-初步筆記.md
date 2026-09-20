# 🌐 網管 W10: RIPv2 無類別繞送與 VLSM 實作 (Classless Routing & RIPv2)

> **授課教師**：張朝旭 教授  
> **教材對齊**：進度大綱第 10～11 週、Distance Vector Protocols  
> **核心主題**：RIPv1 (有類別 Classful) vs RIPv2 (無類別 Classless) 比較、VLSM (可變長度子網路遮罩) 傳遞、關閉自動總結 (`no auto-summary`)、RIPv2 認證與計步上限 (Hop Count 15)

---

## 1. RIPv1 vs RIPv2 核心差異

| 特性 | RIP Version 1 | RIP Version 2 |
| :--- | :---: | :---: |
| **路由類型** | 有類別 (Classful) | **無類別 (Classless)** |
| **子網路遮罩傳送** | **不傳送** Subnet Mask | **隨路由更新傳送** Subnet Mask |
| **支援 VLSM / CIDR** | 否 | **完全支援** |
| **廣播/群播位址** | 255.255.255.255 (全網廣播) | **224.0.0.9** (專屬群播 Multicast) |
| **安全認證** | 不支援 | 支援明文 (Plain Text) 與 **MD5 認證** |
| **度量值 (Metric)** | 跳數 (Hop Count，最大 15，16 為不可達) | 跳數 (Hop Count，最大 15) |

---

## 2. RIPv2 核心配置模板

```text
Router(config)# router rip
Router(config-router)# version 2                 ! 啟用版本 2
Router(config-router)# no auto-summary           ! 關鍵：關閉跨主類別自動總結，否則 VLSM 無法生效！
Router(config-router)# network 192.168.1.0       ! 宣告直連網段主類別位址
Router(config-router)# network 10.0.0.0
Router(config-router)# passive-interface Fa0/0   ! 阻止向使用者 LAN 廣播路由更新 (提升安全性與頻寬)
```

---

## 🎯 課堂速記與期末考檢核重點

```markdown
<!-- 上課重點即時填寫區 -->
> [!note] 課堂速記 (隨堂記錄張老師補充)
> - 
```
