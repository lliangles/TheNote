RIP,EIGRP, OSPF


* RIP (Routing Information Protocol)：距離向量協定，以「跳數」（Hop Count，最大 15 跳）作為評估路徑優劣的標準，適合小型網路。
* EIGRP (Enhanced Interior Gateway Routing Protocol)：思科專有的進階距離向量協定，結合了鏈結狀態的優點，收斂速度快、頻寬消耗低。
* OSPF (Open Shortest Path First)：開放式最短路徑優先協定，屬於鏈結狀態協定，以 Dijkstra 演算法計算最佳路徑，適合大型與複雜的企業網路。
### find

Enable= en[[權限]]

CRIL +C ()跳過
Routing table  `show ip route` 可以看到位址

存檔路由表（避免關機重製）
`copy running-config startup-config（copy running-config sta)
(意思是把目前正在運行的設定，複製儲存到開機設定中，這樣關機才不會消失。)
`copy`run+tab st

關機才能插網卡
NM-1FE-FX
FX光纖(Fiber)
TX 雙角線(Twixed pair)=copper

預設情況下倆路由能互聯並不代表知道彼此的其他區網
`static 加入指令：ip route [遠方目標網路IP] [子網路遮罩] [近方下一跳IP 或輸出介面]`

- Copper

- 儲存後插入Serial (WIC2-T)
Serial (序列) 纜線
	- Serial DCE (有時間)  
	- Serial DTE）
Clock Rate 9600
今天實作接光纖及雙絞線及新增路由插孔？放網卡之後能插的變多了為什麼
這張圖片看起來是您在操作 Cisco Packet Tracer 或實體 Cisco 網路設備時的筆記。
您最後提出的問題是：「放網卡之後能插的變多了為什麼？」

##  💡 核心原因
因為您在路由器或交換器上安裝了擴充模組（Module）。
Cisco 的許多網路設備採用模組化設計（Modular Design）。設備出廠時，自帶的內建連接埠（例如固定的 Ethernet 或 FastEthernet 介面）數量通常很少。
當您在設備的空插槽（Slot）中，放進了您筆記中提到的網卡/模組時：

* NM-1FE-FX：增加了一個 FastEthernet 光纖介面。
* WIC2-T：增加了兩個 Serial（序列）介面。

這些插槽就像是電腦的主機板一樣，原本是空的空位（Slots），一旦您插上了擴充卡，設備就會動態識別並啟用新的物理介面。因此，您可以連接的線路（如光纖、雙絞線、Serial 序列線）和設備數量自然就變多了。

-----------------------------


這裡為您整理 [[光纖（乙太網路）介面 與 序列（Serial）介面 在 Cisco 設備上的完整設定指令]]。
#尚未練習
您可以直接在 Packet Tracer 中打開 CLI 界面，對照著進行實驗。
------------------------------
## 🟠 1. 光纖介面（NM-1FE-FX）設定指令
光纖介面屬於乙太網路（Ethernet）家族，在 Cisco 系統中通常顯示為 FastEthernet（例如 fa0/0 或 fa1/0）。它的設定非常單純，不需要設定封裝協定或時脈。

Router> enable                         ! 進入特權模式
Router# configure terminal             ! 進入全域設定模式
Router(config)# interface fa1/0        ! 進入光纖介面（請依據您的插槽編號調整）
Router(config-if)# ip address 192.168.1.1 255.255.255.0  ! 設定 IP 與子網路遮罩
Router(config-if)# no shutdown         ! 啟用介面（預設是關閉的）
Router(config-if)# exit

------------------------------
## 🔴 2. 序列介面（WIC2-T）設定指令
序列介面屬於廣域網路（WAN）。在 Packet Tracer 中用紅色閃電線連接時，必須區分 DCE（有時鐘標誌）與 DTE 端。
## 📍 情況 A：如果您接的是 DCE 端（有時鐘的一端）
DCE 端負責提供時脈，因此必須多一行 clock rate 指令。此外，Serial 介面需要指定廣域網的封裝協定（預設通常是 HDLC，這裡以常用的 PPP 協定 為例）：

Router> enable
Router# configure terminal
Router(config)# interface serial 0/0/0  ! 進入序列介面（請依據實際編號）
Router(config-if)# ip address 10.0.0.1 255.255.255.252  ! 設定 WAN IP
Router(config-if)# encapsulation ppp    ! 設定封裝協定為 PPP（兩端必須一致）
Router(config-if)# clock rate 64000     ! 【核心】DCE 端必須設定時脈速率
Router(config-if)# no shutdown          ! 啟用介面

## 📍 情況 B：如果您接的是 DTE 端（沒有時鐘的一端）
DTE 端會自動去同步 DCE 傳過來的速度，因此絕對不能設定 clock rate：

Router> enable
Router# configure terminal
Router(config)# interface serial 0/0/0  ! 進入對面的序列介面
Router(config-if)# ip address 10.0.0.2 255.255.255.252  ! 設定與對面同網段的 IP
Router(config-if)# encapsulation ppp    ! 封裝協定必須與 DCE 端相同
Router(config-if)# no shutdown          ! 啟用介面

------------------------------
## 🛠️ 實用檢查與除錯指令
當您把兩端都 no shutdown 之後，可以用以下指令在特權模式（#）檢查狀態：

* show ip interface brief
* 檢查所有介面的 IP 狀態。如果成功，Status 和 Protocol 應該都要顯示為 up / up。
* show controllers s0/0/0
* 如果您忘記哪一端是 DCE、哪一端是 DTE，輸入這個指令，第一行就會直接告訴您這台設備目前是 DCE 還是 DTE。

下一步需要我帶您把您的筆記串起來，利用這些介面來做靜態路由（ip route）的互聯實驗嗎？

