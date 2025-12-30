.PHONY: help bootstrap venv lint test fmt run-sim run-xapp

help:
	@echo "Targets:"
	@echo "  bootstrap   Install deps (venv + pip)"
	@echo "  lint        Run ruff"
	@echo "  fmt         Format imports (ruff)"
	@echo "  test        Run pytest"
	@echo "  run-sim     Run xApp in sim mode"
	@echo "  run-xapp    Run xApp in RIC mode (expects RC xApp reachable)"

bootstrap:
	python -m venv .venv
	. .venv/bin/activate && pip install -U pip && pip install -r requirements.txt

lint:
	. .venv/bin/activate && ruff check .

fmt:
	. .venv/bin/activate && ruff check --fix .

test:
	. .venv/bin/activate && pytest -q

run-sim:
	. .venv/bin/activate && python -m beam_tracking.xapp.main --mode sim --config configs/sim.yaml

run-xapp:
	. .venv/bin/activate && python -m beam_tracking.xapp.main --mode ric --config configs/ric.yaml
