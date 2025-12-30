# Decision matrix: CSI vs RSRP/RSS-per-beam

## 結論（本 repo 採用的「最穩妥」策略）
- **離線訓練**：用 CSI-heavy（teacher model）學到更細緻的 beam policy
- **線上部署**：用 RSRP/RSS-per-beam light（student model）做 inference
- 兩者用 **distillation** 串起來：teacher 產生動作分佈 → student 學習（再用少量真實數據微調）

## 為什麼這是最實務可行的？
### CSI-heavy（優點/缺點）
- 優點：資訊量最大，beam 追蹤上限高（尤其是相位/多徑結構）
- 缺點：在 RIC/E2 取得完整 CSI 通常成本極高、頻寬/延遲不划算，且不同 gNB vendor 的可得性差

### RSRP/RSS-per-beam（優點/缺點）
- 優點：更接近真實網路可取得的指標；可透過 KPM/PM 或 UE measurement report 取得
- 缺點：資訊較粗，可能需要更強的 temporal model（LSTM/GRU）與合理 state design

## Repo 如何支援兩者
- `beam_tracking/schemas.py` 定義 Observation: 同時允許 `rsrp_vector` 與 `csi_tensor`（optional）
- `beam_tracking/model/` 內提供兩個 encoder 入口（teacher / student）
- 後續你只要擴充 ObservationProvider（KPM provider / CSI provider）即可
