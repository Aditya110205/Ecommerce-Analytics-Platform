# =====================
# Builder Stage
# =====================

FROM python:3.13-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install \
    --no-cache-dir \
    --prefix=/install \
    -r requirements.txt


# =====================
# Runtime Stage
# =====================

FROM python:3.13-slim

WORKDIR /app

COPY --from=builder /install /usr/local

COPY . .

EXPOSE 8000

HEALTHCHECK --interval=30s \
            --timeout=5s \
            --start-period=20s \
            --retries=3 \
CMD python -c "import requests; requests.get('http://localhost:8000/health')"

CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "api.main:app", "--bind", "0.0.0.0:8000"]