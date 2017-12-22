FROM python:3.6.3

RUN apt-get update && apt-get -y install supervisor

COPY server/requirements.txt /usr/src/app/server/requirements.txt
COPY docker/server/entrypoint.sh /usr/src/app/docker/server/entrypoint.sh
COPY docker/server/supervisor/supervisord.conf /usr/src/app/supervisord.conf

WORKDIR /usr/src/app/docker

RUN pip install -r ../server/requirements.txt \
    && chmod +x ./server/entrypoint.sh

WORKDIR /usr/src/app/server