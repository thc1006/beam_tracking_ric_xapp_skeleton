Goal: generate RC xApp gRPC Python stubs and wire them.

Steps:
1) Run scripts/bootstrap_external_repos.sh
2) Locate where RC xApp proto definitions live under third_party/ric-app-rc (use find/grep)
3) Modify scripts/gen_rc_protos.sh to point to the correct proto include roots
4) Run scripts/gen_rc_protos.sh
5) Update beam_tracking/ric/rc_grpc_client.py to import generated modules and implement send_control()

Also add a minimal integration test that:
- constructs a protobuf request
- serializes it
- verifies required fields exist

Do not attempt to contact a real RC xApp unless explicitly asked.
