from __future__ import annotations
from abc import ABC, abstractmethod

from beam_tracking.schemas import ControlRequest

class ActionDispatcher(ABC):
    @abstractmethod
    def dispatch(self, req: ControlRequest) -> None:
        raise NotImplementedError
