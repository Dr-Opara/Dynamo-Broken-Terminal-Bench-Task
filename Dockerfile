# Pin by digest for reproducibility — no :latest tags
# python:3.12-slim as of 2026-06-16
FROM python:3.12-slim@sha256:59b67b6d10b8a5f4a7f57af0087a44d4a0a3f8eec5c3a0b1fcbf7b8e4b7b2a3f

RUN pip install --no-cache-dir pytest==8.4.1 pytest-json-ctrf==0.3.5

WORKDIR /app

# Copy only the access log — no solution files
COPY access.log /app/access.log
