FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -U pip && pip install -r requirements.txt

COPY . .
CMD ["python","-m","beam_tracking.xapp.main","--mode","sim","--config","configs/sim.yaml"]
