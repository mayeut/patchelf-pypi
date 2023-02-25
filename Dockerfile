ARG ARCH=amd64
FROM ${ARCH}/python:3.11-alpine3.17
RUN apk add --no-cache autoconf automake bash build-base cmake git
RUN mkdir -p /opt/python && \
    ln -s /usr/local /opt/python/cp38-cp38 && \
    ln -s /usr/local /opt/python/cp311-cp311
