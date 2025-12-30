# Claude Code: Beam Tracking RIC xApp Project Instructions

## What success looks like (definition of done)
1) **Sim mode**: `make run-sim` can run end-to-end:
   - load a mock Observation stream
   - run the policy to produce an Action
   - log decisions and maintain minimal state
2) **RIC mode**: `make run-xapp` can:
   - connect to RC xApp gRPC endpoint
   - send a Control request with `target_beam_id` (or `target_cell_id`) + UE identifier
   - handle retries/timeouts cleanly
3) Code is structured so later we can swap the observation provider:
   - CSI-heavy (offline / Sionna dataset)
   - RSRP-light (real RIC: KPM/PM style or UE measurement report)

## Non-negotiables
- Keep the code **modular**: observation → feature extraction → policy → action dispatch.
- Prefer **typed dataclasses / pydantic models** for Observation/Action schemas.
- Avoid hard-coding shapes. Centralize in `beam_tracking/config.py`.
- Never "poll" the E2 node from xApp for periodic KPM; periodic reporting should come from the **subscription's Event Trigger / Reporting Period** (see `docs/kpm_reporting_period_notes.md`).

## Repository map (where to work)
- `beam_tracking/schemas.py`: canonical Observation/Action models.
- `beam_tracking/xapp/`: runtime loop + integration glue.
- `beam_tracking/ric/rc_grpc_client.py`: the one place to talk to RC xApp.
- `beam_tracking/model/`: keep networks small & inference-safe; training scripts live in `scripts/`.

## Workflow guidance
When implementing a feature:
1) Start with tests in `tests/` for shape + serialization.
2) Implement the minimal code path.
3) Add an example config to `configs/`.
4) Update relevant docs in `docs/` if it changes interfaces.

## External dependencies policy
- Do **not** vendor the full `ric-app-rc` repo here.
- Use `scripts/bootstrap_external_repos.sh` to clone it under `third_party/`.
- Proto generation must be reproducible via `scripts/gen_rc_protos.sh`.

## Suggested next tasks (in order)
1) Finish `scripts/gen_rc_protos.sh` and wire it into `beam_tracking/ric/rc_grpc_client.py`
2) Implement `ObservationProvider` interface and a first real provider:
   - Sim provider reads `resources/sample/` JSON
3) Implement action dispatcher:
   - Map Action → RC gRPC request payload
4) Add a "distilled" lightweight policy model:
   - offline teacher (CSI) → student (RSRP)

