DJANGO_SUPERUSER_NAME := "admin"
export DJANGO_SUPERUSER_PASSWORD := "password"

help:
    just -l

run:
    python manage.py runserver

scrape:
    rm -f fixtures/imports.jsonl
    mkdir -p fixtures
    python -m scrapy runspider ./scripts/spider.py -o fixtures/imports.jsonl

import: scrape
    python manage.py import

bootstrap:
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser --no-input --username {{DJANGO_SUPERUSER_NAME}} --email admin@example.com
    python manage.py import



