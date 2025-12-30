from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class ModelConfig:
    variant: str = "rsrp_student"
    device: str = "cpu"

@dataclass(frozen=True)
class RCConfig:
    enabled: bool = False
    host: str = "rc-xapp"
    port: int = 50051
    timeout_s: float = 2.0
    retries: int = 3

@dataclass(frozen=True)
class AppConfig:
    mode: str = "sim"  # sim | ric
    log_level: str = "INFO"
    model: ModelConfig = ModelConfig()
    rc: RCConfig = RCConfig()
