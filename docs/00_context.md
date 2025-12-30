# Context & requirements (from this session)

你在這個 session 的核心需求可以拆成三條線：

1) **RC xApp 通訊流程驗證**
- 你想要一條「外部可呼叫的通道」（你提到像 gRPC），把 **Target Handover Cell ID / Target Beam ID** 這類控制指令餵給 RC xApp
- RC xApp 負責把這些參數塞進 **E2SM RC ASN.1**，再透過 **E2TERM/RMR** 送到 **E2SIM/gNB**

2) **KPM reporting / periodic reporting 的正確方式**
- 你已經注意到「while(true) polling」可能是錯的
- 希望 xApp 以 **E2 Subscription 的 Event Trigger (Periodic) + Reporting Period** 取得週期性報告

3) **Beam tracking ML/RL 的落地**
- 你提供了兩個模型來源：
  - `RL架構.pdf`：Actor-Critic / LSTM+CNN / Gumbel-Softmax / tanh angle head
  - `sionna_beam_tracking_v2.py`：Sionna CSI + candidate beams + encoder + policy/value（但程式內部有架構不一致之處）
- 你也在逐字稿中提到：最想用的觀測是 **RSS per beam / RSRP**（比 CSI 更容易在真實系統取得）

本 repo 的設計目標：**先讓你端到端跑通（sim → RC gRPC → RIC control），再逐步把 observation 換成真實來源。**
