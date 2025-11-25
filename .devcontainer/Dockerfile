# https://mcr.microsoft.com/v2/devcontainers/python/tags/list
FROM mcr.microsoft.com/devcontainers/python:2.1-3.13-bookworm

ENV PYTHONUNBUFFERED 1

ARG DEBIAN_FRONTEND=noninteractive
ARG USER=vscode

RUN DEBIAN_FRONTEND=noninteractive \
    && apt-get update \
    && apt-get install -y build-essential \
    ca-certificates \
    curl \
    git \
    python3-dev \
    wget \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && git config --global user.name "OttawaSTEM" \
    && git config --global user.email "ottawasteem@gmail.com" \
    && pip install --upgrade pip \
    && pip install uv
