#!/usr/bin/env bash
set -euo pipefail

# Generate Python gRPC stubs from ric-app-rc protos.
# This script intentionally uses local clone to avoid vendoring the whole repo.

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TP_DIR="${ROOT_DIR}/third_party/ric-app-rc"

if [ ! -d "${TP_DIR}" ]; then
  echo "Missing ${TP_DIR}. Run: bash scripts/bootstrap_external_repos.sh" >&2
  exit 1
fi

# TODO: Adjust the proto paths once you confirm where rc protobuf lives.
# Use `find third_party/ric-app-rc -name '*.proto' | head` to locate.
PROTO_DIR="${TP_DIR}"

OUT_DIR="${ROOT_DIR}/beam_tracking/ric/generated"
mkdir -p "${OUT_DIR}"

python -m grpc_tools.protoc   -I "${PROTO_DIR}"   --python_out="${OUT_DIR}"   --grpc_python_out="${OUT_DIR}"   $(find "${PROTO_DIR}" -name '*.proto' | tr '\n' ' ')

echo "Generated stubs under: beam_tracking/ric/generated"
echo "Now wire imports in beam_tracking/ric/rc_grpc_client.py"
