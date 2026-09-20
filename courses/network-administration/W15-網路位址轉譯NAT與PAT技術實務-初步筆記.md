# 🌐 網管 W15: 網路位址轉譯 NAT 與 PAT 技術實務 (NAT & PAT)

> **授課教師**：張朝旭 教授  
> **教材對齊**：進度大綱 IP Addressing & Enterprise Links  
> **核心主題**：IPv4 私有位址範圍 (RFC 1918)、靜態 NAT (1:1)、動態 NAT (M:N)、PAT / NAT Overload (連接埠轉譯)、Inside Local/Global 與 Outside Local/Global 定義

---

## 1. NAT 四大術語與位址定義

```text
內部私網 (LAN) ──────── [ NAT 路由器 ] ──────── 外部公網 (Internet)
Inside Local           Inside Global           Outside Global
(私有 IP: 192.168.1.5)  (公網 IP: 203.0.113.1)  (伺服器 IP: 8.8.8.8)
```

1. **Inside Local (內部本地)**：指派給私網內部主機的 IP（通常為私有位址，如 `192.168.x.x`, `10.x.x.x`）。
2. **Inside Global (內部全域)**：由 ISP 指派之合法的公開 IP，代表內部主機對外溝通。
3. **Outside Global (外部全域)**：網際網路上目標主機的合法公開 IP。

---

## 2. PAT (Port Address Translation / NAT Overload) 配置範例

```text
Router(config)# interface FastEthernet0/0
Router(config-if)# ip nat inside                 ! 標記內部介面
Router(config)# interface Serial0/0/0
Router(config-if)# ip nat outside                ! 標記外部介面

Router(config)# access-list 1 permit 192.168.1.0 0.0.0.255
Router(config)# ip nat inside source list 1 interface Serial0/0/0 overload
! 關鍵關鍵字 overload：多台內部私有 IP 共享同一外部介面 IP，透過不同 Port 號區分！
```

---

## 🎯 課堂速記與期末考檢核重點

```markdown
<!-- 上課重點即時填寫區 -->
> [!note] 課堂速記 (隨堂記錄張老師補充)
> - 
```
