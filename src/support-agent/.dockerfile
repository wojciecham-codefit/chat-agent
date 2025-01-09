FROM python:3.13-slim AS builder

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/.poetry

RUN apt update
RUN apt install -y pipx
RUN pipx install poetry

ENV PATH=/root/.local/bin:$PATH
ENV PATH="/home/appusr/.local/bin:$PATH"

RUN adduser --disabled-password appusr
RUN mkdir -p /home/appusr/app
RUN chown appusr:appusr /home/appusr/app
WORKDIR /home/appusr/app
USER appusr

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root

FROM python:3.13-slim AS runtime

EXPOSE 8555

RUN adduser --disabled-password appusr
RUN mkdir -p /home/appusr/app
RUN chown appusr:appusr /home/appusr/app
WORKDIR /home/appusr/app
USER appusr

ENV VIRTUAL_ENV=.venv
ENV PATH=/home/appusr/app/.venv/bin:$PATH
ENV UVICORN_RELOAD=False

COPY --from=builder /home/appusr/app/${VIRTUAL_ENV} ${VIRTUAL_ENV}

COPY api api
COPY application application
COPY domain domain
COPY main.py main.py

ENTRYPOINT ["python", "main.py"]


