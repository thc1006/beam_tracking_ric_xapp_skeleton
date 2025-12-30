from __future__ import annotations
from dataclasses import dataclass
import torch

from .rsrp_student import RSRPStudentPolicy

@dataclass
class InferenceResult:
    target_beam_id: int
    confidence: float

class InferenceEngine:
    def __init__(self, n_beams: int, device: str = "cpu"):
        self.device = torch.device(device)
        self.policy = RSRPStudentPolicy(n_beams=n_beams).to(self.device)
        self.policy.eval()

    @torch.no_grad()
    def act(self, rsrp_vector: list[float]) -> InferenceResult:
        x = torch.tensor([rsrp_vector], dtype=torch.float32, device=self.device)
        logits = self.policy(x)
        probs = torch.softmax(logits, dim=-1)[0]
        beam = int(torch.argmax(probs).item())
        conf = float(probs[beam].item())
        return InferenceResult(target_beam_id=beam, confidence=conf)
