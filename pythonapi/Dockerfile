# syntax=docker/dockerfile:1
ARG PROJECT_NAME=test_dev
ARG DOMAIN=https://geoserver.massimilianomoraca.me
ARG WORKSPACE=MassimilianoMoraca
ARG SERVICE_VERSION=1.3.0
ARG LAYER_NAME=NDVI_Campania_20150807

# Official Ubuntu Image as Layer
FROM maxdragonheart/ulgis:latest as gis-os
# Disable Prompt During Packages Installation
ARG DEBIAN_FRONTEND=noninteractive

# GIS-OS as Layer
FROM gis-os as project-dependencies
# Set work directory
WORKDIR /app/web
# Environment variables
ARG PROJECT_NAME=python-api

ENV ENV_NAME=${PROJECT_NAME} \
    ENV_DOMAIN=${DOMAIN} \
    ENV_WORKSPACE=${WORKSPACE} \
    ENV_SERVICE_VERSION=${SERVICE_VERSION} \
    ENV_LAYER_NAME=${LAYER_NAME} \
    # Pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    # Poetry
    # https://python-poetry.org/docs/configuration/#using-environment-variables
    # https://python-poetry.org/docs#ci-recommendations
    POETRY_VERSION=1.2.1 \
    POETRY_HOME=/opt/poetry \
    POETRY_VENV=/opt/poetry-venv \
    POETRY_CACHE_DIR=/opt/.cache

# Install Poetry
RUN python3 -m venv $POETRY_VENV \
    && $POETRY_VENV/bin/pip install -U pip setuptools \
    && $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}

# Add Poetry to PATH
ENV PATH="${PATH}:${POETRY_VENV}/bin"

# Copy project requirements
COPY pyproject.toml ./pyproject.toml

# Project initialization
RUN poetry install --only main --no-root --no-ansi

# Copy project data
COPY app app

CMD [ "poetry", "run", "python3", "./app/app.py" ]