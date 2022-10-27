FROM python:3.10-alpine

ARG POETRY_PARAMS=""
ENV PYTHONUNBUFFERED 1
ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

RUN apk add --no-cache \
    build-base make gcc g++ `# for py packages` \
    postgresql-dev libpq `# for psycopg2` \
    libjpeg-turbo-dev zlib-dev libffi-dev cairo-dev libwebp-dev `# for pillow` \
    gcc musl-dev python3-dev openssl-dev cargo `# for cryptography` \
    && pip install poetry && poetry install $POETRY_PARAMS --no-interaction --no-ansi

COPY / /app/
RUN chmod +x entrypoint.sh