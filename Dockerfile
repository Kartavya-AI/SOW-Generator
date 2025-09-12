# Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

EXPOSE 8080

# Cloud Run will set PORT automatically; let Python read it
CMD ["python", "fastapi_app.py"]
