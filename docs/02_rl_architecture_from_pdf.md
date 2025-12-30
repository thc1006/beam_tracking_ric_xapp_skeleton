# RL架構.pdf（圖）整理

你提供的 RL 架構圖（page1/page2）核心資訊（人工整理）：

- Discount factor: **gamma = 0.9**
- Value loss：使用 target network Q'（看起來是 off-policy actor-critic / DDPG-ish 變體）
- Feature extraction：**LSTM → 1D Conv + ReLU → MaxPool → Flatten**
- State 定義（page2）：input size **302**
  - RSS per beam（可能是 77 beams）
  - Channel coefficient / estimator features
  - Previous used beam id
- Policy network 1（beam index）：250 → 512 → 256 → 128 → 77 → Gumbel → 77
- Policy network 2（beam angle）：250 → 1024 → 512 → 256 → 154 → tanh → 154
- Value network：input **481 = 250 + 77 + 154**，之後多層 FC + dropout → 1

本 repo 會把這些拆成：
- `model/encoders.py`：LSTM+Conv feature backbone
- `model/policy_heads.py`：beam-id head / angle head
- `model/value.py`：critic

> 注意：你上傳的 `sionna_beam_tracking_v2.py` 與此 PDF 架構不完全一致，因此本 repo 不直接照抄，而是抽象成「teacher/student」兩種可插拔 encoder/head。
