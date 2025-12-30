# 12月26日 13-39 transcript（重點 + 你原本想講的「正確字詞」）

原檔只有幾行，但你在對話中其實已經描述了真正意圖：
- 你想用一個 beam tracking agent 以 **RSS per beam / RSRP** 做主要 observation
- 你不想把 CSI 當作線上依賴（太重/太難取得）
- 你想把 action 轉成「下一個 time slot 該用的 beam」

本 repo 因此將 Observation 的最小集合定為：
- `rsrp_vector`（per-beam）
- `prev_beam_id`（可選）
並保留 `csi_tensor` 作為 offline teacher 可用欄位。
