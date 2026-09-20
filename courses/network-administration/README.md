# 🌐 電腦網路管理 (Network Administration / CCNA)

> **授課教師**：張朝旭 教授  
> **課程目標**：精熟 Cisco IOS CLI 操作、IP 定址與子網路規劃、靜態/動態路由協定 (RIPv2, EIGRP, OSPF)、VLAN/Trunking、存取控制清單 (ACL) 與 NAT 轉譯技術。

---

## 📑 全學期章節知識庫 (直至期末)

| 週次序號 | 主題名稱 | 核心重點綱要 | 狀態 |
| :---: | :--- | :--- | :---: |
| **W01** | [[W01-Cisco-CLI操作模式與常用指令]] | CLI 模式階層、`Ctrl+Shift+6` 終止鍵、`no ip domain-lookup`、密碼配置 | 🟢 完備 (含手寫重點) |
| **W02** | [[W02-光纖與序列介面設定實作]] | WIC-2T 模組、DCE 時脈 `clock rate 9600` vs DTE、Ping 符號代表意義 | 🟢 完備 (含手寫重點) |
| **W03** | [[W03-靜態路由與預設路由-初步筆記]] | 靜態路由語法、預設路由 `0.0.0.0 0.0.0.0`、浮動靜態路由 (Floating Static) | 🟡 課堂預備 |
| **W04** | [[W04-動態路由協定概論與RIP-初步筆記]] | IGP vs EGP、距離向量 vs 鏈結狀態、路由迴圈防止 (Split Horizon, Poison Reverse) | 🟡 課堂預備 |
| **W05** | [[W05-VLAN虛擬區域網路與Trunk-初步筆記]] | VLAN 廣播域切割、Access Port、802.1Q Trunk 標籤封裝 | 🟡 課堂預備 |
| **W06** | [[W06-單臂路由器與VLAN間路由-初步筆記]] | Router-on-a-Stick、子介面 (Sub-interfaces) 配置、802.1Q 封裝 | 🟡 課堂預備 |
| **W07** | [[W07-EIGRP繞送協定與DUAL-初步筆記]] | 複合度量值計算、可行距離 FD、回報距離 RD、可行性條件 FC | 🟡 課堂預備 |
| **W08** | [[W08-OSPF開放最短路徑優先-初步筆記]] | SPF 演算法、Cost 計算、Area 0 骨幹區域、Wildcard Mask | 🟡 課堂預備 |
| **W09** | [[W09-期中技術檢核與路由表除錯實踐]] | `show ip interface brief`, `show ip route`, `show cdp neighbors` 故障排查 | 🟡 課堂預備 |
| **W10** | [[W10-RIPv2無類別繞送與VLSM實作-初步筆記]] | RIPv1 vs RIPv2、關閉自動總結 `no auto-summary`、VLSM 支援 | 🟡 課堂預備 |
| **W11** | [[W11-尋徑表查找機制與最長匹配原則-初步筆記]] | 最長前綴匹配 (LPM)、管理距離 (AD) 優先權判定 | 🟡 課堂預備 |
| **W12** | [[W12-EIGRP進階配置與非等價負載平衡-初步筆記]] | DUAL 狀態機、非等價負載平衡 `variance` 倍數設定 | 🟡 課堂預備 |
| **W13** | [[W13-OSPF單一區域與多區域階層架構-初步筆記]] | 鄰居狀態機、DR/BDR 競選原則、多區域階層 LSA 概念 | 🟡 課堂預備 |
| **W14** | [[W14-存取控制清單ACL與流量過濾-初步筆記]] | 標準 ACL (靠目的) vs 擴展 ACL (靠來源)、隱含拒絕 (Implicit Deny) | 🟡 課堂預備 |
| **W15** | [[W15-網路位址轉譯NAT與PAT技術實務-初步筆記]] | 靜態 NAT、動態 NAT、PAT / NAT Overload 配置 | 🟡 課堂預備 |
| **W16** | [[W16-企業WAN廣域網路技術與期末總複習]] | 串列 WAN 封裝 HDLC vs PPP、PAP/CHAP 驗證、期末上機實作 Checklist | 🏆 考前衝刺 |
