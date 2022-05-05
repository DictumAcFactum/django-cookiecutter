# Cookiecutter template for Django project.

## Services:

NGINX

BACKEND - Django

DB - Postgres

REDIS (queue, cache)

CELERY 

## Usage:

`cookiecutter django-cookiecutter`

`docker-compose up -d --build`



## Environment variables

You should add `.env` file to the project's root. Example of the `.env` file
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