#課堂實作範本
這裡為您整理 光纖（乙太網路）介面 與 序列（Serial）介面 在 Cisco 設備上的完整設定指令。
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

為了讓你更清楚如何將講義中的 DCE 與 DTE 介面串聯並設定靜態路由，我為你設計了一個經典的雙路由器互聯拓樸。
## 🌐 網路拓樸設計

  【 內部網路 A 】                                                      【 內部網路 B 】
   192.168.1.0/24                                                       192.168.2.0/24
         │                                                                    │
         │ fa1/0 (.254)                                                       │ fa1/0 (.254)
   ┌─────┴─────┐           廣域網路 (WAN) 10.0.0.0/30           ┌─────┴─────┐
   │ Router A  ├────────────────────────────────────────┤ Router B  │
   └───────────┘  Serial 0/0/0                     Serial 0/0/0  └───────────┘
                  (DCE 端)                             (DTE 端)
                  IP: 10.0.0.1                     IP: 10.0.0.2
                  [需設定 clock rate]              [不設定 clock rate]

------------------------------
## 📝 靜態路由（ip route）範例設定
當兩台路由器的基礎介面（IP、封裝、DCE時鐘）都按照你講義的步驟啟動（no shutdown）後，此時 Router A 還不知道內部網路 B 的存在，Router B 也不知道內部網路 A 的存在。此時就必須使用靜態路由讓雙方互通。
## 1. Router A 的靜態路由設定
Router A 需要知道如何前往右側的 192.168.2.0/24 網段，它的下一個跳板（Next-hop）就是 Router B 的 Serial 介面 IP（10.0.0.2）。

Router A> enable
Router A# configure terminal
Router A(config)# ip route 192.168.2.0 255.255.255.0 10.0.0.2
Router A(config)# exit
Router A# write

## 2. Router B 的靜態路由設定
同理，Router B 需要知道如何前往左側的 192.168.1.0/24 網段，它的下一個跳板（Next-hop）就是 Router A 的 Serial 介面 IP（10.0.0.1）。

Router B> enable
Router B# configure terminal
Router B(config)# ip route 192.168.1.0 255.255.255.0 10.0.0.1
Router B(config)# exit
Router B# write

------------------------------
## 🔍 檢查與驗證指令
設定完成後，你可以在任何一台路由器的特權模式（#）下輸入以下指令來檢查路由表：

* 指令： show ip route
* 預期結果： 你會在路由表中看到一條開頭為 S（代表 Static 靜態路由）的條目，例如在 Router A 上會看到：
S 192.168.2.0/24 [1/0] via 10.0.0.2

最後，你可以嘗試從連接在 Router A 底下的電腦，去 ping 10.0.0.2 或 ping 192.168.2.254，如果回應成功，就代表靜態路由已經成功互聯了！
------------------------------
請問這個範例符合你的實驗需求嗎？接下來你想了解預設路由（Default Route）的設定方法，還是直接進入 Packet Tracer 實作呢？

