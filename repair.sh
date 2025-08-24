#!/bin/bash

set -euxo pipefail

WHEEL="$1"
DEST_DIR="$2"

if [ "${AUDITWHEEL_ARCH}" == "x86_64" ] || [ "${AUDITWHEEL_ARCH}" == "i686" ]; then
	PLATFORM_TAG="manylinux1_${AUDITWHEEL_ARCH}.manylinux_2_5_${AUDITWHEEL_ARCH}.musllinux_1_1_${AUDITWHEEL_ARCH}"
elif [ "${AUDITWHEEL_ARCH}" == "riscv64" ]; then
	PLATFORM_TAG="manylinux_2_31_${AUDITWHEEL_ARCH}.musllinux_1_1_${AUDITWHEEL_ARCH}"
else
	PLATFORM_TAG="manylinux2014_${AUDITWHEEL_ARCH}.manylinux_2_17_${AUDITWHEEL_ARCH}.musllinux_1_1_${AUDITWHEEL_ARCH}"
fi

cp "${WHEEL}" "${DEST_DIR}/"
pipx run 'wheel>=0.42' tags --remove --platform-tag "${PLATFORM_TAG}" "${DEST_DIR}"/*.whl
