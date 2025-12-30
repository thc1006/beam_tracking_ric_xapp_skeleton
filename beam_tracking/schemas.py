from __future__ import annotations
from typing import List, Optional, Literal
from pydantic import BaseModel, Field

class Observation(BaseModel):
    # minimum required for online deployment
    ue_id: str = Field(..., description="UE identifier (IMSI/RNTI/etc depending on config)")
    t: Optional[int] = Field(None, description="Time step index (optional)")
    rsrp_vector: List[float] = Field(..., description="Per-beam RSRP/RSS, dBm. Length = N_BEAMS")
    prev_beam_id: Optional[int] = Field(None, description="Beam used at previous step (optional)")

    # optional CSI-heavy path (offline training / simulation)
    csi_tensor: Optional[list] = Field(
        None, description="Optional CSI tensor (nested lists) for offline/teacher training"
    )

class Action(BaseModel):
    target_beam_id: int = Field(..., ge=0, description="Selected beam index")
    # Optional continuous-ish head (e.g., angle bucket)
    target_beam_angle_bucket: Optional[int] = Field(None, description="Angle bucket index (optional)")
    confidence: Optional[float] = Field(None, ge=0.0, le=1.0, description="Optional confidence")

class ControlRequest(BaseModel):
    ue_id: str
    action: Action
    # allow future mapping to RC styles or message IDs
    control_style: Optional[int] = None
