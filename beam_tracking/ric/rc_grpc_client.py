from __future__ import annotations
import time
from dataclasses import dataclass
from typing import Optional

import grpc

from beam_tracking.schemas import ControlRequest

@dataclass
class RCGrpcConfig:
    host: str
    port: int
    timeout_s: float = 2.0
    retries: int = 3

class RCGrpcClient:
    """gRPC client wrapper for OSC RC xApp.

    This file is intentionally minimal and **proto-agnostic**:
    - After you run `scripts/gen_rc_protos.sh`, import generated stubs here and map ControlRequest -> protobuf message.
    """

    def __init__(self, cfg: RCGrpcConfig):
        self.cfg = cfg
        self._channel = grpc.insecure_channel(f"{cfg.host}:{cfg.port}")

        # TODO: after proto generation
        self._stub = None

    def send_control(self, req: ControlRequest) -> None:
        last_err: Optional[Exception] = None
        for attempt in range(1, self.cfg.retries + 1):
            try:
                # TODO: replace with actual protobuf mapping + stub call
                # e.g., pb_req = rc_pb2.RcControlRequest(...)
                # self._stub.SendControl(pb_req, timeout=self.cfg.timeout_s)
                raise NotImplementedError(
                    "RC proto stubs not generated. Run scripts/gen_rc_protos.sh and wire the stub."
                )
            except Exception as e:
                last_err = e
                if attempt < self.cfg.retries:
                    time.sleep(0.2 * attempt)
                    continue
                raise last_err
