# sionna_beam_tracking_v2.py 快速 code review（重點問題 + 重構建議）

## 你提供的檔案裡面，最值得注意的「會卡住整合」問題
1) **架構不一致 / 參數對不上**
   - 檔案中同時出現 `BeamTrackingFeatureEncoder/Backbone` 與 `PolicyNetwork/ValueNetwork` 的兩套路徑
   - `BeamTrackingAgent` 內部也有呼叫參數型別不一致的情況
   - 這會讓「訓練 / inference」很難拆乾淨

2) **Observation 形式偏 CSI-heavy**
   - 設計上以 (T,273,32) 的 CSI tensor 做 encoder
   - 但你逐字稿表示更想用 `RSS per beam / RSRP`

## 本 repo 的重構策略
- 先定義乾淨的資料介面：
  - `Observation`（可 optional CSI / 必備 RSRP vector）
  - `Action`（target_beam_id / optional beam_angle）
- 把 model 拆成兩條：
  - teacher (CSI) — offline
  - student (RSRP) — online
- 再把「控制下發」抽象成 `ActionDispatcher`：
  - 目前用 RC xApp gRPC
  - 未來可替換成 direct RMR / direct ASN.1 encode

