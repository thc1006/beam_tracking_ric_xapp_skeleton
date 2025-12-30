#!/usr/bin/env bash
set -euo pipefail

mkdir -p third_party
cd third_party

if [ ! -d ric-app-rc ]; then
  git clone https://github.com/o-ran-sc/ric-app-rc.git
fi

echo "Done. Repo is at third_party/ric-app-rc"
echo "Next: run scripts/gen_rc_protos.sh to generate python gRPC stubs."
