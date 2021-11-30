#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from setuptools_scm import get_version
from skbuild import setup
from wheel.bdist_wheel import bdist_wheel as _bdist_wheel


class bdist_wheel(_bdist_wheel):
    def finalize_options(self):
        _bdist_wheel.finalize_options(self)
        self.root_is_pure = False

    def get_tag(self):
        python, abi, plat = _bdist_wheel.get_tag(self)
        python, abi = "py2.py3", "none"
        if os.environ.get("CIBUILDWHEEL", "0") == "1":
            assert plat.startswith("linux_")
            arch = plat[6:]
            tags = []
            if arch in {"i686", "x86_64"}:
                tags = ["manylinux_2_5_{arch}", "manylinux1_{arch}"]
            else:
                tags = ["manylinux_2_17_{arch}", "manylinux2014_{arch}"]
            tags.append("musllinux_1_1_{arch}")
            plat = ".".join([tag.format(arch=arch) for tag in tags])
        return python, abi, plat


with open("README.rst", "r") as fp:
    readme = fp.read()

cmdclass = {"bdist_wheel": bdist_wheel}

setup(
    name="patchelf",

    maintainer="Matthieu Darbois",
    maintainer_email="mayeut@users.noreply.github.com",

    version=get_version(),
    cmdclass=cmdclass,

    cmake_install_dir="src/patchelf/data",

    package_dir={"": "src"},
    packages=["patchelf"],
    entry_points={
        'console_scripts': [
            'patchelf=patchelf:patchelf'
        ]
    },

    url="https://github.com/NixOS/patchelf",
    project_urls={
        "Source Code": "https://github.com/mayeut/patchelf-pypi",
        "Bug Tracker": "https://github.com/mayeut/patchelf-pypi/issues",
    },

    description=(
        "A small utility to modify the dynamic linker and RPATH of ELF "
        "executables."
    ),
    long_description=readme,
    long_description_content_type="text/x-rst",
    classifiers=[
        (
            "License :: OSI Approved :: GNU General Public License v3 or "
            "later (GPLv3+)"
        ),
        "Programming Language :: C",
        "Programming Language :: C++",
        "Programming Language :: Python",
        "Operating System :: POSIX :: Linux",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
    ],

    license="GPL-3.0-or-later",
    license_files=["COPYING", "LICENSE"],
    keywords="patchelf auditwheel elf manylinux musllinux",

    extras_require={"test": "pytest"},
)
