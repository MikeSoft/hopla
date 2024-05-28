#!/bin/sh

python manage.py collectstatic --noinput
gunicorn hopla.wsgi --bind 0.0.0.0:8000 --workers 2 --threads 2