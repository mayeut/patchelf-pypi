FROM python:3.13-alpine3.22
RUN apk add --no-cache autoconf automake bash build-base cmake git tar
RUN mkdir -p /opt/python && \
    ln -s /usr/local /opt/python/cp39-cp39 && \
    ln -s /usr/local /opt/python/cp313-cp313

RUN /usr/local/bin/python3 -m pip install pipx build

ARG TARGETARCH

ARG PLATFORM=${TARGETARCH}
ARG PLATFORM=${PLATFORM/amd64/x86_64}
ARG PLATFORM=${PLATFORM/386/i686}
ARG PLATFORM=${PLATFORM/arm64/aarch64}
ARG PLATFORM=${PLATFORM/arm/armv7l}

ARG MANYLINUX1=${PLATFORM/x86_64/manylinux1}
ARG MANYLINUX1=${MANYLINUX1/i686/manylinux1}
ARG MANYLINUX1=${MANYLINUX1##manylinux1}

ARG ALIAS1=${MANYLINUX1:+manylinux2014}
ARG ALIAS1=${ALIAS1:-manylinux1}

ARG ALIAS2=${ALIAS1/manylinux1/manylinux_2_5}
ARG ALIAS2=${ALIAS2/manylinux2014/manylinux_2_17}
ARG ALIAS2=${ALIAS2}_${PLATFORM}
ARG ALIAS2=${ALIAS2/manylinux_2_17_riscv64/manylinux_2_31_riscv64}

ARG ALIAS1=${ALIAS1}_${PLATFORM}.
ARG ALIAS1=${ALIAS1/manylinux2014_riscv64./}

ENV PLATFORM_TAG=${ALIAS2}.${ALIAS1}musllinux_1_1_${PLATFORM}
