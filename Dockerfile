FROM python:3.13.0-slim-bookworm
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]


