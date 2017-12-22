FROM node:9.2.1

COPY client/package.json /usr/src/app/client/package.json

WORKDIR /usr/src/app/docker

RUN cd ../client && yarn install