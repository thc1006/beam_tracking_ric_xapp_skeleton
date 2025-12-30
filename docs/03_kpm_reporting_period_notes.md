# KPM reporting period & PER fallback notes

你上傳的 `OSC_RIC-J_KPM_REPORTING_PERIOD_AND_PER_FALLBACK.pdf` 是針對：
- KPM subscription 的 reporting period
- 當 gNB / E2SIM 不支援某些觸發設定時的 fallback 行為（PER / event trigger）

本 repo 的落地點：
- `beam_tracking/ric/kpm_subscription.py`：定義 subscription request 結構（先 stub）
- `beam_tracking/xapp/observation_provider_kpm.py`：從 KPM Indication 萃取成 Observation（先 stub）

關鍵提醒：
- xApp 不應以 polling 方式「每 100ms 主動去要資料」
- 正確做法是：subscription request 中的 event trigger 指定 periodic + reporting period
