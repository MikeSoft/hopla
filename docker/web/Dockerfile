FROM python:3.12.3-alpine

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
RUN pip install gunicorn
RUN pip install -r requirements.txt

CMD ["sh", "-c", "python manage.py collectstatic --settings=hopla.settings_docker --noinput && python manage.py migrate --settings=losfunables.settings_docker && /usr/local/bin/gunicorn losfunables.wsgi:application -w 2 -b :8000"]
