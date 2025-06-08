FROM python:3.10-slim

WORKDIR /app

COPY inferencia.py .

RUN pip install --no-cache-dir requests

CMD ["python", "inferencia.py"]
