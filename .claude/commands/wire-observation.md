Goal: implement a real ObservationProvider that can later be fed by KPM Indications.

For now:
- Implement a provider that reads JSON messages (same schema as Observation) from stdin or a UDP socket.
- Add config entries to configs/ric.yaml.
- Ensure Observation validation errors are logged but do not crash the loop.

Add tests for schema validation.
