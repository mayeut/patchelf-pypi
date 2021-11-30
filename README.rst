=============
patchelf PyPI
=============

`patchelf <https://github.com/NixOS/patchelf>`_ is a  small utility to modify the dynamic linker
and RPATH of ELF executables.

This project allows to get this utility from `PyPI <https://pypi.org>`_ with a simple ``pip install patchelf``.

Latest Release
--------------

.. image:: https://img.shields.io/pypi/v/patchelf.svg
  :target: https://pypi.python.org/pypi/patchelf

Build Status
------------

.. image:: https://github.com/mayeut/patchelf-pypi/actions/workflows/build.yml/badge.svg
  :target: https://github.com/mayeut/patchelf-pypi/actions/workflows/build.yml

Platforms
---------

The following platforms are supported with binary wheels:

.. table::

  +---------------+--------------------------+
  | OS            | Arch                     |
  +===============+==========================+
  | Linux x86_64  | | manylinux1+            |
  |               | | musllinux_1_1+         |
  +---------------+--------------------------+
  | Linux i686    | | manylinux1+            |
  |               | | musllinux_1_1+         |
  +---------------+--------------------------+
  | Linux aarch64 | | manylinux2014+         |
  |               | | musllinux_1_1+         |
  +---------------+--------------------------+
  | Linux ppc64le | | manylinux2014+         |
  |               | | musllinux_1_1+         |
  +---------------+--------------------------+
  | Linux s390x   | | manylinux2014+         |
  |               | | musllinux_1_1+         |
  +---------------+--------------------------+

License
-------

This project is covered by the `Apache License, Version 2.0 <http://www.apache.org/licenses/LICENSE-2.0>`_.

patchelf is distributed under the OSI-approved GNU General Public License v3.0.
For more information about patchelf, visit https://github.com/NixOS/patchelf
