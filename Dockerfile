FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT ["gunicorn", "--worker-class", "uvicorn.workers.UvicornWorker", "--timeout", "600", "--access-logfile", "-", "--error-logfile", "-", "--bind", "0.0.0.0:8000", "src/main:app"]
