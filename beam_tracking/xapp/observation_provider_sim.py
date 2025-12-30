from __future__ import annotations
import json
from pathlib import Path
from typing import Iterable

from beam_tracking.schemas import Observation
from .observation_provider import ObservationProvider

class JSONLObservationProvider(ObservationProvider):
    def __init__(self, path: str):
        self.path = Path(path)

    def stream(self) -> Iterable[Observation]:
        with self.path.open("r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                yield Observation.model_validate(json.loads(line))
