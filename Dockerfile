ARG ARCH=amd64
FROM ${ARCH}/python:3.9-alpine3.15
RUN apk add --no-cache autoconf automake bash build-base cmake git
RUN mkdir -p /opt/python && \
    ln -s /usr/local /opt/python/cp38-cp38 && \
    ln -s /usr/local /opt/python/cp39-cp39
