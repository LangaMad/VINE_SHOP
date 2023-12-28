FROM python:3.11-slim
RUN mkdir vine_shop
WORKDIR vine_shop
ADD . /vine_shop/
ADD .env.docker /vine_shop/.env
# Устанавливаем зависимости PostgreSQL
RUN apt-get update && apt-get install -y libpq-dev gcc
ENV APP_NAME = DOCKER_DEMO
RUN pip install -r requirements.txt
CMD gunicorn config.wsgi:application -b 0.0.0.0:8000



