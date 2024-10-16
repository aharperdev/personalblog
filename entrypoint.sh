#!/bin/sh

python manage.py migrate --noinput
python manage.py tailwind install
python manage.py tailwind build
python manage.py collectstatic --noinput

gunicorn personalblog.wsgi:application --bind 0.0.0.0:8080