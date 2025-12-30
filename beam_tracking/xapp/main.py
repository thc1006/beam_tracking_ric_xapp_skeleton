from __future__ import annotations
import argparse
import logging
import time
from pathlib import Path

import yaml

from beam_tracking.model.inference import InferenceEngine
from beam_tracking.schemas import Action, ControlRequest
from beam_tracking.ric.rc_grpc_client import RCGrpcClient, RCGrpcConfig
from .observation_provider_sim import JSONLObservationProvider
from .action_dispatcher_rc import RCActionDispatcher

N_BEAMS_DEFAULT = 5  # demo; replace with real number (e.g., 77) when wired

def load_config(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["sim","ric"], required=True)
    ap.add_argument("--config", required=True)
    args = ap.parse_args()

    cfg = load_config(args.config)
    logging.basicConfig(level=getattr(logging, cfg.get("log_level","INFO")))
    log = logging.getLogger("beam-tracking-xapp")

    engine = InferenceEngine(n_beams=N_BEAMS_DEFAULT, device=cfg.get("model",{}).get("device","cpu"))

    if args.mode == "sim":
        obs_path = cfg.get("sim",{}).get("observation_path")
        step_hz = float(cfg.get("sim",{}).get("step_hz", 10))
        provider = JSONLObservationProvider(obs_path)
        for obs in provider.stream():
            res = engine.act(obs.rsrp_vector)
            action = Action(target_beam_id=res.target_beam_id, confidence=res.confidence)
            log.info("SIM decision ue=%s beam=%s conf=%.3f", obs.ue_id, action.target_beam_id, action.confidence)
            time.sleep(1.0/step_hz)
        return

    # RIC mode
    if not cfg.get("rc",{}).get("enabled", True):
        raise SystemExit("RIC mode requires rc.enabled=true in config")

    rc_cfg = RCGrpcConfig(
        host=cfg["rc"]["host"],
        port=int(cfg["rc"]["port"]),
        timeout_s=float(cfg["rc"].get("timeout_s", 2.0)),
        retries=int(cfg["rc"].get("retries", 3)),
    )
    rc_client = RCGrpcClient(rc_cfg)
    dispatcher = RCActionDispatcher(rc_client)

    # For now, reuse sim provider as a "source" of obs. Replace with KPM provider later.
    obs_path = cfg.get("sim",{}).get("observation_path","resources/sample/observation_stream.jsonl")
    provider = JSONLObservationProvider(obs_path)

    for obs in provider.stream():
        res = engine.act(obs.rsrp_vector)
        action = Action(target_beam_id=res.target_beam_id, confidence=res.confidence)
        ctrl = ControlRequest(ue_id=obs.ue_id, action=action)
        log.info("RIC dispatch ue=%s beam=%s conf=%.3f", obs.ue_id, action.target_beam_id, action.confidence)
        dispatcher.dispatch(ctrl)

if __name__ == "__main__":
    main()
