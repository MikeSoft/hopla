FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add --no-cache \
    python3-dev \
    gcc \
    libc-dev \
    libmemcached-dev \
    zlib-dev \
    libffi-dev \
    openssl-dev

COPY . /app

WORKDIR /app
COPY requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install importlib-metadata==4.8.1  # Asegúrate de instalar una versión compatible
RUN pip install gunicorn
RUN pip install -r requirements.txt
