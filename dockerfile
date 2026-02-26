FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get upgrade -y && \
    python -m pip install --no-cache-dir --upgrade pip setuptools wheel && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

USER appuser

EXPOSE 5000

CMD ["python", "app.py"]