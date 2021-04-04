FROM python:3.8.5-slim as api-base
WORKDIR /app

RUN apt-get update && \
    apt-get install -y \
        build-essential \
        default-libmysqlclient-dev --no-install-recommends
RUN pip install pipenv

FROM api-base as prd-stg
COPY ./src/ /app/
RUN pipenv install --deploy --system

FROM prd-stg AS dev

# Redundant but needed for syncing of development files.
COPY ./src/ /app/
RUN pipenv install --dev --deploy --system
