FROM python:3.11.0-alpine

ENV PYTHONUNBUFFERED 1

EXPOSE 5000

WORKDIR /app

COPY . .

RUN python -m venv /py && \
    pip install --upgrade pip && \
    /py/bin/pip install -r requirements.txt

ENV PATH="/py/bin:$PATH"
