# Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

# 👇 adjust api:app to match your filename and FastAPI instance
CMD ["uvicorn", "fastapi_app:app", "--host", "0.0.0.0", "--port", "8080"]