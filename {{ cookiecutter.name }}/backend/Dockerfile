FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apk add --no-cache \
    build-base make gcc g++ `# for py packages` \
    postgresql-dev libpq `# for psycopg2` \
    libjpeg-turbo-dev zlib-dev libffi-dev cairo-dev libwebp-dev `# for pillow` \
    musl-dev python3-dev libffi-dev openssl-dev cargo `# for cryptography`

COPY Pipfile Pipfile.lock /app/
RUN pip install pipenv && pipenv install --system

COPY / /app/
RUN chmod +x entrypoint.sh