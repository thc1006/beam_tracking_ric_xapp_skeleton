from __future__ import annotations

from beam_tracking.schemas import ControlRequest
from beam_tracking.ric.rc_grpc_client import RCGrpcClient

from .action_dispatcher import ActionDispatcher

class RCActionDispatcher(ActionDispatcher):
    def __init__(self, client: RCGrpcClient):
        self.client = client

    def dispatch(self, req: ControlRequest) -> None:
        self.client.send_control(req)
