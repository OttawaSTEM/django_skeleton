FROM python:3.12.11-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

RUN mkdir -p /app
WORKDIR /app
COPY . /app/

ENV PYTHONUNBUFFERED=1

RUN uv sync --no-dev --locked

EXPOSE 5000
CMD ["uv", "run", "manage.py", "runserver"]