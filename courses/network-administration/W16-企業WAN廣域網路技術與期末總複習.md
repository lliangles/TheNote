# 🌐 網管 W16: 企業 WAN 廣域網路技術與期末總複習 (WAN Technologies & Final Review)

> **授課教師**：張朝旭 教授  
> **教材對齊**：進度大綱 Implementing Enterprise WAN Links、期末考總整  
> **核心主題**：WAN 協定封裝 (HDLC vs PPP)、PPP 驗證機制 (PAP 明文 vs CHAP 三向交握挑戰)、CCNA 實驗室期末上機檢定必背指令全彙整

---

## 1. 點對點串列 WAN 協定：HDLC vs PPP

- **HDLC (High-Level Data Link Control)**：Cisco 路由器串列線路的**預設封裝**。Cisco 專屬封裝包含私有欄位，無法與非 Cisco 設備直連。
- **PPP (Point-to-Point Protocol)**：開放標準協定，支援多協定負載、鏈結品質監控及身分驗證。

### PPP 認證兩大協定：
1. **PAP (Password Authentication Protocol)**：**兩向認證，明文傳送帳號密碼**，易被竊聽，安全性低。
2. **CHAP (Challenge Handshake Authentication Protocol)**：**三向交握 (Three-Way Handshake)，傳送 MD5 雜湊值**，密碼永不在網路上傳輸，安全性極高。

---

## 2. CCNA 期末技術上機實作必備 Checklist
- [ ] 基礎安全配置：`enable secret`, `line console 0`, `banner motd`, `service password-encryption`
- [ ] 靜態與浮動靜態路由配置：`ip route 0.0.0.0 0.0.0.0 [next-hop]`
- [ ] VLAN 與 Trunk 配置：`switchport mode trunk`, `switchport trunk allowed vlan`
- [ ] 單臂路由器 (Router-on-a-Stick)：子介面 `encapsulation dot1Q [vlan-id]`
- [ ] OSPF 單一區域：`router ospf 1`, `network [net] [wildcard] area 0`
- [ ] NAT Overload 實作：`ip nat inside source list 1 interface S0/0/0 overload`
