FROM python:3.8-alpine as builder

WORKDIR /heppa

COPY requirements.txt requirements.txt
RUN apk add --no-cache build-base \
    && pip3 install --no-cache-dir -r requirements.txt \
    && apk del --no-cache build-base

COPY . .

CMD ["gunicorn", "--preload", "--workers", "1", "--bind", "0.0.0.0:8000", "application:app"]