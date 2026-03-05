FROM mcr.microsoft.com/devcontainers/python:3-3.14-trixie

ENV PYTHONUNBUFFERED 1

ARG USER=vscode

RUN apt-get update \
    && apt-get install -y build-essential \
    ca-certificates \
    curl \
    git \
    python3-dev \
    wget \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && git config --global user.name "OttawaSTEM" \
    && git config --global user.email "ottawastem@gmail.com" \
    && pip install --upgrade pip \
    && pip install uv


# [Optional] If your requirements rarely change, uncomment this section to add them to the image.
# COPY requirements.txt /tmp/pip-tmp/
# RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
#    && rm -rf /tmp/pip-tmp

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>



