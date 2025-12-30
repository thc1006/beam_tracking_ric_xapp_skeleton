# Beam Tracking RIC xApp (skeleton)

這個 repo 是給你用 **Claude Code** 開發的「乾淨專案骨架」：
- **ML/RL beam tracking**（支援 CSI-heavy 與 RSRP-light 兩種 observation）
- 與 **OSC RIC / RC xApp** 整合（以 gRPC 把 action 交給 RC xApp 進行 **E2SM RC ASN.1 encode + RMR 下發**）
- 同時保留「直接走 RMR/E2AP」的擴充點（未來你想自己 encode E2SM 也可以）

> 你提供的檔案（`RL架構.pdf`、`sionna_beam_tracking_v2.py`、逐字稿、KPM reporting notes）都已放在 `resources/original/`，並被整理成 `docs/` 的設計決策與工作分解，方便 Claude Code 直接引用。

---

## 快速開始

```bash
make bootstrap
make test
make run-sim
```

### 需要的外部 repos（由腳本拉取，不會污染本 repo）
- `o-ran-sc/ric-app-rc`（RC xApp：提供 gRPC → E2SM RC control → RMR/E2 node）
- 你自己的 `OSC RIC` 環境 / `E2SIM` / `gNB`（取決於你實驗）

```bash
bash scripts/bootstrap_external_repos.sh
```

---

## 你現在可以用 Claude Code 做什麼？

建議從這三件開始（repo 內有 `/commands`）：
1. `/plan-impl`：讓 Claude 依照 docs 產生可執行的開發計畫
2. `/gen-rc-protos`：從 `ric-app-rc` 抽 proto 生成 Python gRPC stub
3. `/wire-observation`：把「KPM/PM 指標」或「RSS per beam」接到 `Observation`，跑通 sim→ric 的 end-to-end

---

## 目錄

- `beam_tracking/`：主要 Python package
  - `model/`：policy/value network（先做 inference-ready）
  - `ric/`：RC gRPC client / (future) RMR client / KPM parsing stubs
  - `xapp/`：xApp main loop / state store / action dispatcher
  - `sim/`：離線模擬環境（快速測試 pipeline）
- `docs/`：交叉分析 + 設計決策 + TODO 拆解
- `.claude/commands/`：Claude Code slash commands
- `.claude/skills/`：Claude Code agent skills（自動觸發的規範/知識）
- `resources/original/`：你上傳的原始檔案

