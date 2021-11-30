# -*- coding: utf-8 -*-
import os
import sys

DATA = os.path.join(os.path.dirname(__file__), 'data')
BIN_DIR = os.path.join(DATA, 'bin')


def _program(name, args):
    os.execv(os.path.join(BIN_DIR, name), [name] + args)


def patchelf():
    _program('patchelf', sys.argv[1:])
