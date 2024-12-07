FROM python:3.12-alpine3.20
RUN apk add --no-cache autoconf automake bash build-base cmake git tar
RUN mkdir -p /opt/python && \
    ln -s /usr/local /opt/python/cp39-cp39 && \
    ln -s /usr/local /opt/python/cp312-cp312
