FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080
ENTRYPOINT ["python3", "-m", "uvicorn", "app.src.main:app", "--host", "0.0.0.0", "--port", "8080"]
#ENTRYPOINT ["gunicorn", "--worker-class", "uvicorn.workers.UvicornWorker", "--timeout", "600", "--access-logfile", "-", "--error-logfile", "-", "--bind", "0.0.0.0:8080", "src.main:app"]
