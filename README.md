# django-cookiecutter

Cookiecutter шаблон для Django-проекта.

# Сервисы:

NGINX

BACKEND - Django

DB - Postgres

REDIS (queue, cache)

CELERY 

# Usage:

`cookiecutter django-cookiecutter`

`docker-compose up -d --build`



# Переменные окружения

Для локальной разработки нужно добавить файл .env в корень проекта, пример контента:
```
DEBUG=True
ALLOWED_HOSTS=*
INTERNAL_IPS=localhost,127.0.0.1
POSTGRES_PASSWORD=postgres

# nginx
TLS_MODE=off
SITE_HOST=localhost
ENVIRONMENT=development
```