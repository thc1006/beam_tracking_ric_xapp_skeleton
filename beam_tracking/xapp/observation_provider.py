from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Iterable

from beam_tracking.schemas import Observation

class ObservationProvider(ABC):
    @abstractmethod
    def stream(self) -> Iterable[Observation]:
        """Yield Observations."""
        raise NotImplementedError
