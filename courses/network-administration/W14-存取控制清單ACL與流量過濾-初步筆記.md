# 🌐 網管 W14: 存取控制清單 ACL 與流量過濾 (Access Control Lists)

> **授課教師**：張朝旭 教授  
> **教材對齊**：進度大綱 Filtering Traffic Using ACL  
> **核心主題**：標準 ACL (Standard 1-99) vs 擴展 ACL (Extended 100-199)、ACL 擺放黃金原則、隱含拒絕 (Implicit Deny Any)、Inbound vs Outbound 套用方向

---

## 1. 標準 ACL vs 擴展 ACL

| 比較項目 | 標準 ACL (Standard) | 擴展 ACL (Extended) |
| :--- | :--- | :--- |
| **編號範圍** | **1～99** 及 1300～1999 | **100～199** 及 2000～2699 |
| **檢查依據** | **僅檢查來源 IP 位址** | **來源 IP、目的 IP、協定 (TCP/UDP/ICMP)、通訊埠 (Port)** |
| **擺放最佳位置** | **儘量靠近目的地 (Near Destination)** | **儘量靠近來源端 (Near Source)** |
| **典型配置** | `access-list 10 permit 192.168.1.0 0.0.0.255` | `access-list 101 permit tcp any host 10.1.1.1 eq 80` |

> [!WARNING]
> **隱含拒絕 (Implicit Deny Any)**：
> 任何 ACL 的最末端皆預設隱含一道 `deny any`！若未設定任何 `permit` 規則，所有流量將被全數丟棄！

---

## 🎯 課堂速記與期末考檢核重點

```markdown
<!-- 上課重點即時填寫區 -->
> [!note] 課堂速記 (隨堂記錄張老師補充)
> - 
```
