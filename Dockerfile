ARG ARCH=amd64
FROM ${ARCH}/python:3.11-alpine3.17
RUN if [ "$(uname -m)" == "armv7l" ]; then sed -i -e 's/v3\.17/edge/g' /etc/apk/repositories; fi
RUN apk update && apk upgrade
RUN apk add --no-cache autoconf automake bash build-base cmake git tar
RUN mkdir -p /opt/python && \
    ln -s /usr/local /opt/python/cp38-cp38 && \
    ln -s /usr/local /opt/python/cp311-cp311
