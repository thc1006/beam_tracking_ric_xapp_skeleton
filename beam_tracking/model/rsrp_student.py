from __future__ import annotations
import torch
import torch.nn as nn

class RSRPStudentPolicy(nn.Module):
    """Lightweight policy for online use.

    Input: rsrp_vector shape (B, N_BEAMS)
    Output: logits over beams (B, N_BEAMS)
    """
    def __init__(self, n_beams: int):
        super().__init__()
        self.n_beams = n_beams
        self.net = nn.Sequential(
            nn.Linear(n_beams, 128),
            nn.ReLU(),
            nn.Linear(128, 128),
            nn.ReLU(),
            nn.Linear(128, n_beams),
        )

    def forward(self, rsrp: torch.Tensor) -> torch.Tensor:
        if rsrp.ndim != 2 or rsrp.shape[1] != self.n_beams:
            raise ValueError(f"Expected rsrp (B,{self.n_beams}), got {tuple(rsrp.shape)}")
        return self.net(rsrp)
