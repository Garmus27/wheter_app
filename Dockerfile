FROM python:3.13.0-slim-bookworm
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN mkdir -p /app
