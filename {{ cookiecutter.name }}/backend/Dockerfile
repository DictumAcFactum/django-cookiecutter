FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1
ENV PATH="${PATH}:/root/.local/bin"

WORKDIR /app

RUN apk add --no-cache \
    build-base make gcc g++ `# для сборки пакетов` \
    postgresql-dev libpq `# для psycopg2` \
    libjpeg-turbo-dev zlib-dev libffi-dev cairo-dev libwebp-dev `# для pillow` \
    musl-dev python3-dev libffi-dev openssl-dev cargo `# для cryptography`

COPY Pipfile Pipfile.lock /app/
RUN pip install pipenv && pipenv install --system

COPY / /app/
RUN chmod +x entrypoint.sh