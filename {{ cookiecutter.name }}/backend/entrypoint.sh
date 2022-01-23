#!/bin/sh
python backend/manage.py migrate
exec "$@"
